#! /usr/bin/env python3

import time, sys, re, pyautogui
from datetime import datetime

refer = ['5:00PM = 17:00', '6:00PM = 18:00', "7:00PM = 19:00"] #create a table for user reference on 24HR conversion
print("Reference" "\n----------")
for time in refer:
    print("{:<8}".format(time))

while True:
    sleeps = input('what time (in HH:MM) to turn off?: ')
    if re.match('^([0-1]?[0-9]|2[0-3]):[0-5][0-9]$',sleeps) == None: # regex to test if user input is in correct format
        print("Please input time in HH:MM format\n")
        time.sleep(1)
        continue
    else:
        break

'''function that presses F15 key every 5 mins to simulate being "active"'''
def lazy(sleeps):
    sleeps = datetime.now().replace(hour=int(sleeps[0:2]),minute=int(sleeps[3:5])).time() # conversion of user input into useable datetime
    now = datetime.now().time()
    hours = sleeps.hour - now.hour
    if hours >= 0: # this part did not require any conversions of datetime, intgers would work
        print("\n"+ str(hours) + "-ish hours until program (maybe) stops\n"
        '\nIn the meantime, you can minimize and let program run in background, or close out box to end early' )
        while True:
            now = datetime.now().time()
            if now < sleeps: # this part required a datetime comparison to work
                pyautogui.press("F15")
                intervals = 60 * 5 # can perhaps add a user request at another point in time.
                time.sleep(intervals) # as of right now, set to loop every 5 mins.
            else:
                print("\nIt's quittin time in 5...4...")
                time.sleep(5)
                sys.exit()
    else:
        print("that's", (sleeps.hour - now.hour) * -1, "hour(s) prior to the current time. please start again and enter a later time")
        time.sleep(3)
        sys.exit() # because already used "correct formatting" loop from above, can not loop around to ask again to input another time.

lazy(sleeps)

#if __name__ =="__main__":
#    if len(sys.argv) == 2:
#        lazy(sys.argv[1])
#    else:
#        print("no go")
