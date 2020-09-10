#------------------------------------------#
# Title: Data Classes
# Desc: A Module for Data Classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# DBiesinger, 2030-Jan-02, Modified to add Track class, added methods to CD class to handle tracks
# Brent Kieszling, 2020-September-07, Updated class Track, Updated class CD with track attribute
# Brent Kieszling, 2020-September-08, Updated class CD add_track
# Brent Kieszling, 2020-September-09, Updated class CD rmv_track
#------------------------------------------#

if __name__ == '__main__':
    raise Exception('This file is not meant to run by itself')

class Track():
    """Stores Data about a single Track:

    properties:
        position: (int) with Track position on CD / Album
        title: (str) with Track title
        length: (str) with length / playtime of Track
    methods:
        get_record() -> (str) describing track properties

    """
    # -- Constructor -- #
    def __init__(self, cdposition, cdtitle, cdlength):
        # -- Attributes -- #
        self.__position = cdposition
        self.__title = cdtitle
        self.__length = cdlength

    # -- Properties -- #
    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if str(value).isnumeric() == False:
            raise Exception('Integers only')
        else:
            self.__position = int(value)

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        if value.isstring():
            self.__title = value
        else:
            raise Exception('Not a valid input')

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, value):
        if value.isstring():
            self.__length = value
        else:
            raise Exception('Not a valid input')

    # -- Methods -- #
    def __str__(self):
        """Returns Track details as formatted string"""

        return self.get_record()

    def get_record(self) -> str:
        """Returns: Track record formatted for saving to file"""

        return '{:>2}\t{}\t{}'.format(self.position, self.title, self.length)


class CD:
    """Stores data about a CD / Album:

    properties:
        cd_id: (int) with CD  / Album ID
        cd_title: (string) with the title of the CD / Album
        cd_artist: (string) with the artist of the CD / Album
        cd_tracks: (list) with track objects of the CD / Album
    methods:
        get_record() -> (str)
        add_track(track) -> None
        rmv_track(int) -> None
        get_tracks() -> (str)
        get_long_record() -> (str)
        __sort_tracks() -> None

    """

    # -- Constructor -- #
    def __init__(self, cd_id: int, cd_title: str, cd_artist: str, cd_tracks: list) -> None:
        """Set ID, Title and Artist of a new CD Object"""
        #    -- Attributes  -- #
        try:
            self.__cd_id = int(cd_id)
            self.__cd_title = str(cd_title)
            self.__cd_artist = str(cd_artist)
            self.__tracks = cd_tracks
        except Exception as e:
            raise Exception('Error setting initial values:\n' + str(e))

    # -- Properties -- #
    # CD ID
    @property
    def cd_id(self):
        return self.__cd_id

    @cd_id.setter
    def cd_id(self, value):
        try:
            self.__cd_id = int(value)
        except Exception:
            raise Exception('ID needs to be Integer')

    # CD title
    @property
    def cd_title(self):
        return self.__cd_title

    @cd_title.setter
    def cd_title(self, value):
        try:
            self.__cd_title = str(value)
        except Exception:
            raise Exception('Title needs to be String!')

    # CD artist
    @property
    def cd_artist(self):
        return self.__cd_artist

    @cd_artist.setter
    def cd_artist(self, value):
        try:
            self.__cd_artist = str(value)
        except Exception:
            raise Exception('Artist needs to be String!')

    # CD tracks
    @property
    def cd_tracks(self):
        return self.__tracks

    @cd_tracks.setter
    def cd_tracks(self, value):
        if type(value) != list:
            raise Exception ('List expected')

    # -- Methods -- #
    def __str__(self):
        """Returns: CD details as formatted string"""
        return '{:>2}\t{} (by: {})'.format(self.cd_id, self.cd_title, self.cd_artist)

    def get_record(self):
        """Returns: CD record formatted for saving to file"""
        return '{},{},{}\n'.format(self.cd_id, self.cd_title, self.cd_artist)

    def add_track(self, track: Track) -> None:
        """Adds a track to the CD / Album


        Args:
            track (Track): Track object to be added to CD / Album.

        Returns:
            None.

        """
        # append track
        self.cd_tracks.append(track)

        # sort tracks
        self.__sort_tracks()

    def rmv_track(self, track_id: int) -> None:
        """Removes the track identified by track_id from Album


        Args:
            track_id (int): ID of track to be removed.

        Returns:
            None.

        """

        try:
            del self.cd_tracks[(track_id-1)]
        except:
            print('Track ID not recognized')
        # sort tracks
        self.__sort_tracks()

    def __sort_tracks(self):
        """Sorts the tracks using Track.position. Fills blanks with None"""
        n = len(self.__tracks)
        for track in self.__tracks:
            if (track is not None) and (n < track.position):
                n = track.position
        tmp_tracks = [None] * n
        for track in self.__tracks:
            if track is not None:
                tmp_tracks[track.position - 1] = track
        self.__tracks = tmp_tracks

    def get_tracks(self) -> str:
        """Returns a string list of the tracks saved for the Album

        Raises:
            Exception: If no tracks are saved with album.

        Returns:
            result (string):formatted string of tracks.

        """

        self.__sort_tracks()
        if len(self.__tracks) < 1:
            raise Exception('No tracks saved for this Album')
        result = ''
        for track in self.__tracks:
            if track is None:
                result += 'No Information for this track\n'
            else:
                result += str(track) + '\n'
        return result

    def get_long_record(self) -> str:
        """gets a formatted long record of the Album: Album information plus track details


        Returns:
            result (string): Formatted information about ablum and its tracks.

        """

        result = self.get_record() + '\n'
        result += self.get_tracks() + '\n'
        return result




