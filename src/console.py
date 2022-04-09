from functions import timer, sleep, validTime, sleepOntimer
from Timing import Timing

inp = input('Please insert time in the formt of \"hh::mm:ss\": ')

while not validTime(inp):
    print('Wrong time!!')
    inp = input('Please insert time in the formt of \"hh::mm:ss\": ')

h, m, s = map(int, inp.split(':'))
t = Timing(s, m, h)
sleepOntimer(t,True)