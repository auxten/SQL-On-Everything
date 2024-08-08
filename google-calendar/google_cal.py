import os.path

# install with `pip install --upgrade google-auth-oauthlib google-auth-httplib2 google-api-python-client`
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

import chdb

# First, you need to enable the Google Calendar API in the Google Cloud Console
# and download the credentials.json file.
# https://developers.google.com/calendar/api/quickstart/python#enable_the_api

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"]


def getCalItems():
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    try:
        service = build("calendar", "v3", credentials=creds)
        events_result = service.events().list(calendarId="primary").execute()
        events = events_result.get("items", [])
        return chdb.utils.convert_to_columnar(events)

    except HttpError as error:
        print("An error occurred: %s" % error)


class myReader(chdb.PyReader):
    def __init__(self, data_fetcher):
        self.data_fetcher = data_fetcher
        super().__init__("")

    # If get_schema is not implemented, the schema will be inferred from the first batch of data
    def get_schema(self):
        self.data = self.data_fetcher()
        data_types = chdb.utils.infer_data_types(self.data)
        self.cursor = 0
        return data_types

    def read(self, col_names, count):
        if self.cursor >= len(self.data[col_names[0]]):
            return []
        start = self.cursor
        end = min(start + count, len(self.data[col_names[0]]))
        self.cursor = end
        return [self.data[col][start:end] for col in col_names]


if __name__ == "__main__":
    cal_reader = myReader(getCalItems)
    # print(chdb.query("DESCRIBE Python(cal_reader)"))
    # print(chdb.query("SELECT * FROM Python(cal_reader)", "Dataframe"))
    print(chdb.query("SELECT * FROM Python(cal_reader) LIMIT 1", "JSON"))
