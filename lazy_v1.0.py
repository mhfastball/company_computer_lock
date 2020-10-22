#! /usr/bin/env python3

import time
import pyautogui as pag
from datetime import datetime
import sys

print("Reference:\n"
      "5:00 PM = 17:00\n"
      "6:00 PM = 18:00\n"
      "7:00 PM = 19:00")

while True:
    sleeps = input('what time (in HH:MM) to turn off?: ')
    if len(sleeps) <= 2:
        print("Please input in HH:MM format")
        continue
    else:
        break

sleeps = datetime.strptime(sleeps,"%H:%M").time()
now = datetime.now().time()

'''function that presses F15 key every 5 mins to simulate being "active"'''
def lazy(sleeps):
    hours = sleeps.hour - now.hour
    if hours >  0:
        print("\n"+ str(hours) + "-ish hours until program stops (or close out box to end)\n"
        '\nIn the meantime, you can minimize and let program run in the background' )
        while now < sleeps:
            pag.press("F15")
            time.sleep(300)
    else:
        print("thats", (hours) * -1, "hour(s) before the current time. Restart program and enter another time")
        time.sleep(10)
        sys.exit()

lazy(sleeps)

#if __name__ =="__main__":
#    if len(sys.argv) == 2:
#        lazy(sys.argv[1])
#    else:
#        print("no go")
