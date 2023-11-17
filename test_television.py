import pytest

from television import Television

class TestTelevision:
    def setup_method(self):
        self.tv = Television()

    def teardown_method(self):
        del self.tv

    def test_init(self):
        assert self.tv._str_() == 'Power = False, Channel = 0, Volume = 0'

    def test_power(self):
        self.tv.power()

        assert self.tv._str_() == 'Power = True, Channel = 0, Volume = 0'

        self.tv.power()

        assert self.tv._str_() == 'Power = False, Channel = 0, Volume = 0'

    def test_mute(self):
        pass

    def test_channel_up(self):
        assert self.tv._str_() == 'Power = False, Channel = 0, Volume = 0'

        self.tv.power()

        self.tv.channel_up()

        assert self.tv._str_() == 'Power = True, Channel = 1, Volume = 0'

        self.tv.channel_up()
        self.tv.channel_up()
        self.tv.channel_up()

        assert self.tv._str_() == 'Power = True, Channel = 0, Volume = 0'

    def test_channel_down(self):
        pass

    def test_volume_up(self):
        pass

    def test_volume_down(self):
        pass
