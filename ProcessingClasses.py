#--------------------------
# Title: ProcessingClasses
# Description: Processes Data
# Change Log:  03-11-21, created
# Created By:Eric Hoyle
#--------------------------  

if __name__ == '__main__':
    raise Exception('This file is not meant to ran by itself')

import DataClasses as DC

class DataProcessor:
    """Processing data supplied by the user"""
   
    @staticmethod   
    def add_CD(cdInfo, table):
        """Appends new cd entry as to lstofCDObjects table
        
        Args: 
            cdData(tuple): Information aboout the CD 
            table (list of objects): 2D data structure (list of CD Objects) that holds the data during runtime.
        
        Returns: 
            None
        
        """
        index, title, artist = cdInfo
        index = int(index)
        cd=DC.CD(index, title, artist)
        table.append(cd)
        
    def select_cd(table, cd_idx):
        """Selects CD Object from the table specified that conatins the cd_index cd_idx
        
        Args:
            table (list): Inventory list of CD objects
            cd_idx (int): id of CD object to return.
            
        Raises:
                Exception: If cd_idx is not in list.
            
        Returns:
            Row (DC.CD): CD object that matched cd_idx
        """
        try:
            cd_idx = int(cd_idx)
        except ValueError:
            print('{:*^30}'.format('ID must be an integer, please try again'))         
        for row in table:
            if row.cd_index == cd_idx:
                return row
            
    
    
        
    def add_track(track_info, cd):
        """Adds a track object with attributes in track info to CD
        
        Args:
            track_info (tuple): Tuple containing track infor (position, title, length)
            cd (DC.CD): cd object the track gets added to.
            
        Raises:
            Exception: DESCraised in case position is not an integer.
            
        Returns:
            None: DESCRIPTION
        """
        trkPos, trkTitle, trkLength = track_info
        try:
            trkPos = int(trkPos)
        except:
            raise Exception('Position must be an integer')
        track = DC.Track(trkPos, trkTitle, trkLength)
        cd.add_track(track)
        
        
    
        
        
        