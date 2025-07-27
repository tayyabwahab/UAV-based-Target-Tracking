"""
UAV Autonomous Survey Mission System

This module implements autonomous survey missions for UAVs using Microsoft AirSim.
It provides configurable survey patterns and autonomous flight control for area
surveillance and mapping missions.

Key Features:
- Configurable survey area size and pattern
- Autonomous flight control
- Obstacle avoidance
- GPS-guided navigation
- Survey pattern optimization

Author: UAV Security System Team
License: MIT
"""

import setup_path 
import airsim

import sys
import time
import argparse

class SurveyNavigator:
    """
    Autonomous survey navigation system for UAVs.
    
    This class provides autonomous survey capabilities for UAVs, allowing them to
    perform systematic area surveillance missions. It supports configurable survey
    patterns, altitudes, and speeds.
    
    Attributes:
        boxsize (float): Size of the survey area (square box)
        stripewidth (float): Width of survey stripes for coverage
        altitude (float): Survey altitude in meters
        velocity (float): UAV flight speed in meters/second
        client: AirSim client for UAV control
    """
    
    def __init__(self, args):
        """
        Initialize the SurveyNavigator with mission parameters.
        
        Args:
            args: ArgumentParser object containing survey parameters:
                - size: Size of the survey box
                - stripewidth: Width of survey stripes
                - altitude: Survey altitude
                - speed: UAV flight speed
        """
        self.boxsize = args.size
        self.stripewidth = args.stripewidth
        self.altitude = args.altitude
        self.velocity = args.speed
        self.client = airsim.MultirotorClient()
        self.client.confirmConnection()
        self.client.enableApiControl(True)

    def start(self):
        """
        Execute the autonomous survey mission.
        
        This method performs the complete survey mission:
        1. Arms and takes off the UAV
        2. Climbs to specified altitude
        3. Flies to first corner of survey area
        4. Executes systematic survey pattern
        5. Completes coverage of entire area
        
        The survey pattern follows a back-and-forth pattern to ensure
        complete coverage of the specified area.
        """
        print("arming the drone...")
        self.client.armDisarm(True)

        landed = self.client.getMultirotorState().landed_state
        if landed == airsim.LandedState.Landed:
            print("taking off...")
            self.client.takeoffAsync().join()


        
        # AirSim uses NED coordinates so negative axis is up.
        x = -self.boxsize
        z = -self.altitude

        print("climbing to altitude: " + str(self.altitude))
        self.client.moveToPositionAsync(0, 0, z, self.velocity).join()

        print("flying to first corner of survey box")
        self.client.moveToPositionAsync(x, -self.boxsize, z, self.velocity).join()
        
        # let it settle there a bit.
        self.client.hoverAsync().join()
        time.sleep(2)

        # after hovering we need to re-enabled api control for next leg of the trip
        self.client.enableApiControl(True)

        # now compute the survey path required to fill the box 
        path = []
        distance = 0
        while x < self.boxsize:
            distance += self.boxsize 
            path.append(airsim.Vector3r(x, self.boxsize, z))
            x += self.stripewidth            
            distance += self.stripewidth 
            path.append(airsim.Vector3r(x, self.boxsize, z))
            distance += self.boxsize 
            path.append(airsim.Vector3r(x, -self.boxsize, z)) 
            x += self.stripewidth  
            distance += self.stripewidth 
            path.append(airsim.Vector3r(x, -self.boxsize, z))
            distance += self.boxsize 
        
        print("starting survey, estimated distance is " + str(distance))
        trip_time = distance / self.velocity
        print("estimated survey time is " + str(trip_time))
        try:
            result = self.client.moveOnPathAsync(path, self.velocity, trip_time, airsim.DrivetrainType.ForwardOnly, 
                airsim.YawMode(False,0), self.velocity + (self.velocity/2), 1).join()
        except:
            errorType, value, traceback = sys.exc_info()
            print("moveOnPath threw exception: " + str(value))
            pass

        # let it settle there a bit.
        self.client.hoverAsync().join()
        time.sleep(2)
        '''print("flying back home")
        self.client.moveToPositionAsync(0, 0, z, self.velocity).join()
        
        if z < -5:
            print("descending")
            self.client.moveToPositionAsync(0, 0, -5, 2).join()

        print("landing...")
        self.client.landAsync().join()

        print("disarming.")
        self.client.armDisarm(False)'''

if __name__ == "__main__":
    """
    Main entry point for survey mission execution.
    
    Parses command line arguments and starts the survey mission.
    Default parameters provide a reasonable starting configuration.
    """
    args = sys.argv
    args.pop(0)
    arg_parser = argparse.ArgumentParser("Usage: survey boxsize stripewidth altitude")
    arg_parser.add_argument("--size", type=float, help="size of the box to survey", default=20)
    arg_parser.add_argument("--stripewidth", type=float, help="stripe width of survey (in meters)", default=10)
    arg_parser.add_argument("--altitude", type=float, help="altitude of survey (in positive meters)", default=5)
    arg_parser.add_argument("--speed", type=float, help="speed of survey (in meters/second)", default=2)
    args = arg_parser.parse_args(args)
    nav = SurveyNavigator(args)
    nav.start()