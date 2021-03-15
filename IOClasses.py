#--------------------------
# Title: IO Classes
# Description:
# Change Log: 
# Created By:Eric Hoyle
# Description:
#--------------------------  
if __name__ == '__main__':
    raise Exception('This file is not meant to ran by itself')

import DataClasses as DC
import ProcessingClasses as PC
    
class FileIO:
    """Processing the data to and from text file"""

    @staticmethod
    def read_file(file_name:list)->list:
        """Function to manage data ingestion from file to a list of 
        CD Objects. Reads the data from file identified by file_name into a listt of objects
        one line in the file is converted to a CD object and appended to the list. 
        

        Args:
            file_name(list): list of file name [CD Inventory, Track Inventory] that
            hold the data
            lst_Inventory (list): list of CD objects that holds data during runtime
            
        Returns:
            list: list of CD objects.
        """
        
        file_name_CD = file_name[0]
        file_name_track = file_name[1]
        lst_Inventory = []
        try:     
            with open(file_name_CD, 'r') as cdFile:
                for line in cdFile:
                    data = line.strip().split(',')
                    row = DC.CD(data[0],data[1],data[2])
                    lst_Inventory.append(row)
                    print('list inventory', lst_Inventory)
            with open(file_name_track, 'r') as trkFile:
                for line in trkFile:
                    trkdata = line.strip().split(',')
                    cd = PC.DataProcessor.select_cd(lst_Inventory, int(trkdata[0]))
                    track = DC.Track(int(trkdata[1]),trkdata[2],trkdata[3])
                    cd.add_track(track)
        except FileNotFoundError as e:
            print('\n{:*^66}'.format((e.__doc__).upper()),
                  '\n{:^66}'.format(' WARNING: Data not loaded').upper()) 
         
        return lst_Inventory

    @staticmethod
    def write_file(file_name, lst_Inventory):
        """Function to manage data output from a list of objects to a file 

        Writes the data from a 2D table (lstofCDObjects) to a file identified by 
        file_name, as string data one cd at a time.
        
        Args:
            Args:
                file_name(list): list of file name [CD Inventory, Track Inventory] that hold the data
                lst_Inventory (list): list of CD objects that holds data during runtime

        Returns:
            None.
        """
       
        file_name_CD  = file_name[0]
        file_name_track = file_name [1]
        try:
            with open(file_name_CD, 'w') as cdFile:
                for cd in lst_Inventory:
                    cdFile.write(cd.file_export())
            with open(file_name_track, 'w') as trkFile:
                for cd in lst_Inventory:
                    tracks = cd.cd_tracks
                    cdID = cd.cd_index
                    for trk in tracks:
                        if trk is not None:
                            record = '{},{}'.format(cdID, trk.get_record())
                            trkFile.write(record)
        except FileNotFoundError as e:
            print('\n{:*^66}'.format((e.__doc__).upper()),
                  '\n{:^66}'.format(' WARNING: Data not saved').upper())

    
    
class ScreenIO:
    """Handling Input / Output"""
    @staticmethod
    def print_main_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('\n\n')
        print('{:-^66}'.format(' Main Menu '),
             '\n{:<}'.format('[l] Load Inventory'),
             '\n{:<30}'.format('[a] Add CD'),
             '\n{:<30}'.format('[d] Display Current Inventory'),
             '\n{:<30}'.format('[c] Choose CD'),
             '\n{:<}'.format('[s] Save Inventory to'),
             '\n{:<30}'.format('[x] Exit'),
             '\n{:-^66}'.format('-'))   
 
    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, d, s or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'd', 'c', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, d, c, s, or x]: ').lower().strip()
        print()  
        return choice

    @staticmethod 
    def print_CD_menu():
        """Displays a sub menu of choices for CD / Album to the user

        Args:
            None.

        Returns:
            None.
        """
        print('{:-^66}'.format(' CD Menu '),
            '\n{:<}'.format('[a] Add Track'),
            '\n{:<30}'.format('[d] Display CD Details'),
            '\n{:<30}'.format('[r] Remove Track'),
            '\n{:<30}'.format('[x] Exit to Main Menu'),
            '\n{:-^66}'.format('-'))  
    
    @staticmethod
    def menu_CD_choice():
        """Gets user input for CD sub menu selection

         Args:
            None.

         Returns:
            choice (string): a lower case sting of the users input out of the choices a, d, r or x

        """
        choice = ' '
        while choice not in ['a', 'd', 'r', 'x']:
            choice = input('Which operation would you like to perform? [a, d, r or x]: ').lower().strip()
        print()
        return choice
    
    @staticmethod
    def show_CD_inventory(table):
        """Displays current inventory table


        Args:
            table (list of CD Objects): 2D data structure that holds the data during runtime.

        Returns:
            None.

        """
        print('\n\n')
        print('{:=^66}'.format(' The Current Inventory '))
        print('{:<10}{:^30}{:^30}'.format('ID','Title','Artist'))
        print('{:-^66}'.format('-'))
        for cd in table:
            print(cd)
        print('{:=^66}'.format('='))
    
    @staticmethod 
    def show_tracks(cd):
        """Displays the tracks on a CD
        
            Args:
                cd (CD): CD object
            
            Returns:
                None
        """
        try:
            print('\n\n')
            print('{:=^66}'.format(' Current CD '))
            print('{:<10}{:^30}{:^30}'.format('CD ID', 'Title','Artist'))
            print('{:-^66}'.format('-'))
            print(cd)
            print('{:-^66}'.format('-'))
            print()
            print('{:=^66}'.format(' Track Listing '))
            print('{:<10}{:^30}{:^30}'.format('Track ID', 'Track Title','Time'))
            print('{:-^66}'.format('-'))
            print(cd.get_tracks())
        except: print('No tracks for this CD')
        
    @staticmethod
    def get_cd_info():
        """Ask user for new ID, CD Title and Artist
        
        Args: 
            None.
        
        Raises:
            Exception ValueError if index is not an integer.
        
        Returns:
            list of information (ID, Title, and Artist) for a new CD entry"""
        
        index = ''
        n=2
        while index == '':
            try:
                index = int(input('Enter ID: ').strip())
            except ValueError:
                print('\n* Don\'t be a dummy! ID must be a number. Please try again *\n'.upper())
                n-=1
                if n==0:
                    input('You seem to be pretty dense. Let\'s get you back to the main menu.')
                    break
                continue
            strTitle = input('What is the CD\'s title? ').strip()
            strArtist = input('What is the Artist\'s name? ').strip()
            cdData =[index, strTitle, strArtist]
            return cdData
    
    @staticmethod 
    def get_track_info():
        """Ask user for new track information
        
        Args: 
            None.
            
        Raises: 
            Exception ValueError if track position is not an integer.
            
        Returns:
            track_info (tuple): tuple containing trak position, track title, and track length.
           
            """
        
        index = ''
        n=2
        while index == '':
            try:
                trkPos = int(input('Enter track number: ').strip())
            except ValueError:
                print('\n* Don\'t be a dummy! Track number must be a number. Please try again *\n'.upper())
                n-=1
                if n==0:
                    input('You seem to be pretty dense. Let\'s get you back to the main menu.')
                    break
                continue
            trkTitle = input('What is the track\'s title? ').strip()
            trkLength = input('What is the track\'s time? ').strip()
            trkInfo =(trkPos, trkTitle, trkLength)
            return trkInfo
        
    @staticmethod 
    def cd_display(cd):
        print('\n\n')
        print('{:=^66}'.format(' Current CD '))
        print('{:<10}{:^30}{:^30}'.format('CD ID', 'Title','Artist'))
        print('{:-^66}'.format('-'))
        print(cd)
        print('{:-^66}'.format('-'))
        
    @staticmethod
    def track_select():
        """Selects the track to be removed from the track inventory

        Args:
            None
        Returns:
            Track ID  
        """
        track_ID = ""
        try:
            track_ID = input('Which track would you like to remove?: ')
            track_ID = int(track_ID)
        except ValueError:
            print('ID must be a number')
        return track_ID
            