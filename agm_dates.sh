#!/bin/bash

usage()
{
cat << EOF

Usage:

$0 [YEAR]

This script print the dates of the All Guilds Meetings for the current year, and the equivalent D'ni dates.

If a year is given, it will calculate the dates for that year.

OPTIONS:
   -h    show this message

EOF
}

OPTIND=1
while getopts "h" opt; do
        case "$opt" in
                "h")  usage; exit 1;;
                "?")  usage; exit;;
        esac
done
shift $(expr $OPTIND - 1)


for i in {1..12}; do
	for j in {1..7}; do
		if [ -z $1 ]
			then date=$(date -d "$i/1 + $j day" +"%w %F")
			else date=$(date -d "$1/$i/1 + $j day" +"%w %F")
		fi

		# day of week (1..7); 1 is Monday
		if [ ${date:0:1} -eq 6 ] ; then
			year=${date:2:4}  ; year=$(echo $year | sed 's/^0*//')
			month=${date:7:2} ; month=$(echo $month | sed 's/^0*//')

			let agm=$year-2019
			let agm=$agm*12
			let agm=$agm+$month+104
			if [ $agm -lt 5 ] ; then let agm=$agm+1 ; fi

			myst=0 ; note=""
			if [ $month -eq 8 ] ; then myst=7 ; note="(Mysterium!)" ; fi

			if [ $agm -eq 5 ] && [ $month -eq 8 ]
				then unset agm ; note="(This AGM was skipped)"
			elif [ $agm -lt 1 ]
				then continue
			fi

			if [ $month -gt 3 ] && [ $month -lt 11 ]
				then daym=19 ; else daym=20
			fi

			let sat=${date:11:2}+$myst
			sat=$(echo $sat | sed 's/^0*//')

			if [ ${date:10:2} -gt 7 ]; then let sat=$sat-7 ; fi

			printf "%4d-%02d-%02d #%d %s\tShorah, and welcome to the %dth All Guilds Meeting!\nIn the D'ni calendar today is " "$year" "$month" "$sat" "$agm" "$note" "$agm"

			echo "$(dnitime.py -q -x $year $month $sat $daym 0 0)"
		fi
	done
done
