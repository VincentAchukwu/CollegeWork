#!/bin/sh

#both do the same thing..
#grep -E -o ".{0,5}.computing.dcu.ie" access.current | grep -v "stein" | grep -Eo '^.{0,5}'| sort -t: -u -k1,1
grep -Eo '.{0,5}.computing.dcu.ie' access.current | grep -v 'stein' | grep -Eo '^.{0,5}'| sort -u
