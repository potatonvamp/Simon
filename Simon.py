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



sequence = [0,3]

def add():
    pass
    
def game_over():
    

def display_sequence():
    
