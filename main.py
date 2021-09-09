import sys
import pygame
from pygame.locals import *
import pyautogui
from time import time, sleep
#-------------------------Global variables--------------------------
Running = True
#------------------------init pygame and joy------------------------
pygame.init()
clock = pygame.time.Clock()
pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
# for joystick in joysticks:
#     print(joystick.get_name())
#---------------------------Key Execution---------------------------
def hotkey_bleepingON():
    pyautogui.keyDown('f13')
def hotkey_bleepingOFF():
    pyautogui.keyUp('f13')

def hotkey_VoiceChangerON():
    pyautogui.keyDown('f14')
def hotkey_VoiceChangerOFF():
    pyautogui.keyDown('f14')


#---------------------------Checking loop---------------------------
def Check_loop():
    global Running
    while Running:
        for event in pygame.event.get():
            if event.type == JOYBUTTONDOWN:
                print(event)
                if event.button == 0:
                    hotkey_bleepingON()
                elif event.button == 1:
                    hotkey_VoiceChangerON()
                elif event.button == 2:
                    pass
                elif event.button == 3:
                    pass
                elif event.button == 4:
                    pass
                elif event.button == 5:
                    pass
                elif event.button == 6:
                    pass
                elif event.button == 7:
                    pass
                elif event.button == 8:
                    pass
                elif event.button == 9:
                    pass
                elif event.button == 10:
                    pass
                elif event.button == 11:
                    pass
            if event.type == JOYBUTTONUP:
                print(event)
                if event.button == 0:
                    hotkey_bleepingOFF()
                elif event.button == 1:
                    hotkey_VoiceChangerOFF()
                elif event.button == 2:
                    pass
                elif event.button == 3:
                    pass
                elif event.button == 4:
                    pass
                elif event.button == 5:
                    pass
                elif event.button == 6:
                    pass
                elif event.button == 7:
                    pass
                elif event.button == 8:
                    pass
                elif event.button == 9:
                    pass
                elif event.button == 10:
                    pass
                elif event.button == 11:
                    pass
        clock.tick(100)
Check_loop()