#!/bin/bash

usage()
{
cat << EOF

Usage:

$0 [YEAR]

This script print the dates of the All Guilds Meetings for the current year, and the equivalent D’ni dates (calculated using dnitime.py). If a year is given, it will calculate the dates for that year.

    In the D'ni calendar it's Leevosahn 2, 9681, and the time is 19:00:21.

When using the -m parameter, the script will instead list the D’ni dates for the beginning and endings of the months.

    Jan: Leevobro 29 - Leevosahn 24.

OPTIONS:
   -h    show this message
   -m    show D’ni boundaries for months

EOF
}

MONTHS=false
while getopts ":hm" opt; do
        case "$opt" in
                "h")  usage; exit 1;;
      	        "m")  MONTHS=true;;
                "?")  usage; exit;;
        esac
done
shift $(expr $OPTIND - 1)


if [[ $MONTHS == true ]]; then
	if [ -z $1 ] ; then year=$(date +%Y) ; else year=$1 ; fi
	echo "Jan: $(dnitime.py -dx $year  1 1 7 0 1 | cut -c 6-) - $(dnitime.py -dx $year  1 31 6 59 59 | cut -c 6-)."
	echo "Feb: $(dnitime.py -dx $year  2 1 7 0 1 | cut -c 6-) - $(dnitime.py -dx $year  2 28 6 59 59 | cut -c 6-)."
	echo "Mar: $(dnitime.py -dx $year  3 1 7 0 1 | cut -c 6-) - $(dnitime.py -dx $year  3 31 5 59 59 | cut -c 6-)."
	echo "Apr: $(dnitime.py -dx $year  4 1 6 0 1 | cut -c 6-) - $(dnitime.py -dx $year  4 30 5 59 59)."
	echo "May: $(dnitime.py -dx $year  5 1 6 0 1 | cut -c 6-) - $(dnitime.py -dx $year  5 31 5 59 59 | cut -c 6-)."
	echo "Jun: $(dnitime.py -dx $year  6 1 6 0 1 | cut -c 6-) - $(dnitime.py -dx $year  6 30 5 59 59 | cut -c 6-)."
	echo "Jul: $(dnitime.py -dx $year  7 1 6 0 1 | cut -c 6-) - $(dnitime.py -dx $year  7 31 5 59 59 | cut -c 6-)."
	echo "Aug: $(dnitime.py -dx $year  8 1 6 0 1 | cut -c 6-) - $(dnitime.py -dx $year  8 31 5 59 59 | cut -c 6-)."
	echo "Sep: $(dnitime.py -dx $year  9 1 6 0 1 | cut -c 6-) - $(dnitime.py -dx $year  9 30 5 59 59 | cut -c 6-)."
	echo "Oct: $(dnitime.py -dx $year 10 1 6 0 1 | cut -c 6-) - $(dnitime.py -dx $year 10 31 6 59 59 | cut -c 6-)."
	echo "Nov: $(dnitime.py -dx $year 11 1 7 0 1 | cut -c 6-) - $(dnitime.py -dx $year 11 30 6 59 59 | cut -c 6-)."
	echo "Dec: $(dnitime.py -dx $year 12 1 7 0 1 | cut -c 6-) - $(dnitime.py -dx $year 12 31 6 59 59 | cut -c 6-)."
else
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

				if [ $month -gt 3 ] && [ $month -lt 12 ]
					then daym=19 ; else daym=20
				fi

				let sat=${date:11:2}+$myst
				sat=$(echo $sat | sed 's/^0*//')

				if [ ${date:10:2} -gt 7 ]; then let sat=$sat-7 ; fi

				printf "%4d-%02d-%02d #%d %s In the D'ni calendar it's " "$year" "$month" "$sat" "$agm"
				echo "$(dnitime.py -q -x $year $month $sat $daym 0 0)."
			fi
		done
	done
fi
