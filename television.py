class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        self._status = False
        self._muted = False
        self._volume = Television.MIN_VOLUME 
        self._channel = Television.MIN_CHANNEL 

    def power(self):
        """Turns the TV on or off."""
        self._status = not self._status

    def mute(self):
        """Mutes or unmutes the TV."""
        if self._status:
            self._muted = not self._muted

    def channel_up(self):
        """Increases the TV channel value."""
        if self._status and not self._muted:
            self._channel = (self._channel + 1) % (Television.MAX_CHANNEL + 1)

    def channel_down(self):
        """Decreases the TV channel value."""
        if self._status and not self._muted:
            self._channel = (self._channel - 1) % (Television.MAX_CHANNEL + 1)

    def get_volume(self):
        """Returns the TV's current volume."""
        return self._volume

    def set_volume(self, volume):
        """Sets the TV's volume to the specified value."""
        if self._status and not self._muted and Television.MIN_VOLUME <= volume <= Television.MAX_VOLUME:
            self._volume = volume

    def volume_up(self):
        """Increases the TV volume by one unit."""
        if self._status and not self._muted and self._volume < Television.MAX_VOLUME:
            self._volume += 1

    def volume_down(self):
        """Decreases the TV volume by one unit."""
        if self._status and not self._muted and self._volume > Television.MIN_VOLUME:
            self._volume -= 1

    def get_channel(self):
        """Returns the TV's current channel."""
        return self._channel

    def set_channel(self, channel):
        """Sets the TV's channel to the specified value."""
        if self._status and not self._muted and Television.MIN_CHANNEL <= channel <= Television.MAX_CHANNEL:
            self._channel = channel

    def __str__(self):
        """Returns a string representation of the TV."""
        if self._status:
            return "Power = True, channel = {}, volume = {}.".format(self._channel, self._volume)
        else:
            return "Power = False, channel = {}, volume = {}.".format(self._channel, self._volume)
        

