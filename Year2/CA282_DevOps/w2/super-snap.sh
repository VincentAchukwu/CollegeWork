#!/bin/sh


read word1
read word2
while [ $word1 != $word2 ];
do
	echo $word1 >> file.txt
	word1=$word2
	read word2
	grep -q $word2 file.txt
	if [ $? -eq 0 ];
	then
		break
	fi
done
echo $word2

