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

White = DigitalInOut(board.D6)
White.direction = Direction.INPUT

Black = DigitalInOut(board.D7)
Black.direction = Direction.INPUT

Orange = DigitalInOut(board.D8)
Orange.direction = Direction.INPUT

my_list = []

def blink(me):
    me.value = not me.value
    time.sleep(.3)
    me.value = not me.value
    time.sleep(.3)
   
def add_to_sequence(yes):
   yes.append(random.randint(0, 3))

def display_sequence(yes):
   for item in yes:
       if item == 0:
           blink(blue)
       if item == 1:
           blink(yellow)
       if item == 2:
           blink(green)
       if item == 3:
           blink(red)

while True:
   if  Black.value:
       time.sleep(.3)
       add_to_sequence(my_list)
       print(my_list)
   elif White.value:
       time.sleep(.3)
       display_sequence(my_list)
       print(my_list)
   elif Orange.value:
       time.sleep(.3)
       my_list = []
