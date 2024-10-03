import board
import time
from digitalio import DigitalInOut, Direction
import random

blue = DigitalInOut(board.D2)
blue.direction = Direction.OUTPUT


yellow = DigitalInOut(board.D3)
yellow.direction = Direction.OUTPUT


green = DigitalInOut(board.D4)
green.direction = Direction.OUTPUT


red = DigitalInOut(board.D5)
red.direction = Direction.OUTPUT


bluebtn = DigitalInOut(board.D9)
bluebtn.direction = Direction.INPUT


yellowbtn = DigitalInOut(board.D8)
yellowbtn.direction = Direction.INPUT


greenbtn = DigitalInOut(board.D7)
greenbtn.direction = Direction.INPUT


redbtn = DigitalInOut(board.D6)
redbtn.direction = Direction.INPUT


white = DigitalInOut(board.D10)
white.direction = Direction.INPUT

points = 0
sequence = []
count = 0
game_start = False


def blink(light):
    """
    This function allows for a led to blink so you can call this function later on which allows the lights to blink.
    
    light.value: a light thats on
    time.sleep: the lights turned off
    
    returns a blinking light
    """
    light.value = not light.value
    time.sleep(.3)
    light.value = not light.value
    time.sleep(.3)


def lose():
    """
    Makes it so the leds blink when you lose and shows off your score.
    
    blue.value: blue Led turned on
    red.value: red Led turned on
    yellow.value: yellow Led turned on
    green.value: green Led turned on

    Returns all lights blinking and a blinking light that shows your score
    """
    global sequence
    global game_start
    global count
    global points
    blue.value = True
    red.value = True
    yellow.value = True
    green.value = True
    time.sleep(.6)
    sequence = []
    blue.value = False
    red.value = False
    yellow.value = False
    green.value = False
    game_start = False
    time.sleep(.2)
    score(points)
    print(points)


def score(game_score):
    """
    Does the math to show your score in 10’s and 1’s places.

    score_ones = game_score % 10: does the math for the 1’s place
    score_tens = game_score // 10: does the math for the 10’s place
    for i in range(score_ones): every time the math is in the 1’s place it blinks the red light
    for i in range(score_tens): every time the math is the 10’s place it blinks the green light.

    returns blinking lights that show your score
    """
    global points
    score_ones = game_score % 10
    score_tens = game_score // 10
    for i in range(score_ones):
        blink(red)
    for i in range(score_tens):
        blink(green)


def add_sequence(me):
    """
    Adds a random number to the list so the sequence for simon is random.

    me.append(random.randint(0, 3)): Adds a random number between 0-3 to the list.

    Returns a random addition to the list.
    """
    me.append(random.randint(0, 3))


def user():
    """
    This function makes it so that if you press a button the led that corresponds lights up

    while not (bluebtn.value or yellowbtn.value or greenbtn.value or redbtn.value): This makes it so that if none of the buttons are pressed it moves on to the next thing in the function.

    Returns a number depending on what led blinked and what button got pressed.
    """
    while not (bluebtn.value or yellowbtn.value or greenbtn.value or redbtn.value):
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


def display_sequence():
    """
    This function makes it so that the random sequence of LEDs is shown.
    
    for i in range(len(sequence)): Makes it so that if the random number that is picked from the sequence is the same number as a light, the led lights up.
        if sequence[i] == 3:
            blink(red)
        elif sequence[i] == 2:
            blink(green)
        elif sequence[i] == 1:
            blink(yellow)
        elif sequence[i] == 0:
            blink(blue)
            
    for i in range(len(sequence)): Makes it so if the user presses a button it adds that to the count and keeps the sequence going
        press = user()
        if press == sequence[i]:
            count += 1
            print(score)
        else:
            count = 0
            lose()
    
    returns the simon sequence as blinking lights
    """
    global sequence
    global count
    count = 0
    add_sequence(sequence)
    for i in range(len(sequence)):
        if sequence[i] == 3:
            blink(red)
        elif sequence[i] == 2:
            blink(green)
        elif sequence[i] == 1:
            blink(yellow)
        elif sequence[i] == 0:
            blink(blue)
    for i in range(len(sequence)):
        press = user()
        if press == sequence[i]:
            count += 1
            print(score)
        else:
            count = 0
            lose()
            return


def user_press():
    """
    Counts the amount of times the user pressed the buttons in comparison to the length of the sequence.

    count == len(sequence): counts the length of the sequence.

    Returns the length of the sequence and makes count equal to that.
    """
    global count
    global sequence
    return count == len(sequence)


while True:
    """
    This while loop makes the game run after the white button is pressed and to keep running until the white button is pressed again.
    
    if not game_start and white.value: Makes it so that if the game didnt start and white button wasnt pressed, the game doesnt run.
        game_start = True
        time.sleep(.5)
        
    if game_start: Makes it so if the game starts, the sequence runs and simon plays and your score is shown when you lose.
        display_sequence()
        if user_press():
            points += 1
            time.sleep(1)
            
    if not game_start and white.value: Makes it so if the game ended, it starts a new game.
        if not game_start:
            sequence = []
            score = 0
            game_start = True
    
    """
    if not game_start and white.value:
        game_start = True
        time.sleep(.5)
    if game_start:
        display_sequence()
        if user_press():
            points += 1
            time.sleep(1)
    if not game_start and white.value:
        if not game_start:
            sequence = []
            score = 0
            game_start = True



