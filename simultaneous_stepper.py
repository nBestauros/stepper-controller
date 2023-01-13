from time import sleep
from multiprocessing import Process
import board
from adafruit_motor import stepper as STEPPER
from adafruit_motorkit import MotorKit

# create a default object, no changes to I2C address or frequency
kit = MotorKit(i2c=board.I2C())

class MotorMover:
    def movemotor(self, steps, direction, style):
        #print(direction)
        for i in range(steps):
            self.stepper.onestep(direction=direction, style=style)

    # Use this method to create a new thread to move a motor by steps 
    def move(self, steps, direction, style):
        if self.current_thread and self.current_thread.is_alive():
            self.current_thread.terminate()
            self.stepper.release()
        #print("declaring thread")
        self.current_thread = Process(target=self.movemotor, args=(
                steps,
                direction,
                style,
            ))
        #print("starting thread")
        self.current_thread.start()
        #print("line after start")


    def __init__(self, stepper):
        self.current_thread = None
        self.stepper = stepper
    
    # might not work properly, we should release at end of program termination too
    def __del__(self):
        self.stepper.release()




st1 = MotorMover(kit.stepper1)
st2 = MotorMover(kit.stepper2)

#print("calling move on st1")
st1.move(10000, STEPPER.FORWARD, STEPPER.DOUBLE)
sleep(2)
st1.move(5000, STEPPER.BACKWARD, STEPPER.DOUBLE)
#print("right after move on st1")
#print("calling move on st2")
st2.move(600, STEPPER.BACKWARD, STEPPER.DOUBLE)
#print("right after move on st2")
st1.stepper.release()
st2.stepper.release()

exit()