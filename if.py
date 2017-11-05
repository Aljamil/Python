#!/usr/bin/python
# Filename: if.py

number = 23 
run = True

while run:
    guess = int(input('Enter an integer: '))

    if guess == number:
        print('Congratulations!')
        run = False
    elif guess > number:
        print('It is greater')

    else: 
        print('It is lesser')
else:
    print 'The while loop is OVER'


print 'Done!'
