from os import system

clear = lambda : system("clear") # place at the top of your code

from time import sleep

# clear() to clear screen
# sleep(secs) to pause

#Your theme: Haunted Emoji 04Hoedown

sleepy = "😪"

x = 2 * 2
for i in range(10, 20):
    print(i , i* sleepy)
    sleep(0.1)
for i in range(x):
    print(i, i * sleepy)
    x += 2