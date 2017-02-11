"""
# This example shows how ApMon can be used to send parameters with a
# given time, set by user to the MonALISA service
# This feature can be useful, for example, if you generate the parameters by
# parsing a log file and you want that they have the time from the log.
"""
from __future__ import print_function
import apmon
import time
import random

# Initialize ApMon by specifying a ref to a list of hosts having a MonALISA service running
# with monXDRUDP module enabled.
# Note that background monitor process sends information about the host. In apmon.py
# is the list with default parameters. If you want to modify what is sent, you can
# take the configuration from a file or URL
apm = apmon.ApMon(('pcardaab.cern.ch:8884', ))

for i in list(range(1, 20)):
    my_time = time.time() - 2 * 3600 - (20 - i) * 60
    state = int(random.randint(0, 10))
    # Note that also there's a sendTimedParams version
    apm.sendTimedParameters("LogParser", "SomeApp", my_time, {'state': state})
    print("Set for i=", i)
