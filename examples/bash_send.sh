#!/bin/sh

max=$1
echo "sending to $max"
i=0
while [ $i -lt $max ] ; do
	./mlmetric -dest 137.138.30.95:18884 -cluster SimpleCluster -node SimpleNode -param cucu -value $i
	i=$((i+1))
done
