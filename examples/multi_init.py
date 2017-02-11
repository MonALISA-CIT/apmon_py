"""
# This example shows how you cand recreate multiple times the ApMon object
"""
from __future__ import print_function
import apmon
import time


def doStuff(i):
    print("start", i)
    apm = apmon.ApMon('http://monalisa2.cern.ch/~catac/apmon/destinations.conf')
    apm.sendParameter('cluster', 'node', 'param', 34+i)
    time.sleep(0.01)
    apm.sendParameter('cluster', 'node', 'param', -34+i)
    time.sleep(0.06)
    apm.sendParameter('cluster', 'node', 'param', i)
    # You absolutely have to call this function here!
    apm.free()
    print("end", i)


def main():
    """ main function """
    for i in list(range(1, 5)):
        doStuff(i)
    for i in range(1, 10):
        a = list(range(1, i))
        del a

if __name__ == '__main__':
    main()
