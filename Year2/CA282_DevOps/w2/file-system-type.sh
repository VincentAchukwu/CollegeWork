#!/bin/sh

for file in "$@";
do
	if test -f $file;
	then
		echo "$file file"
	elif test -d $file;
	then
		echo "$file directory"
	else
		echo "$file does not exist"
	fi
done
