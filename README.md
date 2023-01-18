# Stepper motor controller.
For use with [Adafruit DC and Stepper Motor Hat for Raspberry Pi](https://learn.adafruit.com/adafruit-dc-and-stepper-motor-hat-for-raspberry-pi) with an NVIDIA Jetson Nano.

## Installation
[Make a venv with python version 3.10.9.](https://stackoverflow.com/questions/1534210/use-different-python-version-with-virtualenv)

Once venv is created, activate the venv by running:

    source ./bin/activate

Install the requirements from requirements.txt:

    pip3 install -r requirements.txt
    
Run the example with:

    python3 simultaneous_stepper.py

Set the flask environment variables:

    export FLASK_APP=server
    export FLASK_DEBUG=1

Run the flask server with:

    flask run
