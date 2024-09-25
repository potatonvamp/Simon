import board
import time
from digitalio import DigitalInOut, Direction
import random

blue = DigitalInOut(board.D2)
blue.direction = Direction.OUTPUT
blue.value = False

yellow = DigitalInOut(board.D3)
yellow.direction = Direction.OUTPUT
yellow.value = False

green = DigitalInOut(board.D4)
green.direction = Direction.OUTPUT
green.value = False

red = DigitalInOut(board.D5)
red.direction = Direction.OUTPUT
red.value = False

bluebtn = DigitalInOut(board.D9)
bluebtn.direction = Direction.OUTPUT
bluebtn.value = False

yellowbtn = DigitalInOut(board.D8)
yellowbtn.direction = Direction.OUTPUT
yellowbtn.value = False

greenbtn = DigitalInOut(board.D7)
greenbtn.direction = Direction.OUTPUT
greenbtn.value = False

redbtn = DigitalInOut(board.D6)
redbtn.direction = Direction.OUTPUT
redbtn.value = False

white = DigitalInOut(board.D10)
white.direction = Direction.INPUT


points = 0
sequence = []


def blink(light):
    light.value = not light.value
    time.sleep(.6)
    light.value = not light.value
    time.sleep(.6)
    

def add_sequence(me):
    me.append(random.randint(0,3))
    
def user():
    while not bluebtn.value and not yellowbtn.value and not greenbtn.value and not redbtn.value:
        pass
    if bluebtn.value:
        blink(blue)
        return 0
    if yellowbtn.value:
        blink(yellow)
        return 1
    if greenbtn.value:
        blink(green)
        return 2
    if redbtn.value:
        blink(red)
        return 3
        
def display_sequence(me):
    for x in me:
        if x == 0:
            blink(blue)
        if x == 1:
            blink(yellow)
        if x == 2:
            blink(green)
        if x == 3:
            blink(blue)
            
def game_start():
    white.value
    
while True:
    if not game_start and :
        add_sequence(me)
        display_sequence(sequence)
        input = user()
            


game_start()
