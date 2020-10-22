#! /usr/bin/env python3

import time, sys, re, pyautogui
from datetime import datetime

print("Reference:\n" "5:00 PM = 17:00\n" "6:00 PM = 18:00\n" "7:00 PM = 19:00")

while True:
    sleeps = input('what time (in HH:MM) to turn off?: ')
    if re.match('^([0-1]?[0-9]|2[0-3]):[0-5][0-9]$',sleeps) == None:
        print("Please input time in HH:MM format\n")
        time.sleep(1)
        continue
    else:
        break

'''function that presses F15 key every 5 mins to simulate being "active"'''
def lazy(sleeps):
    sleeps = datetime.now().replace(hour=int(sleeps[0:2]),minute=int(sleeps[3:5])).time()
    now = datetime.now().time()
    hours = sleeps.hour - now.hour
    if hours >= 0:
        print("\n"+ str(hours) + "-ish hours until program (maybe) stops\n"
        '\nIn the meantime, you can minimize and let program run in background, or close out box to end early' )
        while True:
            now = datetime.now().time()
            if now < sleeps:
                pyautogui.press("F15")
                time.sleep(300)
            else:
                print("\nIt's quittin time in 5...4...")
                time.sleep(5)
                sys.exit()
    else:
        print("that's", (sleeps.hour - now.hour) * -1, "hour(s) prior to the current time. please start again and enter a later time")
        time.sleep(3)
        sys.exit()

lazy(sleeps)

#if __name__ =="__main__":
#    if len(sys.argv) == 2:
#        lazy(sys.argv[1])
#    else:
#        print("no go")
