
"""
# This example shows how ApMon can get its configuration from a cgi script or a servlet -
# there's no change needed in the code. You just have to point the URL from where to read
# the configuration to your cgi script / servlet. This allows generating the configuration
# based on the IP from where the request came, or based on some parameters sent by the user.

# Being able to get the configuration based on the IP address of the
# request can be useful if for example you have a distributed system that
# allows users to run jobs and each worker node where the job is run
# you want to report the data to the closest MonALISA service without having
# to know apriori on which site the job would run.

# Generating the config based on parameters is useful for example to send the
# the information from 2 or more different applications to different dedicated
# MonALISA services.
"""
from __future__ import print_function
import os
import time
import apmon

# change the value for appName parameter to see the difference.
# Also see the cgi script and/or the servlet that generates the configuration
apm = apmon.ApMon("http://pcardaab.cern.ch:8888/cgi-bin/ApMonConf?appName=confgen_test")

apm.setLogLevel("DEBUG")

my_host = os.popen('hostname -f').readline().strip()

# the background data about the system will be sent with this cluster and node
apm.setMonitorClusterNode("MyStatus", my_host)

# just send some data
x = 0
while x < 20:
    print("Sending for x = ", x)
    apm.sendParameter("MyCluster", "MyNode", "x", x)
    time.sleep(1)
    x += 1
