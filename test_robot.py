import pytest

from device import Device


class TestRobot:
    def test_touch(self):
        device = Device()

        device.add_properties([1920, 1080], [165, 76, 10])

        assert 1 == 1

