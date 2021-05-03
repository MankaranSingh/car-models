import numpy as np
import math

L = 2.56  # [m]
Lr = L / 2.0  # [m]
Lf = L - Lr
Cf = 1600.0 * 2.0  # N/rad
Cr = 1700.0 * 2.0  # N/rad
Iz = 2250.0  # kg/m2
m = 1500.0  # kg


class DynamicBicycle:

    def __init__(self, x=0.0, y=0.0, theta=0.0, vx=0.01, vy=0.0, omega=0.0):
        self.xc = x
        self.yc = y
        self.theta = theta
        self.vx = vx
        self.vy = vy
        self.omega = omega
        self.delta = 0.0
        self.L = L
        self.lr = Lr
        
    def step(self, a, d_delta, dt=0.2):
        if self.vx < 0.1:
            self.stepKinematic(a, d_delta)
        else:
            self.stepDynamic(a, d_delta)
        
    def stepKinematic(self, a, d_delta, dt=0.2):
        dx = self.vx*np.cos(self.theta) * dt 
        dy = self.vx*np.sin(self.theta) * dt 
        self.xc = self.xc + dx
        self.yc = self.yc + dy
        self.theta = self.theta + self.vx*np.cos(self.omega)*np.tan(self.delta)/self.L * dt
        self.beta = np.arctan(self.lr*self.delta/self.L)
        self.vx += a*dt - self.vx / 25
        self.delta += d_delta
        self.delta = np.clip(self.delta, -0.5, 0.5)
        self.vx = np.clip(self.vx, 0, 20)

    def stepDynamic(self, a, d_delta, dt=0.2):
        self.xc = self.xc + self.vx * math.cos(self.theta) * dt - self.vy * math.sin(self.theta) * dt
        self.yc = self.yc + self.vx * math.sin(self.theta) * dt + self.vy * math.cos(self.theta) * dt
        self.theta = self.theta + self.omega * dt
        Ffy = -Cf * math.atan2(((self.vy + Lf * self.omega) / self.vx - self.delta), 1.0)
        Fry = -Cr * math.atan2((self.vy - Lr * self.omega) / self.vx, 1.0)
        self.vx = self.vx + (a - Ffy * math.sin(self.delta) / m + self.vy * self.omega) * dt - self.vx / 25
        self.vy = self.vy + (Fry / m + Ffy * math.cos(self.delta) / m - self.vx * self.omega) * dt
        self.omega = self.omega + (Ffy * Lf * math.cos(self.delta) - Fry * Lr) / Iz * dt
        self.delta += d_delta
        self.vx = np.clip(self.vx, 0, 20)        
        self.delta = np.clip(self.delta, -0.5, 0.5)
        

