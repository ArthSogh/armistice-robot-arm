from pyPS4Controller.controller import Controller
from adafruit_servokit import ServoKit
from time import sleep

kit = ServoKit(channels=16)
servo = 14


class MyController(Controller):
    value_indice_motor = 0
    value_up_down = 0
    value_l3_vertical = 0
    value_l3_horizontal = 0

    value_moto_0 = 0
    list_of_angles = [0, 0, 0, 0]

    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)

    def on_x_press(self):
        print("Hello world")

    def on_x_release(self):
        print("GO to 90")
        ServoMove(self.value_indice_motor, 90)

    def on_circle_release(self):
        print("GO to 0")
        ServoMove(self.value_indice_motor, 0)

    def on_L1_press(self):
        self.value_indice_motor -= 1
        print("L1", self.value_indice_motor)

    def on_R1_press(self):
        self.value_indice_motor += 1
        print("R1", self.value_indice_motor)



    def on_R2_release(self):
        self.value_moto_0 += 5
        print("BASEMENT", self.value_moto_0)
        ServoMove(self.value_indice_motor, self.value_moto_0)

    def on_up_arrow_press(self):
        self.list_of_angles[self.value_indice_motor] += 5
        print("Up", self.value_up_down)
        print("Test", self.list_of_angles[self.value_indice_motor])
        # ServoMove(self.value_indice_motor, self.list_of_angles[self.value_indice_motor])

    def on_down_arrow_press(self):
        self.list_of_angles[self.value_indice_motor] -= 5
        print("Down", self.value_up_down)
        print("Test", self.list_of_angles[self.value_indice_motor])
        # ServoMove(self.value_indice_motor, self.list_of_angles[self.value_indice_motor])

    def on_L3_up(self, value):
        # print("Up",-value/32767)
        self.value_l3_vertical += -value / 32767
        ServoMove(self.value_indice_motor, round(self.value_l3_vertical))
        print("Up", round(self.value_l3_vertical))

    def on_L3_down(self, value):
        # print("Down",-value/32767)
        self.value_l3_vertical += -value / 32767
        ServoMove(self.value_indice_motor, round(self.value_l3_vertical))
        print("Down", round(self.value_l3_vertical))

    def on_L3_left(self, value):
        self.value_l3_horizontal += value / 32767
        # ServoMove(self.value_l1_r1,round(self.value_l3_horizontal))
        print("Left", round(self.value_l3_horizontal))

    def on_L3_right(self, value):
        self.value_l3_horizontal += value / 32767
        # ServoMove(self.value_l1_r1,round(self.value_l3_horizontal))
        print("Right", round(self.value_l3_horizontal))


def ServoMove(numero, angl):
    print("fonction")
    kit.servo[numero].angle = int(angl)


controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)

controller.listen(timeout=60)


