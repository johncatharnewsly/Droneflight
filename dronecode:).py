from djitellopy import tello
from time import sleep
tell0 = tello.Tello()
tell0.connect()
tell0.takeoff()
tell0.move_up(103.333543)
tell0.move_forward(456)
sleep(.5)
tell0.rotate_clockwise(90)
tell0.move_forward(190)
sleep(.5)
tell0.rotate_clockwise(90)
tell0.move_forward(44)
sleep(.5)
tell0.rotate_clockwise(180)
tell0.move_forward(500)
sleep(.5)
tell0.rotate_counter_clockwise(90)
tell0.move_forward(190)
sleep(.5)
tell0.move_down(103.333543)
tell0.land()
