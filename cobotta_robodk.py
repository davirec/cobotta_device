from robodk.robolink import *  # API to communicate with RoboDK
from robot import Robot


class CobottaRobodk(Robot):
    
    def __init__(self, device, speed_robot=200):
        super().__init__(device)
        self.ref_touch_center = [-54.000000, 0.000000, 210.000000]
        self.joints_ref = [-50.000000, 25.000000, 125.000000, -55.000000, -72.000000, 25.000000]

        # Connection to the simulator
        self.RDK = Robolink()
        self.robot = self.RDK.ItemUserPick('Select a robot', ITEM_TYPE_ROBOT)
        if not self.robot.Valid():
            raise Exception('No robot selected or available')

        # current position of the TCP with respect to the reference frame
        target_ref = self.robot.Pose()

        self.robot.MoveJ(target_ref)
        self.robot.MoveJ(self.joints_ref)

        # It is important to provide the reference frame and the tool frames when generating programs offline
        self.robot.setPoseFrame(self.robot.PoseFrame())
        self.robot.setPoseTool(self.robot.PoseTool())

        # Set the rounding parameter (Also known as: CNT, APO/C_DIS, ZoneData, Blending radius, cornering, ...)
        self.robot.setRounding(10)
        self.robot.setSpeed(speed_robot)  # Set linear speed in mm/s
        
    def move_robot(self, pos_i):
        pass

    def move_robot_home(self):
        pass

    def move_touch_center(self):
        pass

    def touch(self, x, y, orientation=-1, event_type=2):
        pass

    def swipe(self, start_xy, end_xy, duration, orientation=-1):
        pass

