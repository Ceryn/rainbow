#!/usr/bin/python

import sys
from datetime import datetime
COLOURS = [1,2,3,4,5,6,7]

class rainbow:
    """
    The rainbow class provides static, scrolling or pulsating rainbow
    colouring of text. Exports pulsebar() and scrollbar().
    """
    odd = speed = colidx = lasttime = -1

    def __init__(self, fps=10):
        """Initiate speed based on fps."""
        onesecond = 1000000
        self.speed = onesecond / fps

    def pulsebar(self, text):
        """Write the text in the colour of the current time frame."""
        time = int(datetime.now().strftime("%f")) / self.speed
        sys.stdout.write("\033[0;3%dm%s\033[0m" % (COLOURS[time % len(COLOURS)], text))
        #sys.stdout.flush()

    def scrollbar(self, text, colourlen=8):
        """
        Write the text in colours specified by the current time frame.
        The text is coloured in columns of colourlen characters.
        """
        pos = i = 0
        textlen = len(text)
        if self.colidx < 0:
            self.colidx = 0
        if colourlen < 1:
            colourlen = 1
        if self.odd < 0:
            self.odd = colourlen - 1;

        now = datetime.now().strftime("%S%f")
        time = int(now[:2]) * 1000000 + int(now[2:])
        if abs(self.lasttime - time) >= self.speed:
            self.odd = (self.odd + 1) % colourlen
            self.lasttime = time
            if self.odd == 0:
                self.colidx = len(COLOURS) - 1 if self.colidx == 0 else self.colidx - 1

        while pos < self.odd and pos < textlen:
            sys.stdout.write("\033[0;3%dm%c\033[0m" % (COLOURS[self.colidx % len(COLOURS)], text[pos]))
            pos += 1
        while pos < textlen:
            sys.stdout.write("\033[0;3%dm%c\033[0m" % (COLOURS[(self.colidx + 1 + i / colourlen) % len(COLOURS)], text[pos]))
            pos += 1
            i += 1
        sys.stdout.write("\033[0m");
        #sys.stdout.flush()

if __name__ == "__main__":
    """Write the input text coloured in columns of argv[1] (or 3) characters."""
    if(len(sys.argv) > 1 and sys.argv[1] == '-v'):
        print 'Usage:'
        print '    ' + sys.argv[0] + ' [duration]'
        print '    ' + sys.argv[0] + ' -h'
        sys.exit(0)

    r = rainbow(1)
    while True:
        colourlen = int(sys.argv[1]) if len(sys.argv) > 1 else 3
        strs = file.read(sys.stdin).splitlines()
        for s in strs:
            r.scrollbar(s, colourlen)
            sys.stdout.write('\n')
        sys.exit(0)
