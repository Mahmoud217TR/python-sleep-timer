import os
import time
import re
from Timing import Timing

def timer(timing: Timing) -> None:
    time.sleep(timing.getTimeInSeconds())

def sleep() -> None:
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

def validTime(string) -> bool:
    return re.fullmatch('([0-9]{1,2}:){2}[0-9]{1,2}',string) != None

def sleepOntimer(timing: Timing, enablePrint: bool = False) -> None:
    if enablePrint:
        print('Sleeping After: {} ({} seconds)'.format(timing.getTime(),timing.getTimeInSeconds()))
    while timing.getTimeInSeconds() > 0:
        time.sleep(1)
        t = timing.changeTotalTime(-1)
        if enablePrint:
            print(t)
    sleep()