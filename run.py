import matplotlib.pyplot as plt
import numpy as np
from bicycle_model import Bicycle
import keyboard
from ui import plot_car

car = Bicycle()

D_STEER = 0.2
D_A = 0.5

area = 20

def loop():
    pressed = False
    while True:
        if keyboard.is_pressed('right'):
            pressed = True
            a, d_steer = 0, -D_STEER
        if keyboard.is_pressed('left'):
            pressed = True
            a, d_steer = 0, D_STEER
        if keyboard.is_pressed('up'):
            pressed = True
            a, d_steer = D_A, 0
        if keyboard.is_pressed('down'):
            pressed = True
            a, d_steer = -D_A, 0
        if keyboard.is_pressed('up+left'):
            pressed = True
            a, d_steer = D_A, D_STEER
        if keyboard.is_pressed('up+right'):
            pressed = True
            a, d_steer = D_A, -D_STEER
        
        if pressed:
            car.step(a, d_steer)
        else:
            car.step(0, 0)
            
        pressed = False

        plt.clf()
        plt.xlim([-area, area])
        plt.ylim([-area, area])
        plot_car(car.xc, car.yc, car.theta, car.delta)
        #plt.plot(car.xc, car.yc, 'or')
        plt.draw()
        plt.pause(0.001)

loop()
