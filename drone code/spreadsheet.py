"""
Google Sheets Coordinate Management System

This module provides coordinate management functionality using Google Sheets API.
It allows for real-time coordinate logging and retrieval for UAV control systems.

Key Features:
- Google Sheets API integration
- Real-time coordinate logging
- Coordinate data retrieval
- Service account authentication
- Spreadsheet management

Author: UAV Security System Team
License: MIT
"""

import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('fypapi-275115-1487f536b9fc.json', scope)

gc = gspread.authorize(credentials)

wks = gc.open("droneCordinates").sheet1

#print(wks.get_all_records())

#values_list = wks.row_values(2)

#if values_list:
#    print(values_list)

def log_coordinates(x, y):
    """
    Log coordinates to Google Sheets for UAV tracking.
    
    This function appends coordinate data to the Google Sheets spreadsheet
    for real-time UAV tracking and control.
    
    Args:
        x (float): X-coordinate of target position
        y (float): Y-coordinate of target position
        
    Note:
        Coordinates are appended as a new row to the spreadsheet.
        The UAV control system reads from row 2 and deletes processed coordinates.
    """
    wks.append_row([x, y])

def get_coordinates():
    """
    Retrieve coordinates from Google Sheets.
    
    Returns:
        tuple: (x, y) coordinates from the first available row, or (None, None) if empty
        
    Note:
        This function reads from row 2 of the spreadsheet where new coordinates
        are typically stored for processing.
    """
    x = wks.cell(2,1).value
    y = wks.cell(2,2).value
    return (x, y)

def delete_processed_coordinates():
    """
    Delete processed coordinates from Google Sheets.
    
    This function removes the second row (index 2) from the spreadsheet
    after coordinates have been processed by the UAV control system.
    """
    wks.delete_row(2)

# Example usage
x = 2515
y = 1254

log_coordinates(x, y)

#wks.delete_row(2)

# pip install PyOpenSSL
# pip install oauth2client
# pip install gspread

'''x = wks.cell(5,1).value
y=20

if x and y:
    x = float(x)   
    y=y+x
    print(y)'''