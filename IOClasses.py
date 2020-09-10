#------------------------------------------#
# Title: IO Classes
# Desc: A Module for IO Classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# DBiesinger, 2030-Jan-02, Extended functionality to add tracks
# Brent Kieszling, 2020-September-07, Updated get_CD_info for error handling
# Brent Kieszling, 2020-September-09, Updated FileIO
#------------------------------------------#

if __name__ == '__main__':
    raise Exception('This file is not meant to run by itself')
import DataClasses as DC
import ProcessingClasses as PC
import pickle

class FileIO:
    """Processes data to and from file:

    properties:

    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)

    """
    @staticmethod
    def save_inventory(file_name: list, lst_Inventory: list) -> None:
        """


        Args:
            file_name (list): list of file names [CD Inventory (txt), Track Inventory (txt), Data File (dat)] that hold the data.
            lst_Inventory (list): list of CD objects.

        Returns:
            None.

        """

        file_name_CD = file_name[0]
        file_name_track = file_name[1]
        file_name_data = file_name[2]
        #save formatted text file of CDs
        try:
            with open(file_name_CD, 'w') as file:
                for disc in lst_Inventory:
                    file.write(disc.get_record())
        except Exception as e:
            print('There was a general error!', e, e.__doc__, type(e), sep='\n')

        #save formatted text file of track info
        try:
            with open(file_name_track, 'w') as file:
                for disc in lst_Inventory:
                    file.write(disc.get_tracks())
        except Exception as e:
            print('There was a general error!', e, e.__doc__, type(e), sep='\n')

        #Save Binary File for easier loading
        try:
            with open(file_name_data, 'wb') as fileObj:
                pickle.dump(lst_Inventory, fileObj)
        except Exception as e:
            print('There was a general error!', e, e.__doc__, type(e), sep='\n')

    @staticmethod
    def load_inventory(file_name: list) -> list:
        """


        Args:
            file_name (list): list of file names [CD Inventory, Track Inventory, Data File (dat)] that hold the data.

        Returns:
            list: list of CD objects.

        """

        file_name_data = file_name[2]
        lst_Inventory = []
        try:
            with open(file_name_data, 'rb') as fileObj:
                lst_Inventory = pickle.load(fileObj)
        except Exception as e:
            print('There was a general error!', e, e.__doc__, type(e), sep='\n')
        return lst_Inventory

class ScreenIO:
    """Handling Input / Output"""

    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('Main Menu\n\n[l] load Inventory from file\n[a] Add CD / Album\n[d] Display Current Inventory')
        print('[c] Choose CD / Album\n[s] Save Inventory to file\n[x] exit\n')

    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, d, c, s or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'd', 'c', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, d, c, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice

    @staticmethod
    def print_CD_menu():
        """Displays a sub menu of choices for CD / Album to the user

        Args:
            None.

        Returns:
            None.
        """

        print('CD Sub Menu\n\n[a] Add track\n[d] Display cd / Album details\n[r] Remove track\n[x] exit to Main Menu')

    @staticmethod
    def menu_CD_choice():
        """Gets user input for CD sub menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case string of the users input out of the choices a, d, r or x

        """
        choice = ' '
        while choice not in ['a', 'd', 'r', 'x']:
            choice = input('Which operation would you like to perform? [a, d, r or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice


    @staticmethod
    def track_choice():
        """Gets user input for a track in a CD

        Args:
            None.

        Returns:
            choice (int): an interger string of the users input

        """
        choice = None
        while True:
            choice = input('Please enter the track number to be deleted: ')
            try:
                choice = int(choice)
                break
            except:
                print('The input provided was not an integer')
        return choice

    @staticmethod
    def show_inventory(table):
        """Displays current inventory table


        Args:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.

        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in table:
            print(row)
        print('======================================')

    @staticmethod
    def show_tracks(cd):
        """Displays the Tracks on a CD / Album

        Args:
            cd (CD): CD object.

        Returns:
            None.

        """
        print('====== Current CD / Album: ======')
        print(cd)
        print('=================================')
        print(cd.get_tracks())
        print('=================================')

    @staticmethod
    def get_CD_info():
        """function to request CD information from User to add CD to inventory


        Returns:
            cdId (string): Holds the ID of the CD dataset.
            cdTitle (string): Holds the title of the CD.
            cdArtist (string): Holds the artist of the CD.

        """

        while True:
            cdId = input('Enter ID: ').strip()
            try:
                cdId = int(cdId)
                break
            except:
                print('Please use numbers only.')
        cdTitle = input('What is the CD\'s title? ').strip()
        cdArtist = input('What is the Artist\'s name? ').strip()
        cdTracks = []
        return cdId, cdTitle, cdArtist, cdTracks

    @staticmethod
    def get_track_info():
        """function to request Track information from User to add Track to CD / Album


        Returns:
            trkId (string): Holds the ID of the Track dataset.
            trkTitle (string): Holds the title of the Track.
            trkLength (string): Holds the length (time) of the Track.

        """

        while True:
            trkId = input('Enter Position on CD / Album: ').strip()
            try:
                trkId = int(trkId)
                break
            except:
                print('Numbers only please.')
        trkTitle = input('What is the Track\'s title? ').strip()
        trkLength = input('What is the Track\'s length? ').strip()
        return trkId, trkTitle, trkLength

