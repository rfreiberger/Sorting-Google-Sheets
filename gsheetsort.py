#!/usr/bin/env python3
# Title: gsheetsort.py
# Author: Robert Freiberger
# Repo: https://github.com/rfreiberger/Sorting-Google-Sheets
# Notes: This is code from the Google Sheets example code
#        https://developers.google.com/sheets/api/quickstart/python
# 
# 
from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import pprint

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'

def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    class bcolors:
        HEADER = '\033[95m'
        OKBLUE = '\033[94m'
        OKGREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'

    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('/Users/robert.freiberger/.config/credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('sheets', 'v4', http=creds.authorize(Http()))

    # Call the Sheets API
    # SPREADSHEET_ID = '1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms'
    SPREADSHEET_ID = '17OVdQhD0VVwxglrC9FD_JR2YEepaG-DUEe5os4r_4Ys'
    # RANGE_NAME = 'Class Data!A2:E'
    RANGE_NAME = '6 Aug 2018 Cut!A2:Q100'
    result = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID,
                                                range=RANGE_NAME).execute()
    values = result.get('values', [])

    if not values:
        print('No data found.')
    else:
        print(bcolors.BOLD + 'Migrations\t\t\t\t Run in US\t Run in EU\t Run in LA\t Before or After' + bcolors.ENDC)
        for row in values:
            # Print columns A and E, which correspond to indices 0 and 4.
            # Note - 
            # We need to print A through F, so that's 0 to 5
            print('%s\t\t %s\t\t %s\t\t %s\t\t %s' % (row[0], row[2], row[3], row[4], row[5]))

if __name__ == '__main__':
    main()
