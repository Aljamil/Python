# !/usr/bin/python
# Filename: def.py

def printMax(a, b):
    if a > b:
        print(a, 'is Maximum')

    elif a < b:
        print(b, 'is Maximum')

    else:
        print(a, ' is equal to ', b)


x = int(input())
y = int(input())

printMax(x, y)
