import os

from os import system

clear = lambda : system("clear") # place at the top of your code

from time import sleep

size = os.get_terminal_size()
a = size.columns * size.lines
i = 1
e1="👺😱"
flyCommand=print(" " * i, e1)



import random
v = random.randint(0,a)
for i in range(a):
    j = print(" " * i, e1)
    sleep(0.009)
    clear()
print("💥" * a)

