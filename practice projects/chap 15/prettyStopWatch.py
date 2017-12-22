#!/usr/bin/env python3
# stopwatch.py - A simple stopwatch program.
''' Expand the stopwatch project from this chapter so that it uses the
rjust() and ljust() string methods to “prettify” the output.

Next, use the pyperclip module introduced in Chapter  6 to copy the text
output to the clipboard so the user can quickly paste the output to a
text file or email.'''

import time
import pyperclip

# Display the program's instructions.
print('Press ENTER to begin. Afterwards, press ENTER to "click" '
      'the stopwatch. Press Ctrl-C to quit.')
input()                    # press Enter to begin
print('Started.')
startTime = time.time()    # get the first lap's start time
lastTime = startTime
lapNum = 1
totalRecord =''

# Start tracking the lap times.
try:
    while True:
        input()
        now = time.time()
        lapTime = round(now - lastTime, 2)
        totalTime = round(now - startTime, 2)
        strLapTime = '%0.2f' % (lapTime)
        strTotalTime = '%0.2f' % (totalTime)
        record = 'Lap #%s: %s %s' % (str(lapNum).rjust(2), strTotalTime.\
                rjust(5), ('(' + strLapTime + ')').rjust(8))
        totalRecord += record + '\n'
        print(record, end='')
        lapNum += 1
        lastTime = time.time() # reset the last lap time
# Handle the Ctrl-C exception to keep its error message from displaying.
except KeyboardInterrupt:
    pyperclip.copy(totalRecord)
    print('\nDone.')
