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
count = 0
game_start = False


def blink(light):
    light.value = not light.value
    time.sleep(.3)
    light.value = not light.value
    time.sleep(.3)

def lose():
    global sequence
    global game_start
    global count
    blue.value = True
    red.value = True
    yellow.value = True
    green.value = True
    time.sleep(.6)
    sequence[]
    blue.value = False
    red.value = False
    yellow.value = False
    green.value = False
    game_start = False
    time.sleep(.2)
    score(scoring)
    print(scoring)
    
def score(game_score):
    global scoring
    score_ones = game_score % 10
    score_tens = game_score // 10
    for i in range(score_ones):
        blink(red)
    for i in range (score_tens):
        blink(green)

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
    
            

    
while True:
    if not game_start and white.value:
        add_sequence()
        display_sequence(sequence)
        input = user()
