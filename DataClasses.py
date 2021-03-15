#--------------------------
# Title: Data Classes
# Description: Creates CD object
# Change Log: 03-11-21, created
# Created By: Eric Hoyle
#--------------------------  
if __name__ == '__main__':
    raise Exception('This file is not meant to ran by itself')

class Track:
    """Stores Data about a single track:
     
        properties:
        position: (int) with Track position on CD / Album
        title: (str) with Track title
        length: (str) with length / playtime of Track
    methods:
        get_record() -> (str)

    """
    # TODO add Track class code
    # -- Constructor -- #
    def __init__(self, position, title, length):
        try:
            self.__track_position = int(position)
            self.__track_title = str(title)
            self.__track_length = str(length)
        except Exception as e:
            raise Exception('Error setting intial track values \n'+str(e))
            
    # -- Properties -- #
    @property 
    def track_position(self):
        return self.__track_position
    
    @track_position.setter
    def track_position(self, value):
        try:
            self.__track_position = int(value)
        except Exception:
            raise Exception('Track position must be an integer')
            
    @property 
    def track_title(self):
        return self.__track_title
    
    @track_title.setter 
    def track_title(self, title):
        try:
            self.__track_title = str(title)
        except Exception:
            raise Exception('Title  must be entered as a string')
            
    @property 
    def track_length(self):
        return self.__track_length
    
    @track_length.setter 
    def track_length(self, length):
        try:
            self.__track_length = str(length)
        except Exception:
            raise Exception('Track length must be enetered as a string')
            

    # -- Methods -- #
    # TODO Add Track class methods
    def __str__(self):
        """Returns Track details as formatted string"""
        return '{:>2}{:30}{:30}'.format(self.track_position, self.track_title, self.track_length).title()

    def get_record(self) -> str:
        """Returns: Track record formatted for saving to file"""
        return '{},{},{}\n'.format(self.track_position, self.track_title, self.track_length).title()
    
    def track_listing(self):
        """Returns: Track record formatted for saving to file"""
        return '{:<10}{:^30}{:^30}\n'.format(self.track_position, self.track_title, self.track_length).title()
            
    
    
    
class CD:
    """Stores data about a CD:

    properties:
        cd_index: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
        cd_tracks:(list) with track objects of the CD / Album
    methods:
        __str__(): formatted string of cd attributes for presentation of inventory  
        __file_export(): formatted string of cd attributes for exporting to .txt files
        
    """  
    #Constructor
    def __init__(self, index, title, artist):
        try:
            self.__cd_index = int(index)
            self.__cd_title = str(title)
            self.__cd_artist = str(artist)
            self.__cd_tracks = []
        except Exception as e:
            raise Exception ('Error setting initial CD values\n'+str(e))
    #Poperties
    @property
    def cd_index(self):
        return self.__cd_index
    
    @cd_index.setter
    def cd_index(self,value):
        try:
            self.__cd_index =int(value)
        except Exception:
            raise Exception('Index must be an integer')        
    
    @property 
    def cd_title(self):
        return self.__cd_title
    
    @cd_title.setter
    def cd_title(self, title):
        try:
            self.__cd_title = str(title)
        except Exception:
            raise Exception('Title must be entered as string')
   
    @property 
    def cd_artist(self):
        return self.__cd_artist
    
    @cd_artist.setter
    def cd_artist(self, artist):
        try:
            self.__cd_artist = str(artist)
        except Exception:
            raise Exception('Title must be entered as string')
            
    @property 
    def cd_tracks(self):
        return self.__cd_tracks
    #Methods
    def __str__(self):
        return '{:<10}{:^30}{:^30}'.format(self.cd_index, self.cd_title, self.cd_artist).title()
    
    def file_export(self):
        return '{},{},{}\n'.format(self.cd_index,self.cd_title,self.cd_artist).title()
    
    def add_track(self,track):
        """Adds a track to the CD / Album


        Args:
            track (Track): Track object to be added to CD / Album.

        Returns:
            None.

        """
        self.__cd_tracks.append(track)
        self.__sort_tracks()
        
    def rmv_track(self,track_id):
        """Removes the track identified by track_id from Album
    
    
            Args:
                track_id (int): ID of track to be removed.
    
            Returns:
                None.
        """   
        try:
            del self.__cd_tracks[track_id -1]
        except IndexError as e: print(e.__doc__)
        self.__sort_tracks()
        
    def __sort_tracks(self):
        
        """Sorts the tracks using Track.position. Fills blanks with None"""
        n = len(self.__cd_tracks)
        for track in self.__cd_tracks:
            if (track is not None) and (n < track.track_position):
                n = track.track_position
        tmp_tracks = [None] * n
        for track in self.__cd_tracks:
            if track is not None:
                tmp_tracks[track.track_position - 1] = track
        self.__cd_tracks = tmp_tracks
        
    def get_tracks(self):
        """Returns a string list of the tracks saved for the Album

        Raises:
            Exception: If no tracks are saved with album.

        Returns:
            result (string):formatted string of tracks.

        """
        self.__sort_tracks()
        if len(self.__cd_tracks) < 1:
            raise Exception('No tracks saved for this Album')
        result = ''
        for track in self.__cd_tracks:
            if track is None:
                result += 'No Information for this track\n'
            else:
                # result = str(track) + '\n'
                result += track.track_listing()
        return result
    
    def get_long_record(self):
        """gets a formatted long record of the Album: Album information plus track details


        Returns:
            result (string): Formatted information about ablum and its tracks.

        """
        result = self.file_export() + '\n'
        result += self.get_tracks() + '\n'
        return result

#-------DATA-------#
    

#-------PROCESSING--------#
    

#--------PRESENTATION (I/O)-----------#