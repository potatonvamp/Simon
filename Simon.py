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

White = DigitalInOut(board.D10)
White.direction = Direction.INPUT

Black = DigitalInOut(board.D11)
Black.direction = Direction.INPUT


sequence = []

def blink(light):
    light.value = not light.value
    time.sleep(.6)
    light.value = not light.vlue
    time.sleep(.6)
    

def add_sequence():
    sequence.append(random.randint(0,3))
    
def display_sequence(me):
    add_sequence
    
def game_start():
    while True:
        if White.value:
            
