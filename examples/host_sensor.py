"""
# This example shows how ApMon can be used as a simple host sensor to monitor and send
# the desired parameters to the MonALISA service (configured in the given file/url/list)
"""
from __future__ import print_function
import apmon
import os
import time

# apm = apmon.ApMon('dest_3.conf');
apm = apmon.ApMon('http://monalisa2.cern.ch/~catac/apmon/destinations.conf')
# apm = apmon.ApMon('http://gangamon.cern.ch:8080/apmon/ganga.conf');
# apm = apmon.ApMon({'lxgate35.cern.ch' : {'sys_interval' : 10}});
apm.setLogLevel('DEBUG')

my_host = os.popen('hostname -f').readline().strip()
# the background data about the system will be sent with this cluster and node
apm.setMonitorClusterNode("MyTestSensor", my_host)

print("host-sensor: sleeping forever; hit ctrl+c to stop")
# sleep forever
while True:
    time.sleep(1)
