#!/usr/bin/env python3

import xvfbman
import time
import os

xvfbman.registerAtExitCleanup

displayNum = xvfbman.startXvfbRange(1, 199, screenStr='1280x720x24')

print("Display number is: " + str(displayNum))


# -name is application name, not really sure what that does
# -T is window title
# -e is command and arguments - must be last on the line
# -display
#timeout 10s xterm -display :1 -name scrot-$1 -T scrot-$1 -e $temp_file &

cmd = 'xterm -display :' + str(displayNum) + ' -e /home/robin/pyx11/run.sh'
print(cmd)
stream = os.popen('xterm -display :' + str(displayNum) + ' -e /home/robin/pyx11/run.sh')
output = stream.read()
print("From the xterm")
print(output)

time.sleep(20)

print("Stopping the display")
success = xvfbman.stopXvfb(displayNum)

if success:
    print("Display successfully closed down")
else:
    print("There was a problem closing down the display")

print("Done")
