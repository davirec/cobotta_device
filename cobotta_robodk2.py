from robodk.robolink import *  # API to communicate with RoboDK
import time

class Cobotta:
    def __init__(self):
        # Definição dos parâmetros do smartphone e dos pontos de referência
        self.resolution = [1920, 1080]
        self.smartphone_dimensions = [165, 76, 10]
        self.touch_center_ref = [-54.0, 0.0, 210.0]

        # Configuração dos deslocamentos e dimensões do smartphone
        self.gap = 15
        self.scroll_border = 10
        self.touch_border = 5
        self.distance_screen = 10
        self.scroll_margin = 40

        # Conexão com o simulador e configuração do robô
        self.RDK = Robolink()
        self.robot = self.RDK.ItemUserPick('Select a robot', ITEM_TYPE_ROBOT)
        if not self.robot.Valid():
            raise Exception('No robot selected or available')

        self.robot.MoveJ([-50, 25, 125, -55, -72, 25])  # Movimento para a posição inicial
        self.robot.setPoseFrame(self.robot.PoseFrame())
        self.robot.setPoseTool(self.robot.PoseTool())
        self.robot.setRounding(10)
        self.robot.setSpeed(200)

    # def move_robot(self, position):
    #     pose = self.robot.Pose()
    #     pose.setPos(position)
    #     self.robot.MoveL(pose)
    #     self.robot.WaitMove()
    #     time.sleep(1)

    def move_robot(self, pos_i):
        target_i = self.robot.Pose()
        target_i.setPos(pos_i)
        try:
            print(target_i)
            self.robot.MoveL(target_i)
        except TargetReachError as erro:
            print("\033[1;31m", erro, "\033[0;0m")
            self.move_robot([-64.000000, 0.000000, 210.000000])
            print("\033[1;31m", target_i, "\033[0;0m")
            # self.robot.MoveL(target_i)
        time.sleep(1)

    def touch(self, x, y):
        print('\033[41m' + f"Touch {x}, {y}" + '\033[0m')
        x = max(0, min(x, self.smartphone_dimensions[1]))
        y = max(0, min(y, self.smartphone_dimensions[0]))

        x_offset = self.touch_border if x > self.smartphone_dimensions[1] / 2 else -self.touch_border
        touch_point = [self.touch_center_ref[0] - self.distance_screen,
                       self.touch_center_ref[1] + x_offset - x,
                       self.touch_center_ref[2] + y]

        self.move_robot(touch_point)

    def scroll(self, direction):
        scroll_border = self.touch_center_ref[1] + self.smartphone_dimensions[1] / 2 - self.scroll_border if direction == 'left' else self.touch_center_ref[1] - self.smartphone_dimensions[1] / 2 + self.scroll_border
        scroll_start = [self.touch_center_ref[0] - self.distance_screen, scroll_border, self.touch_center_ref[2]]
        scroll_end = [self.touch_center_ref[0] - self.distance_screen, scroll_border, self.touch_center_ref[2] - self.scroll_margin] if direction == 'up' else [self.touch_center_ref[0] - self.distance_screen, scroll_border, self.touch_center_ref[2] + self.scroll_margin]

        self.move_robot(scroll_start)
        self.move_robot(scroll_end)

    def double_rotation(self, orientation_code):
        print('\033[41m' + f"Double rotation {orientation_code}" + '\033[0m')
        self.robot.MoveJ([-50, 25, 125, -55, -72, 25])  # Movimento para a posição inicial
        if orientation_code == 1:
            self.robot.MoveJ([-50, 25, 125, -55, -72, -65])
        else:
            self.robot.MoveJ([-50, 25, 125, -55, -72, 25])
            time.sleep(1)
            self.move_robot([-64, 0, 210])

    def move_touch_home(self):
        self.robot.MoveJ([-50, 25, 125, -55, -72, 25])  # Movimento para a posição inicial


if __name__ == '__main__':
    robot_cobotta = Cobotta()
    robot_cobotta.touch(0, 165)
    robot_cobotta.double_rotation(0)
    time.sleep(1)
    robot_cobotta.double_rotation(1)
    time.sleep(1)
    robot_cobotta.double_rotation(0)
    time.sleep(1)
    robot_cobotta.scroll('down')
    robot_cobotta.scroll('up')
    robot_cobotta.move_touch_home()
