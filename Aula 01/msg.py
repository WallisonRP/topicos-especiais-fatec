import random

import pyautogui as pg

import time

you = ("trouxa", "bobo", "zé ruela")

time.sleep(8)

for i in range(100):
    a = random.choice(you)
    pg.write(f"Voce e um {a}")
    pg.press('enter')
