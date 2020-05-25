# -*- coding: utf-8 -*-
"""
Created on Sun May 24 16:38:12 2020

@author: qzane
"""

from pynput import mouse
from pynput.mouse import Button, Controller
from queue import Queue 
import ctypes
import time

USAGE = 'Double click the middle button to start auto swing and click to stop'

PROCESS_PER_MONITOR_DPI_AWARE = 2

ctypes.windll.shcore.SetProcessDpiAwareness(PROCESS_PER_MONITOR_DPI_AWARE)

class TerrariaAutoSwing:
    def __init__(self, TIME_THRESHOLD=0.3):
        self.TIME_THRESHOLD = TIME_THRESHOLD
        self.LAST_HIT = 0 # timestamp when you release the middle button
        self.HIT_TIMES = 0 # times of continued hit
        
        self.ctrl = Controller()
        self.listener = mouse.Listener(on_click=self.on_click)
        self.listener.start()
        
    def on_click(self, x, y, button, pressed):
        if button == Button.middle and not pressed:
            tstamp = time.time()
            delta = tstamp - self.LAST_HIT
            self.LAST_HIT = tstamp
            if delta <= self.TIME_THRESHOLD:
                self.HIT_TIMES += 1
            else:
                self.HIT_TIMES = 0
            print('here', self.HIT_TIMES)
                
    def register(self):
        self.listener = mouse.Listener(on_click=self.on_click)
        self.listener.start()
        
    def loop(self):
        while(1):
            if(self.HIT_TIMES):
                self.ctrl.press(Button.left)
                time.sleep(0.005)
                self.ctrl.release(Button.left)
                time.sleep(0.005)
            else:                
                time.sleep(0.01)
        
if __name__ == '__main__':
    print(USAGE)
    a = TerrariaAutoSwing()
    a.loop()
    
    
