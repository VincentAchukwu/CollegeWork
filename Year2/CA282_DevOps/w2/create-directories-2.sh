#!/bin/sh
n=$1

#for i in (seq $n);
#do
#	printf "dir.%06d" $i | mkdir
#done

#mkdir $(printf "dir.%06d" $(seq $n))
#seq $n | sed 's/^/dir./' | xargs mkdir
for i in $(seq $n);
do
	mkdir $(printf "dir.%06d" $i)
done
