#!/usr/bin/python

"""
This is a simple test program for the 'apmon' Python module.

"""
from __future__ import print_function

import apmon
import time
from Logger import Logger
# read destination hosts form file

apmonUrls = ["http://lxgate35.cern.ch:40808/ApMonConf1", "http://monalisa.cacr.caltech.edu:40808/ApMonConf"]
apm = apmon.ApMon(apmonUrls, Logger.DEBUG)

if not apm.initializedOK():
    print("It seems that ApMon cannot read its configuration. Setting the default destination")
    apm.setDestinations({'pcardaab.cern.ch:8884': {'sys_monitoring': 0, 'general_info': 0, 'job_monitoring': 1, 'job_interval': 300}})


# set the destinations as a tuple of strings
# apm = apmon.ApMon (('141.85.99.136:8453', 'ui.rogrid.pub.ro'))
# or
# apm = apmon.ApMon(('ui.rogrid.pub.ro:8884', ))   # trailing comma => tuple with a single value!

# read the destinations from a URL
# apm = apmon.ApMon("http://rb.rogrid.pub.ro/~catac/destinations.conf")

# check for changes in the configuration files
# apm.configRecheck = True
# apm.configRecheckInterval = 10 # (time in seconds)
print(("ApmTest: Destinations:", apm.destinations))

# nodeName will be the machine's full hostname
apm.sendParameters("MyCluster1_py", None, {'a': .5, 'b': 23, 'c': 3.32, 'd': 4.99})
apm.sendParameters("MyCluster1_py_in_order", None, [('a', .5), ('b', 23), ('c', 3.32), ('d', 4.99)])

# clusterName will be "MyCluster1", given by last sendParameters call.
apm.sendParameter(None, "MyNodeName", "jobs_started", 10)

# default clusterName will be changed
apm.sendParameter("MyCluster2_py", "MyNodeName", "total_memory", 20)

for i in list(range(500)):
    # clusterName = "MyCluster2", given by last apmon call
    # nodeName = the machine's full hostname
    apm.sendParams({'cpu_load': (int((i % 11) // 10.0)), 'jobs_finished': i})
    print("ApmTest: sent", (int((i % 11) // 10.0)), i % 11)
    time.sleep(.005)
print("ApmTest: Done.")
apm.free()
