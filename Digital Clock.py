import time
from unittest import result

# Digital Clock
def digital_clock():
    localtime = time.localtime()
    result = time.strftime('%I:%M:%S %p', localtime) # %I for 12 hour clock %H for 24 hour clock
    print(result, "\r", end="", flush=True) # /r rewind back to start of the line
    time.sleep(1)

while True:
    digital_clock()
