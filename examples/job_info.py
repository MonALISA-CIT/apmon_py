"""
# This example shows how ApMon can be used to send information about a given job
# to the MonALISA service
# Also, note that:
# - you can monitor multiple jobs
# - the retrieved information is a sum for all processes forked from the given pid
# - you can stop background processes with stopBgProcesses() and still do system and
#   job monitoring. You just have to call sendBgMonitoring() whenever you want to
#   send the data. However, note that also the config checker process is stopped, so
#   if you get the config from a URL, and the configuration changes, you will not get the
#   changes.
"""
from __future__ import print_function
import apmon
import time
import os

# Each 10 seconds send information about given jobs and no information about the system
apm = apmon.ApMon(['dest_3.conf'])
print("apmon was init")
# Monitor this process and all its children
# apm.addJobToMonitor(os.getpid(), os.getcwd(), "JobInfoTest", "job")
apm.addJobToMonitor("1", os.getcwd(), "JobInfoTest", "job")

t = 40

print('Sleeping for 40 seconds')
time.sleep(t)

print('Working for 40 seconds')
start = time.time()
while start + t > time.time():
    pass

print('Preparing to finish in 40 seconds')
time.sleep(t)

# Although here this is not needed because program ends, you can stop monitoring a
# job if you need.
apm.removeJobToMonitor(os.getpid())
