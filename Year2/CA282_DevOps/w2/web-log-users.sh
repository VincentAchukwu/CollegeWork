#!/bin/sh
grep -o "user-[0-9][0-9][0-9][0-9]" access.current | sort -t: -u -k1,1
