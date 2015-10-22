#!/bin/bash
# Use the terminal window as a rudimentary D'ni clock
# Exit with ctrl-c

printf '\e[8;3;40t'      # resize the terminal window to 3 lines x 40 columns
printf '\e[3;0;0t'       # move the window to the top/left corner of the display
printf '\033[2J'         # clear screen
while [ 1 ]; do
	printf '\033[0;0H\n'  # move to first line
	dnitime.py -n
	sleep 1
done
