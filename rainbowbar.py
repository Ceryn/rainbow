#!/usr/bin/python

import sys, os, signal
from time import sleep, time
from rainbow import rainbow

secs  = 2
fps   = 25
bar   = 'scroll'
width = 3

# Parse command line.
try:
    argc = len(sys.argv)
    if argc >= 2:
        bar = sys.argv[1]
        if bar not in ['scroll', 'pulse']:
            raise
    if argc >= 3:
        secs = int(sys.argv[2])
    if argc >= 4:
        fps = int(sys.argv[3])
    elif bar == 'pulse':
        fps = 10
        if argc >= 5:
            width = int(sys.argv[4])
except:
    print 'Usage:'
    print '    ' + sys.argv[0]
    print '    ' + sys.argv[0] + ' scroll [secs [fps [width]]]'
    print '    ' + sys.argv[0] + ' pulse  [secs [fps]]'
    sys.exit(0)

# Exit gracefully on sigint (ctrl+c).
def sigint(signal, frame):
    sys.stdout.write('\r')
    os.system('tput cnorm')
    sys.exit(0)
signal.signal(signal.SIGINT, sigint)

strs = file.read(sys.stdin).splitlines()
r = rainbow(fps)
t = time()
# Turn the cursor invisible
os.system('tput civis')
first = True
# Until we are out of time, draw the next frame and sleep a bit.
while not secs or time() - t < secs:
    # Do not delete written text before it has been written for the first time.
    if first:
        first = False
    else:
        sys.stdout.write("\033["+str(len(strs))+"A")
    for s in strs:
        sys.stdout.write("\r")

        if bar == 'scroll':
            r.scrollbar(s, width)
        else:
            r.pulsebar(s)
        sys.stdout.write('\n')
    sys.stdout.flush()
    sleep(0.01)

# Turn the cursor visible
os.system('tput cnorm')
