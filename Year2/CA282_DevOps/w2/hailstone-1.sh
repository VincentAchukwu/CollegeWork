#!/bin/sh
read n
for i in $(seq 20);
do
	echo $n
	if [ $(($n%2)) -eq 0 ];
	then
		n=$((n/2))
	else
		n=$((n*3+1))
	fi
done
