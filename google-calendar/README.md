# SQL on Google Calendar


## Introduction

SQL on Google Calendar is a simple project that uses Google Calendar API to fetch events from a calendar and query it with [chDB](https://github.com/chdb-io/chdb) User Defined Table (UDT).

## Requirements

1. First, you need to enable the [Google Calendar API](https://developers.google.com/calendar/api/quickstart/python#enable_the_api) in the Google Cloud Console and download the `credentials.json` file.

2. Install the required packages.
    ```bash
    pip install -r requirements.txt
    ```

## Usage

Usage: `python google_cal.py sql [outputFormat]`

- sql: SQL query to run on the Google Calendar data, `FROM Python(cal)` could be omitted. Eg.:
  - SELECT summary, organizer_email, parseDateTimeBestEffortOrNull(start_dateTime) LIMIT 10;;
  - DESCRIBE Python(cal)

- outputFormat: Output format, e.g. Dataframe, CSV, JSON, PrettyCompact

## Example

```bash
python google_cal.py \
 "SELECT summary, organizer_email, parseDateTimeBestEffortOrNull(start_dateTime) WHERE status = 'confirmed';"
```

![Example](img/shot.png)


## Notice

- If you are using the Google Calendar API for the first time, you will be asked to authenticate and authorize the application to access your Google Calendar data. The credentials will be stored in a file named `token.json`.

- If running the script on a server, you may need to copy the `token.json` file to the server.

- You may got this authing on browser, please click `Advanced` and `Go to SQL on gCal (unsafe)` to continue. As all the data is processed locally (you can check the code yourself), it is safe to proceed. It will take some time to pass Google's review, so please be patient.

   ![Authing](img/api_warning.png)