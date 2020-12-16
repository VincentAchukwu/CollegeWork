#!/bin/sh

line=1
for n in "$@";
do
	echo "$line. $n"
	line=$((line + 1))
done
