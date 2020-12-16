#!/bin/sh

n=$1
while [ $n -ne 1 ];
do
	echo $n
	if [ $(($n%2)) -eq 0 ];
	then
		n=$((n/2))
	else
		n=$((n*3+1))
	fi
done
echo $n
