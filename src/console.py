from functions import getValidTime, sleepOntimer
from Timing import Timing

def takeInput() -> str:
    return input('Please insert time in the formt of \"hh::mm:ss\": ')

timing = getValidTime(takeInput())


while not timing:
    print('Wrong time!!')
    timing = getValidTime(takeInput())

sleepOntimer(timing,True)