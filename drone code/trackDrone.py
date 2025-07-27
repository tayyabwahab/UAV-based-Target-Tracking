"""
UAV Real-time Tracking System

This module implements real-time UAV control based on tracking coordinates received from
the main tracking system. It connects to Microsoft AirSim for UAV simulation and controls
drone movement based on target position changes.

Key Features:
- Microsoft AirSim integration for UAV simulation
- Real-time coordinate reception from tracking system
- Autonomous drone movement control
- Google Sheets integration for coordinate logging
- Continuous tracking loop with goto control flow

Author: UAV Security System Team
License: MIT
"""

import airsim

import sys
import time
import math

import gspread
from oauth2client.service_account import ServiceAccountCredentials

from goto import with_goto


scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('fypapi-275115-1487f536b9fc.json', scope)

gc = gspread.authorize(credentials)

wks = gc.open("droneCordinates").sheet1


''' 0.00520833335 '''


client = airsim.MultirotorClient()
client.confirmConnection()
client.enableApiControl(True)

client.armDisarm(True)

landed = client.getMultirotorState().landed_state
if landed == airsim.LandedState.Landed:
    print("taking off...")
    client.takeoffAsync().join()
else:
    client.hoverAsync().join()


def track_person(y, x):
    """
    Control UAV movement based on target coordinates.
    
    This function receives target coordinates and moves the UAV to follow the target.
    It calculates the relative position change and adjusts the UAV's position accordingly.
    
    Args:
        y (float): Y-coordinate of target position (relative movement)
        x (float): X-coordinate of target position (relative movement)
        
    Note:
        The function uses a scaling factor of 0.0104166667 to convert pixel coordinates
        to UAV movement distances. The UAV maintains a constant altitude of -5 meters.
    """
    start = client.getMultirotorState().kinematics_estimated.position
    z = -5
    start.x_val = start.x_val + ((-x) * 0.0104166667)
    start.y_val = start.y_val + (y * 0.0104166667) 
    client.moveToPositionAsync(start.x_val, start.y_val, z, 1).join()

@with_goto
def startFunc():
    """
    Main tracking function with continuous coordinate monitoring.
    
    This function implements the main tracking loop that continuously monitors
    Google Sheets for new coordinates and controls UAV movement accordingly.
    It uses goto statements for control flow management.
    
    The function:
    1. Reads coordinates from Google Sheets
    2. Converts coordinates to float values
    3. Calls track_person() to move UAV
    4. Deletes processed coordinates from sheet
    5. Loops back to start for continuous monitoring
    """
    label .start_the_tracking

    x = wks.cell(2,1).value
    y = wks.cell(2,2).value
    '''for x,y in arr:
        track_person(y,x)'''

    if x and y:
        x = float(x)
        y = float(y)
        track_person(x,y)

        wks.delete_row(2)

    goto .start_the_tracking

startFunc()

'''
if(var == True):
    track_person(x,y)
else:
    client = airsim.MultirotorClient()
    client.confirmConnection()
    client.enableApiControl(True)
    var=True
    track_person(x,y)'''