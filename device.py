
class Device:

    def __init__(self):
        self.sizes = None
        self.screen_resolution = None

    def add_properties(self, screen_resolution, sizes):
        if len(screen_resolution) != 2 or len(sizes) != 3:
            raise ValueError('Error in input size. Ex. screen resolution = [1920, 1080]; sizes = [165, 76, 10].')
        self.screen_resolution = screen_resolution
        self.sizes = sizes

    def check_connectivity(self):
        pass

    def connect(self):
        pass

    def disconnect(self):
        pass

    def get_display_info(self):
        pass

    def get_height(self):
        pass

    def release_version(self):
        pass

    def sdk_version(self):
        pass

    def get_settings(self):
        pass

    def get_width(self):
        pass

    def install_app(self):
        pass

    def shutdown(self):
        pass

    def start_activity_via_monkey(self):
        pass

    def start_app(self):
        pass

    def take_screenshot(self):
        pass

    def uninstall_app(self):
        pass

    def unlock(self):
        pass

    def wait_for_device(self):
        pass

    def pull_file(self):
        pass

    def push_file(self):
        pass
