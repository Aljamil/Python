#!/usr/bin/python
# Filename: scope.py

def outer():
    x = 20
    print('x is ', x)

    def inner():
        nonlocal x
        x = 5


    inner()
    print('Changed local x to ', x)

outer()
