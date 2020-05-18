#!/usr/bin/python

# this code initializes an HTML page and hosts it

from flask import Flask
from flask import render_template
from Adafruit_PWM_Servo_Driver import PWM
import time

app = Flask(__name__)

# Initialise the PWM device using the default address
pwm = PWM(0x40)
# Note if you'd like more debug output you can instead run:
# pwm = PWM(0x40, debug=True)

servoMin = 150  # Min pulse length out of 4096
servoMax = 600  # Max pulse length out of 4096

# Servo 0 Range - 150 to 600
# Servo 1 Range - Will Test Later
# Servo 2 Range - 150 - 600
# Servo 3 Range - 150 - 375


def setServoPulse(channel, pulse):
    # initializes the frequencies and currents for the servo
    pulseLength = 1000000                   # 1,000,000 us per second
    pulseLength /= 60                       # 60 Hz
    print "%d us per period" % pulseLength
    pulseLength /= 4096                     # 12 bits of resolution
    print "%d us per bit" % pulseLength
    pulse *= 1000
    pulse /= pulseLength
    pwm.setPWM(channel, 0, pulse)


pwm.setPWMFreq(60)


def motorTest():
    pwm.setPWM(0, 0, servoMin)
    pwm.setPWM(2, 0, servoMin)
    time.sleep(1)
    pwm.setPWM(0, 0, 375)
    pwm.setPWM(2, 0, 375)
    time.sleep(1)
    pwm.setPWM(0, 0, servoMax)
    pwm.setPWM(2, 0, servoMax)
    time.sleep(1)
    pwm.setPWM(0, 0, servoMin)
    pwm.setPWM(2, 0, servoMin)
    time.sleep(1)


motorTest()


@app.route('/')
def mypysite(name=None):
    # return the html page i already made
    return render_template('index.html')


@app.route('/index.html')
def index():
    return render_template('index.html')


@app.route('/routine1.html')
def routine1():
    return motorTest()
    return render_template('routine1.html')


@app.route('/routine2.html')
def routine2():
    return motorTest()
    return render_template('routine2.html')


@app.route('/routine3.html')
def routine3():
    return motorTest()
    return render_template('routine3.html')


if __name__ == "__main__":
    # hosts the site locally
    app.run('0.0.0.0')
