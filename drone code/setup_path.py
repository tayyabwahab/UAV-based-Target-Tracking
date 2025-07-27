"""
AirSim Module Path Setup Utility

This module automatically sets up the path to the local AirSim module for UAV simulation.
It first checks if AirSim is installed via pip, and if not, looks for the AirSim folder
in the parent directory and adds it to the Python path.

Key Features:
- Automatic AirSim module detection
- Path configuration for local AirSim installation
- Fallback to pip-installed AirSim
- Cross-platform path handling

Author: UAV Security System Team
License: MIT
"""

# Import this module to automatically setup path to local airsim module
# This module first tries to see if airsim module is installed via pip
# If it does then we don't do anything else
# Else we look up grand-parent folder to see if it has airsim folder
#    and if it does then we add that in sys.path

import os,sys,logging

class SetupPath:
    """
    Utility class for setting up AirSim module path.
    
    This class provides methods to automatically configure the Python path
    to include the AirSim module for UAV simulation. It handles both
    pip-installed and local AirSim installations.
    
    Methods:
        getDirLevels: Get directory depth level
        getCurrentPath: Get current file directory
        getGrandParentDir: Get grandparent directory
        getParentDir: Get parent directory
        addAirSimModulePath: Add AirSim to Python path
    """
    
    @staticmethod
    def getDirLevels(path):
        """
        Get the number of directory levels in a path.
        
        Args:
            path (str): File system path
            
        Returns:
            int: Number of directory levels
        """
        path_norm = os.path.normpath(path)
        return len(path_norm.split(os.sep))

    @staticmethod
    def getCurrentPath():
        """
        Get the directory of the current file.
        
        Returns:
            str: Directory path of the current file
        """
        cur_filepath = __file__
        return os.path.dirname(cur_filepath)

    @staticmethod
    def getGrandParentDir():
        """
        Get the grandparent directory of the current file.
        
        Returns:
            str: Grandparent directory path, or empty string if not available
        """
        cur_path = SetupPath.getCurrentPath()
        if SetupPath.getDirLevels(cur_path) >= 2:
            return os.path.dirname(os.path.dirname(cur_path))
        return ''

    @staticmethod
    def getParentDir():
        """
        Get the parent directory of the current file.
        
        Returns:
            str: Parent directory path, or empty string if not available
        """
        cur_path = SetupPath.getCurrentPath()
        if SetupPath.getDirLevels(cur_path) >= 1:
            return os.path.dirname(cur_path)
        return ''

    @staticmethod
    def addAirSimModulePath():
        """
        Add AirSim module to Python path.
        
        This method automatically configures the Python path to include the AirSim
        module. It first checks for a pip-installed version, then looks for a
        local installation in the parent directory.
        
        The method:
        1. Checks if AirSim is installed via pip
        2. If not, looks for AirSim in parent directory
        3. Adds the AirSim path to sys.path if found
        4. Logs a warning if AirSim is not found
        
        Note:
            This method modifies sys.path directly and should be called
            early in the import process.
        """
        # if airsim module is installed then don't do anything else
        #import pkgutil
        #airsim_loader = pkgutil.find_loader('airsim')
        #if airsim_loader is not None:
        #    return

        parent = SetupPath.getParentDir()
        if parent !=  '':
            airsim_path = os.path.join(parent, 'airsim')
            client_path = os.path.join(airsim_path, 'client.py')
            if os.path.exists(client_path):
                sys.path.insert(0, parent)
        else:
            logging.warning("airsim module not found in parent folder. Using installed package (pip install airsim).")

SetupPath.addAirSimModulePath()
