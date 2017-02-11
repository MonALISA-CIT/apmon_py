"""
# This example shows how ApMon can be used to send the parameters
# to the MonALISA service (given in the constructor)
"""
from __future__ import division
import apmon
import time

# Initialize ApMon specifying that it should not send information about the system.
# Note that in this case the background monitoring process isn't stopped, in case you may
# want later to monitor a job.
apm = apmon.ApMon('dest_2.conf')
apm.setLogLevel("NOTICE")
apm.confCheck = False
apm.enableBgMonitoring(False)
apm.setMaxMsgRate(75)
apm.setMaxMsgSize(130)

for i in list(range(1,20000)):
    # you can put as many pairs of parameter_name, parameter_value as you want
    # but be careful not to create packets longer than 8K.
    apm.sendParameters("SimpleCluster1", "SimpleNode1", {'var_i': i, 'ar_i^2': i*i})
    f = 20.0 / i
    # send in the same cluster and node as last time;
    apm.sendParams({'var_f': f, '5_times_f': 5 * f, 'i+f': i + f, 'x' * 70: 'y' * 40})
    # print "simple_send-ing for i=",i
    time.sleep(0.1)
