#!/bin/sh

read word1
read word2
while [ $word1 != $word2 ];
do
	word1=$word2
	read word2
done
echo $word1
