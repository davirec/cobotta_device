from abc import ABC, abstractmethod


class Robot(ABC):

    def __init__(self, device):
        self.device = device

    @abstractmethod
    def move_robot(self, pos_i):
        pass

    @abstractmethod
    def move_robot_home(self):
        pass

    @abstractmethod
    def move_touch_center(self):
        pass

    @abstractmethod
    def touch(self, x, y, orientation=-1, event_type=2):
        """
        Touch at (x, y)
        :param x:
        :param y:
        :param orientation:
        :param event_type:
        :return:
        """

        pass

    @abstractmethod
    def swipe(self, start_xy, end_xy, duration, orientation=-1):
        """
        Sends drag event with swipe command.
        :param start_xy:
        :param end_xy:
        :param duration:
        :param orientation:
        :return:
        """
        pass

    def long_touch(self, duration=2000, orientation=-1):
        """
        Long touches at duration
        :param duration:
        :param orientation:
        :return:
        """

        pass

    def swipe_left(self):
        pass

    def swipe_right(self):
        pass

    def swipe_up(self):
        pass

    def swipe_down(self):
        pass

    def touch_button_back(self):
        pass

    def touch_button_home(self):
        pass

    def touch_button_recent_apps(self):
        pass

    def input_text(self, x, y, text):
        pass

    def vertical_swipe_zoom(self, x, y, duration=2000):
        pass

    def double_rotation(self, duration=2000):
        pass
