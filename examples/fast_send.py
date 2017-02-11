"""
# This example shows how ApMon can be used to send the parameters 
# to the MonALISA service (given in the constructor)
"""

from __future__ import print_function

import apmon
import sys

# Initialize ApMon specifying that it should not send information about the system.
# Note that in this case the background monitoring process isn't stopped, in case you may
# want later to monitor a job.
apm = apmon.ApMon('dest_2.conf')
apm.setLogLevel("INFO")
apm.confCheck = False
apm.enableBgMonitoring(False)
apm.setMaxMsgRate(1000)

maxV = 0
try:
    maxV = int(sys.argv[1])
except IndexError as er:
    print("Error in first call parameter: "+str(er))

print("sending to", maxV)
for i in list(range(1, maxV)):
    # you can put as many pairs of parameter_name, parameter_value as you want
    # but be careful not to create packets longer than 8K.
    apm.sendParameters("SimpleCluster", "SimpleNode", {'var_i': i})
    # time.sleep(0.1);
