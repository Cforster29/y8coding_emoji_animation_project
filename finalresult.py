import os

from os import system

clear = lambda : system("clear") # place at the top of your code

from time import sleep

# clear() to clear screen
# sleep(secs) to pause

#Your theme: Haunted Emoji Hoedown

cp = "👻 👹 😱 😨 🎃 😈 👺 💀 ⚰️ 🧛 🦇"

e1 = "👹"
e2 = "👻"
fs = 12250
hfs = 3184
l1 = 202


print(e1 * hfs + " 😱  WAAAA", e1 * hfs)
sleep(5)
print(e2 * hfs + " 😨  EEK!!", e2 * hfs)
sleep(5)
clear()

for _ in range(3):
    for y in range(2):
        print("🧛")
        sleep(0.2)
    print("🦇")
    sleep(2)
    clear()
    for x in range(2):
        print("🎃")
        sleep(0.2)
    print("😈")


print(" " * 1040, "WELCOME")
sleep(0.5)
clear()
print(" " * 1040, "TO")
sleep(0.5)
clear()
print(" " * 1040, "THE")
sleep(0.5)
clear()
print(" " * 1040, "HAUNTED")
sleep(0.5)
clear()
print(" " * 1040, "CLUBBBB!!!")
sleep(0.5)
clear()


a=1








