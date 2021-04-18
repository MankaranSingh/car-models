import numpy as np

class Bicycle():
    def __init__(self):
        self.xc = 0
        self.yc = 0
        self.v = 0
        self.theta = 0
        self.delta = 0
        self.beta = 0
        
        self.L = 2.56
        self.lr = self.L / 2
        
    def reset(self):
        self.xc = 0
        self.yc = 0
        self.theta = 0
        self.delta = 0
        self.beta = 0
        
    def step(self, a, d_delta, dt=0.2):
        
        dx = self.v*np.cos(self.theta) * dt 
        dy = self.v*np.sin(self.theta) * dt 
        self.xc = self.xc + dx
        self.yc = self.yc + dy
        self.theta = self.theta + self.v*np.cos(self.beta)*np.tan(self.delta)/self.L * dt
        self.beta = np.arctan(self.lr*self.delta/self.L)
        self.v += a*dt - self.v / 25
        self.delta += d_delta
        self.delta = np.clip(self.delta, -0.5, 0.5)
        self.v = np.clip(self.v, 0, 20)
