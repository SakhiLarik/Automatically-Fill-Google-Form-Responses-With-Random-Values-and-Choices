import pandas as pd
import time
import math
import random
import pyautogui as pgt
import webbrowser

dataset = pd.read_csv("./dataset.csv")


i = 0
names = dataset['name']
roll_clm = 3
batch_clm = 5    

def choiceOptions():
    for x in range(0,6): # Options
        options = [1,2,3,4]
        pgt.press("down",presses=random.choice(options))
        pgt.press("tab")
    pgt.press("tab")

def fillSections():
    for i in range(0,4):
        choiceOptions()
        pgt.press("enter")
        time.sleep(5)
        pgt.press("tab",presses=3)

    pgt.hotkey("ctrl","w")

for name in names:

    url = "https://forms.gle/j775v2LGwLEYsHDi6" # Your google form url
    webbrowser.open(url)
    time.sleep(5)
    pgt.press('tab',presses=4)

    pgt.write(dataset['name'][i])
    pgt.press("tab")
    pgt.write(dataset['email'][i])
    pgt.press("tab")
    pgt.write(""+str((dataset['roll'].iloc[i]))) # Roll Number
    pgt.press("tab")
    pgt.write(dataset['department'][i])
    pgt.press("tab")
    pgt.write(""+str((dataset['batch'].iloc[i])))

    pgt.press("tab")
    pgt.press('enter')

    time.sleep(3)
    pgt.press("tab",presses=3)
    fillSections()

    time.sleep(3)


    i = i+1