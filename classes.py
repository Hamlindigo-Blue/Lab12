class Television:
    '''
    A class to representing a television object
    '''

    MIN_CHANNEL = 0     # Minimum TV channel
    MAX_CHANNEL = 3     # Maximum TV channel
    MIN_VOLUME = 0      # Minimum TV volume
    MAX_VOLUME = 2      # Maximum TV volume

    def __init__(self) -> None:
        '''
        Method to set the object state of the TV.
        '''

        self.__channel: int = Television.MIN_CHANNEL
        self.__volume: int = Television.MIN_VOLUME
        self.__status: bool = False

    def power(self) -> None:
        '''
        Method to turn the TV on/off.
        '''

        if self.__status:
            self.__status = False
        else:
            self.__status = True

    def channel_up(self) -> None:
        '''
        Method to change channel by one increment.
        '''

        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        '''
        Method to change channel by one decrement.
        '''

        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel-= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        '''
        Method to increment the volume by one.
        '''

        if self.__status:
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        '''
        Method to decrement the volume by one.
        '''

        if self.__status:
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        '''
        Method to acess a tv's power status, channel, and volume.
        :return: TV's power status, channel, and volume.
        '''

        return f'TV status: Is on = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
