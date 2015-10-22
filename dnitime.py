#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import division
import time
import math
import argparse
from argparse import RawTextHelpFormatter

parser = argparse.ArgumentParser(description="""
Prints the current D'ni date in extended format, and the pahrtahvo as it appears
on the clock in the Neighborhoods in the Myst Online: Uru Live game.
Algorithms based on
Middleton B., 2004 - Date Conversion Techniques For the D'ni Scholar
(http://home.earthlink.net/~seizuretown/myst/conversion/D%27ni%20Calendar%20Conversion.pdf).
""", formatter_class=RawTextHelpFormatter)

parser.add_argument("-n", "--nts", help="use the New Transliteration System for \
vailee", action="store_true")
parser.add_argument("-d", "--date", help="""prints hahr, vailee, yahr in the format
'Ha-Va-Ya', with vailee as a number""", action="store_true")
parser.add_argument("-t", "--time", help="""prints gahrtahvo, tahvo, gorahn, prorahn
in the format 'Ga:Ta:Go:Pr'""", action="store_true")
parser.add_argument("-p", "--pahrtahvo", help="prints just the pahrtahvo", \
action="store_true")
parser.add_argument("-a", "--atrian", help="""prints the current D'ni date in \
extended format,
using hahrtee fahrah instead of the full hahr""", action="store_true")
args = parser.parse_args()

# Functions equivalents from Brett Middleton's
# "Date Conversion Techniques For the D'ni Scholar":
#    BrettM    python
#    int()  -> math.floor()
#    fix()  -> int()

dniMonthsOTS = ["Leefo","Leebro","Leesahn","Leetahr","Leevot","Leevofo",\
                "Leevobro","Leevosahn","Leevotahr","Leenovoo"]
dniMonthsNTS = ["Lífo","Líbro","Lísan","Lítar","Lívot","Lívofo","Lívobro",\
                "Lívosan","Lívotar","Línovú"]

# Prorahn                          ~ 1.39 seconds
# Gorahn           25 prorahn     ~ 34.8  seconds
# Tahvo            25 gorahn      ~ 14.5  minutes
# Gahrtahvo        25 tahvo        ~ 6.05 hours
# Yahr              5 gahrtahvo    ~ 1.26 days
# Vailee           29 yahr         ~ 1    month
# Hahr             10 vailee       ~ 1    year
# Hahrtee fahrah  625 hahr         ~ 6.25 centuries
# 
#  1   Leefo       April 21 - May 27
#  2   Leebro      May 28 - July 3
#  3   Leesahn     July 3 - August 8
#  4   Leetar      August 9 - September 14
#  5   Leevot      September 14 - October 20
#  6   Leevofo     October 21 - November 26
#  7   Leevobro    November 26 - January 1
#  8   Leevosahn   January 2 - February 7
#  9   Leevotar    February 7 - March 15
# 10   Leenovoo    March 16 - April 21

(year, mon, mday, hour, min, sec, wday, yday, isdst) = time.gmtime()

# Baseline conversion date (UTC time), equivalent to 9654 Leefo 1, 00:00:00:00
#(year, mon, mday, hour, min, sec) = (1998, 4, 21, 10, 35, 18)

month1 = mon
year1 = year
day1 = mday

# Adjusting for Mountain Time
hour1 = hour - 8
if hour < 8:
	hour1 = hour1 + 24
	day1 = mday - 1

# Algorithm 1. Gregorian Date to Julian Day Number
if month1 < 3:
	month1 = month1 + 12
	year1 = year1 - 1

WD = day1 + int(((153 * month1) - 457) / 5) + math.floor(365.25 * year1) - \
     math.floor(0.01 * year1) + math.floor(0.0025 *  year1)
FD = ((hour1 * 3600) + (min * 60) + sec) / 86400
JD = WD + FD;

# Algorithm 6. Gregorian Date (Julian Day Number) to Cavernian Date
JDD = JD - 729806.107847222
AY = JDD * 0.79399371150033 + 1

# Algorithm 4. Atrian Yahr Number to Cavernian Date
Z = math.floor(AY)
G = Z - 0.25
A = math.floor(G / 290)
C = Z - (A * 290)
Z = (AY - math.floor(AY)) * 78125
vailee = math.floor((C - 0.25) / 29) + 1
yahr = C - ((vailee - 1) * 29)
hahr = 9654 + A
gahrtahvo = int(Z / 15625)
pt = Z - (gahrtahvo * 15625)
pahrtahvo = int(Z * 10 / 3125) / 10
R = Z - (gahrtahvo * 15625)
tahvo = int(R / 625)
R1 = R - (tahvo * 625)
gorahn = int(R1 / 25)
prorahn = int(R1 - (gorahn * 25))

# (Modified) Algorithm 3. Cavernian Date to Atrian Yahr Number
# Here we use the beginning of the current D'ni century, 9375 DE
WY = yahr + ((vailee - 1) * 29) + ((hahr - 9375) * 290)
FY = ((gahrtahvo * 15625) + (tahvo * 625) + (gorahn * 25) + prorahn) / 78125
atrian = int((WY + FY) / 290)

# Display options for vailee names
if args.nts:
	vaileeName = dniMonthsNTS[int(vailee)-1]
else:
	vaileeName = dniMonthsOTS[int(vailee)-1]

# Time format display
if args.date:
	print "%02d-%02d-%02d" % (hahr, int(vailee), yahr)
elif args.time:
	print "%02d:%02d:%02d:%02d" % (gahrtahvo, tahvo, gorahn, prorahn)
elif args.pahrtahvo:
	print "%.1f" % (pahrtahvo)
elif args.atrian:
	print "%02d %s %02d, %02d:%02d:%02d:%02d [%.1f]" % (atrian, vaileeName, yahr, \
	       gahrtahvo, tahvo, gorahn, prorahn, pahrtahvo)
else:
	print "%02d %s %02d, %02d:%02d:%02d:%02d [%.1f]" % (hahr, vaileeName, yahr, \
	       gahrtahvo, tahvo, gorahn, prorahn, pahrtahvo)
