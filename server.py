from flask import Flask, render_template, request
from simultaneous_stepper import MotorMover
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper as STEPPER
import board
import json
app = Flask(__name__)

kit = MotorKit(i2c=board.I2C())

st1 = MotorMover(kit.stepper1)
st2 = MotorMover(kit.stepper2)

@app.route('/')
def hello():
    # st1.move(1000, STEPPER.FORWARD, STEPPER.DOUBLE)
    # st2.move(1500, STEPPER.FORWARD, STEPPER.DOUBLE)
    st1.stepper.release()
    st2.stepper.release()
    return render_template('index.html')

@app.route('/v1/moveForward')
def moveForward():
    args = request.args
    args = args.to_dict()
    if "steps" in args:
        steps = args["steps"]
        if not steps.isnumeric():
            st1.stepper.release()
            st2.stepper.release()
            return json.dumps({'success':False, 'error':'steps must be an int'}), 400, {'ContentType':'application/json'}
        steps = int(steps)
        st1.move(steps, STEPPER.FORWARD, STEPPER.DOUBLE)
        st2.move(steps, STEPPER.FORWARD, STEPPER.DOUBLE)
    else:
        print("steps not in args in moveForward")
    st1.stepper.release()
    st2.stepper.release()
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'}
    
@app.route('/v1/moveBackward')
def moveBackward():
    args = request.args
    args = args.to_dict()
    if "steps" in args:
        steps = args["steps"]
        if not steps.isnumeric():
            st1.stepper.release()
            st2.stepper.release()
            return json.dumps({'success':False, 'error':'steps must be an int'}), 400, {'ContentType':'application/json'}
        steps = int(steps)
        st1.move(steps, STEPPER.BACKWARD, STEPPER.DOUBLE)
        st2.move(steps, STEPPER.BACKWARD, STEPPER.DOUBLE)
    else:
        print("steps not in args in moveBackward")
    st1.stepper.release()
    st2.stepper.release()
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'}


@app.route('/v1/moveStop')
def moveStop():
    st1.move(0, STEPPER.FORWARD, STEPPER.DOUBLE)
    st2.move(0, STEPPER.FORWARD, STEPPER.DOUBLE)
    st1.stepper.release()
    st2.stepper.release()
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'}

