"""
# This is an example that shows how Log Levels can be used.
# The logLevel can also be specified in the configuration file like:
# xApMon_loglevel = INFO
"""
from __future__ import print_function
from builtins import range
import apmon
import time

# Also, we show how you can initialize using a hash of hashes.
# By default, cpu_usr cpu_sys are not sent. This way you can enable them
apm = apmon.ApMon({'pcardaab.cern.ch': {'sys_cpu_usr': True, 'sys_cpu_sys': True, 'job_monitoring': False}}, defaultLogLevel=apmon.Logger.WARNING)
# apm.setLogLevel("DEBUG")

for i in range(1, 100):
    print('Sending i =', i)
    if i == 20:
        apm.setLogLevel("NOTICE")
    if i == 50:
        apm.setLogLevel("DEBUG")
    apm.sendParameters("MyCluster", "MyNode", {'val_i':i})
    apm.sendTimedParameters("MyClusterOld", "MyNodeOld", time.time() - 5*3600, {'val_ii': i})
    time.sleep(1)
