#------------------------------------------#
# Title: CD_Inventory.py
# Desc: The CD Inventory App main Module
# DBiesinger, 2030-Jan-01, Created File
# DBiesinger, 2030-Jan-02, Extended functionality to add tracks
# Change Log: 03-11-21 - Built modules and tested
#             03-12-21 - Built out main, added sub menu functionality
#             03-14-21 - Debugged file import
#             03-14-21 - Added track removal feature 
#------------------------------------------#

import ProcessingClasses as PC
import IOClasses as IO


lstFileNames = ['AlbumInventory.txt', 'TrackInventory.txt']
lstOfCDObjects = IO.FileIO.read_file(lstFileNames)

while True:
    IO.ScreenIO.print_main_menu()
    strChoice = IO.ScreenIO.menu_choice()

    if strChoice == 'x':
        break
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled: ')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            lstOfCDObjects = IO.FileIO.read_file(lstFileNames)
            IO.ScreenIO.show_CD_inventory(lstOfCDObjects)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.ScreenIO.show_CD_inventory(lstOfCDObjects)
        continue  
    elif strChoice == 'a':
        tplCdInfo = IO.ScreenIO.get_cd_info()
        PC.DataProcessor.add_CD(tplCdInfo, lstOfCDObjects)
        IO.ScreenIO.show_CD_inventory(lstOfCDObjects)
        continue  
    elif strChoice == 'd':
        IO.ScreenIO.show_CD_inventory(lstOfCDObjects)
        continue  
    elif strChoice == 'c':
        while True:
            IO.ScreenIO.show_CD_inventory(lstOfCDObjects)
            cd_idx = input('Select the CD you would like to choose, or press Enter to return to the CD Menu: ')
            cd = PC.DataProcessor.select_cd(lstOfCDObjects, cd_idx)
            if cd_idx == '': break
            if cd == None: continue
            IO.ScreenIO.cd_display(cd)
            IO.ScreenIO.print_CD_menu()
            subChoice = IO.ScreenIO.menu_CD_choice()
            if subChoice == 'x':
                break
            elif subChoice == 'a':
                track_info = IO.ScreenIO.get_track_info()
                PC.DataProcessor.add_track(track_info, cd)
                continue
            elif subChoice == 'd':
                IO.ScreenIO.show_tracks(cd)
            elif subChoice == 'r':
                IO.ScreenIO.show_tracks(cd)
                track_id = IO.ScreenIO.track_select()
                cd.rmv_track(track_id)
                continue
    elif strChoice == 's':
        IO.ScreenIO.show_CD_inventory(lstOfCDObjects)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        if strYesNo == 'y':
            IO.FileIO.write_file(lstFileNames, lstOfCDObjects)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue
    else:
        print('General Error')