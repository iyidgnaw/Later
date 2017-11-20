#!/bin/bash
# Author: Diyi Wang (wang.di@husky.neu.edu)
#
# Send notification based on system built-in tool.

#TODO: Make this script automatically fit the system it runs on.

at $1 <<< "notify-send '$2' '$3' && ./archive.py $2"
