#!/usr/bin/python3
# Filename: list1.py

shoplist = ['b', 'a', 'c', 'e', 'd']

print ('The total elements are', len(shoplist))

print ('The elements are: ', end=' ')

for item in shoplist:
    print (item, end=' ')

print ('\nI also have to add z.')

shoplist.append('z')

print ('The elements now are ', shoplist)

shoplist.sort()

print ('Sorted shoplist is ', shoplist)


