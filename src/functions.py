import os
import time
import re
from typing import Tuple
from Timing import Timing


# Sleep timer usinf Timing class
def timer(timing: Timing) -> None:
    time.sleep(timing.getTimeInSeconds())

# Sleep Command
def sleep() -> None:
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

# Uses Timer to put PC in sleep
def sleepOntimer(timing: Timing, enablePrint: bool = False) -> None:
    if enablePrint:
        print('Sleeping After: {} ({} seconds)'.format(timing.getTime(),timing.getTimeInSeconds()))
    while timing.getTimeInSeconds() > 0:
        time.sleep(1)
        t = timing.changeTotalTime(-1)
        if enablePrint:
            print(t)
    sleep()

# Search string using regex for hh:mm:ss and returns it as string
def getTimeFromString(string) -> str:
    res = re.search('([0-9]{1,2}:){2}[0-9]{1,2}',string)
    if res != None:
        return str(res.group())
    return res

# Checks if num is in the range (0, end)
def inRange(num, end):
    if num > end or end < 0:
        return False
    return True

# Splits time as string and returns a tuple (hours, minutes, seconds)
def getTimeParts(string)->tuple():
    timing = tuple(map(int,string.split(':')))
    if inRange(timing[0], 24) and inRange(timing[1], 59) and inRange(timing[2], 59):
        return timing
    return None       

# Returns a Timing Object from string
def getValidTime(string) -> Timing():
    timing = getTimeFromString(string)
    if timing:
        timeParts = getTimeParts(timing)
        if timeParts:
            return Timing(timeParts[2], timeParts[1], timeParts[0])
    return None
