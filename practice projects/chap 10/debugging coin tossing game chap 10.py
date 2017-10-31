#!/usr/bin/env python3
'''
The following program is meant to be a simple coin toss guessing game.
The player gets two guesses (it’s an easy game). However, the program
has several bugs in it. Run through the program a few times to find
the bugs that keep the program from working correctly.
'''

import random, logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s %(message)s')
# logging.disable(logging.CRITICAL) # Disables all messages at the critical level or lower.

def convert (number):
    assert number == 0 or number == 1, 'Toss should be 1 or 0!!!'
    if number == 0:
        return 'tails'
    elif number == 1:
        return 'heads'


logging.debug('Start of program')
                    
guess = ''

while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
    logging.critical('Guess is {0}'.format(guess))
toss = random.randint(0, 1) # 0 is tails, 1 is heads
logging.warning('Tossed number is {0}'.format(toss))
toss = convert(toss)
logging.debug('Converted string is {0}'.format(toss))

if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    logging.debug('Guess is {0}'.format(guess))
    if toss == guess:
       print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
