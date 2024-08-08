### Introduction

SQL on Google Calendar ("the Application") uses the Google Calendar API to fetch events from your calendar and allows querying these events using chDB User Defined Table (UDT). This Privacy Policy explains how we collect, use, and share information from users of the Application.

### Information We Collect

1. **Google Calendar Data**: When you use the Application, we access your Google Calendar data to fetch events based on your queries.
2. **Credentials**: To access your Google Calendar, you need to provide a `credentials.json` file which contains OAuth 2.0 credentials. This file is used to obtain an access token and a refresh token, stored in a file named `token.json`.

### How We Use Information

1. **Fetching Calendar Events**: The Application fetches events from your Google Calendar based on the SQL queries you provide.
2. **Storing Tokens**: The access token and refresh token are stored locally in the `token.json` file to allow the Application to access your Google Calendar data without requiring you to log in each time.

### Data Security

1. **Local Processing**: All data processing is done locally on your machine. No data is transmitted to external servers or third parties.
2. **Credentials and Tokens**: The `credentials.json` and `token.json` files are stored locally. It is your responsibility to keep these files secure and not share them.

### Data Sharing

We do not share your Google Calendar data or any other personal information with third parties.

### User Control

1. **Authorization**: You can revoke the Application's access to your Google Calendar at any time by removing the access token or revoking the Application's permission in the Google Account settings.
2. **Data Deletion**: To delete the access token and any associated data, simply delete the `token.json` file from your local machine.

### Notice Regarding Credentials

The `credentials.json` file included in the repository is for testing purposes only and should not be used in a production environment. Always create your own credentials when using the Application for any serious purposes.

### Changes to This Privacy Policy

We may update this Privacy Policy from time to time. Any changes will be posted on this page, and we will update the effective date at the top of the policy.

### Contact Us

If you have any questions or concerns about this Privacy Policy, please contact us at auxtenwpc@gmail.com