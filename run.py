#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
from flask_script import Manager
from time import sleep
import threading
import hardware
import config

app = Flask(__name__)
app.config.from_object(config)
manager = Manager(app)


@app.route('/')
def hello_world():
    return render_template("index.html")


#
# 定义全局变量
# 之后要修改要定义 motor_status 的值是从数据库中读取以读取实时状态
motor_1_status = "stop"
# motor_2_status = "stop"
# motor_3_status = "stop"
# motor_4_status = "stop"
# motor_5_status = "stop"


#
# ######################## motor settings ########################
# motor one settings
class motor_1_run:
    def __init__(self):
        global motor_1_status
        self.motor = hardware.motor()

    def set_fast(self):
        sleep(0.05)
        self.motor.motor_speed(speed=3)
        sleep(0.05)
        # print("set fast model")

    def set_middle(self):
        sleep(0.05)
        self.motor.motor_speed(speed=2)
        sleep(0.05)
        # print("set middle model")

    def set_low(self):
        sleep(0.05)
        self.motor.motor_speed(speed=1)
        sleep(0.05)
        # print("set low model")

    def run_fast(self):
        self.set_fast()
        self.motor.motor_start()
        while motor_1_status == "fast":
            pass

    def run_middle(self):
        self.set_middle()
        self.motor.motor_start()
        while motor_1_status == "middle":
            pass

    def run_low(self):
        self.set_low()
        self.motor.motor_start()
        while motor_1_status == "low":
            pass

    def run_stop(self):
        self.motor.motor_stop()




# ################### motor controlling #####################

# motor one
# 定义在函数内部，页面刷新后，会释放掉对象，导致刷新页面后会停止
# 因为这个原因，只能定义在函数外面了
motor_one = motor_1_run()

@app.route('/motor_1')
def motor_1():

    global motor_1_status
    motor_order = request.args.get("motor_order")

    if (motor_1_status != "fast") and (motor_order == "fast"):
        # 分配线程，执行线程
        t = threading.Thread(target=motor_one.run_fast, args=())
        t.start()
        sleep(0.02)
        motor_1_status = "fast"
        print("motor one run in fast speed")

    elif (motor_1_status != "middle") and (motor_order == "middle"):

        # same as before
        t = threading.Thread(target=motor_one.run_middle, args=())
        t.start()
        sleep(0.02)
        motor_1_status = "middle"
        print("motor one run in middle speed")

    elif (motor_1_status != "low") and (motor_order == "low"):

        # same as before
        t = threading.Thread(target=motor_one.run_low, args=())
        t.start()
        sleep(0.02)
        motor_1_status = "low"
        print("motor one run in low speed")

    elif (motor_1_status != "stop") and (motor_order == "stop"):

        motor_one.run_stop()
        # 停止动机需要时间
        sleep(0.5)
        motor_1_status = "stop"

    elif (motor_order == "fast") and (motor_1_status == "fast"):
        print("motor one has run in fast speed")

    elif (motor_order == "middle") and (motor_1_status == "middle"):
        print("motor one has run in middle speed")

    elif (motor_order == "low") and (motor_1_status == "low"):
        print("motor one has run in low speed")

    elif (motor_order == "stop") and (motor_1_status == "stop"):
        print("motor one has stopped")

    return motor_1_status

# need add the motor control codes
@app.route('/motor_2')
def motor_2():
    motor_order = request.args.get("motor_order")
    # the controlling motor codes
    return motor_order

# need add the motor control codes
@app.route('/motor_3')
def motor_3():
    motor_order = request.args.get("motor_order")
    # the controlling motor codes
    return motor_order

# need add the motor control codes
@app.route('/motor_4')
def motor_4():
    motor_order = request.args.get("motor_order")
    # the controlling motor codes
    return motor_order

# need add the motor control codes
@app.route('/motor_5')
def motor_5():
    motor_order = request.args.get("motor_order")
    # the controlling motor codes
    return motor_order


# ################### ultrasound real time ##################
@app.route('/ultrasound_1')
def ultrasound_1():
    ultrasound = hardware.ultrasound()
    distance = ultrasound.get_distance_cm()
    return str(distance)

## need to modify ##
@app.route('/ultrasound_2')
def ultrasound_2():
    ultrasound = hardware.ultrasound()
    distance = ultrasound.get_distance_cm()
    return str(distance)

## need to modify ##
@app.route('/ultrasound_3')
def ultrasound_3():
    ultrasound = hardware.ultrasound()
    distance = ultrasound.get_distance_cm()
    return str(distance)

## need to modify ##
@app.route('/ultrasound_4')
def ultrasound_4():
    ultrasound = hardware.ultrasound()
    distance = ultrasound.get_distance_cm()
    return str(distance)

## need to modify ##
@app.route('/ultrasound_5')
def ultrasound_5():
    ultrasound = hardware.ultrasound()
    distance = ultrasound.get_distance_cm()
    return str(distance)


if __name__ == '__main__':
    manager.run()
