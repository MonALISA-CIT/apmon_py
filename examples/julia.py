#!/usr/bin/python
"""
julia example
"""
from __future__ import print_function
import os
import time
import apmon


def main():
    task = "TestTask4"  # context['MonitorID']
    job = "TestJob4"  # context['MonitorJobID']
    ppid = os.getppid()
    cdir = os.getcwd()
    apmonUrls = ["http://lxgate35.cern.ch:40808/ApMonConf1", "http://monalisa.cacr.caltech.edu:40808/ApMonConf"]
    # apmonUrls = ["http://monalisa.cacr.caltech.edu:40808/ApMonConf"]
    # apmonUrls = []
    cdate = os.popen("date ").read()[:-1]
    print("Create apmon instance " + cdate)
    apm = apmon.ApMon(apmonUrls, apmon.Logger.ERROR)
    if not apm.initializedOK():
        print("It seems that ApMon cannot read its configuration. Setting the default destination")
        apm.setDestinations({'pcardaab.cern.ch:8884': {'sys_monitoring': 0, 'general_info': 0, 'job_monitoring': 1, 'job_interval': 300}})
    print("ApMon Initialized\n===========================")
    print(apm.getConfig()+"===========================")
    # apm = apmon.ApMon({'192.91.245.5:58884': {'job_interval':60,'sys_info':False,'general_info': False}})
    # apm.setLogLevel('DEBUG')
    apm.addJobToMonitor(ppid, cdir, task, job)
    apm.setMaxMsgRate(500)
    # print "ApmReport: Destinations: " + `apm.destinations`
    params = {}
    f = open("data.cms", "r")
    line = f.readline()
    while len(line) > 0:
        spc = line.find(" ")
        if spc == -1:
            print("ignoring", line)
            continue
        key = line[0:spc]
        val = line[spc+1:-1]
        try:
            valn = float(val)
            params[key] = valn
        except ValueError:
            params[key] = val
        line = f.readline()
    f.close()
    cnt = 0
    lastcnt = 0
    lastsec = 0
    # params = {"a": 1, "b": 3}
    print("params:", len(params), repr(params))
    while 1:
        try:
            time.sleep(1)
            # print ".",
            if int(time.time()) != lastsec:
                lastsec = int(time.time())
                print("last sec i sent", (cnt - lastcnt), "packets")
                lastcnt = cnt
            cnt += 1
            apm.sendParams(params)
            print("params:", len(params), repr(params))
        except:
            print("Before sendBgMonitoring")
            apm.sendBgMonitoring(True)
            print("After sendBgMonitoring")
            print("Now go out")
            apm.free()
            time.sleep(1)
            break

if __name__ == '__main__':
    main()
