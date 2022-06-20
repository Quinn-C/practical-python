#!/usr/bin/env python3
# bounce.py
#
# Exercise 1.5
'''
Plan:
input height: 100
i = 10 
h -> h * 3 / 5
h = h * 3/5
if h 
'''

def print_height(h, t):
    for i in range(t):
        h = h * 3 / 5
        print(round(h, 4))

print_height(100, 10)


