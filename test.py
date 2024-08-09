import time
import random
import pyautogui as pg

animal = ['Dog','monkey', 'Cat']

time.sleep(10)

for i in range(50):
    anml = random.choice(animal)
    pg.write("You are a " + anml)
    pg.press("enter")
