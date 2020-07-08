#!/bin/sh

max=${1:-10}
echo "sending from 0 to $max"
i=0
while [ $i -lt $max ] ; do
	echo "  sending $i"
	./mlmetric -dest aliendb10.cern.ch:8884 -cluster SimpleCluster -node SimpleNode -param cucu -value $i
	sleep 1
	i=$((i+1))
done
