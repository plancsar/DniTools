#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
import time
import math
import argparse
from argparse import RawTextHelpFormatter

parser = argparse.ArgumentParser(description="""
Prints the current D'ni date, as described in the Myst Online: Uru Live game by Cyan, Inc.
The date is given as Hahr:Vailee:Yahr (default) or Hahrtee_Fahrah:Vailee:Yahr.
The time is given as Gahrtahvo:Tahvo:Gorahn:Prorahn (default) or Pahrtahvo:Tahvo:Gorahn:Prorahn.
Algorithms based on: Middleton B., 2004 - Date Conversion Techniques For the D'ni Scholar (http://home.earthlink.net/~seizuretown/myst/conversion/D%27ni%20Calendar%20Conversion.pdf).
""", formatter_class=RawTextHelpFormatter)

parser.add_argument("-n", "--nts", help="use the New Transliteration System for vailee", action="store_true")
parser.add_argument("-d", "--date", help="""prints the date only""", action="store_true")
parser.add_argument("-t", "--time", help="""prints the time only""", action="store_true")
parser.add_argument("-p", "--pahrtahvo", help="""use pahrtahvotee instead of gahrtahvotee and tahvotee""", action="store_true")
parser.add_argument("-a", "--atrian", help="""use hahrtee fahrah instead of the full hahr""", action="store_true")

parser.add_argument("-x", "--indate", nargs="+", type=int, default=[], help="input \
a Gregorian date to convert [YYYY MM DD HH MM SS]")

args = parser.parse_args()

# Functions equivalents from Brett Middleton's
# "Date Conversion Techniques For the D'ni Scholar":
#    BrettM    python
#    int()  -> math.floor()
#    fix()  -> int()

dniMonthsOTS = ["Leefo","Leebro","Leesahn","Leetahr","Leevot","Leevofo","Leevobro","Leevosahn","Leevotahr","Leenovoo"]
dniMonthsNTS = ["Lífo","Líbro","Lísan","Lítar","Lívot","Lívofo","Lívobro","Lívosan","Lívotar","Línovú"]

# Prorahn                          ~ 1.39 seconds
# Gorahn           25 prorahn     ~ 34.8  seconds
# Tahvo            25 gorahn      ~ 14.5  minutes
# Pahrtahvo         5 tahvo        ~ 1.22 hours
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

if args.indate:
    (year, mon, mday, hour, min) = args.indate
    sec = 0

# Baseline conversion date (UTC time), equivalent to 9647 Leefo 1, 00:00:00:00
#(year, mon, mday, hour, min, sec) = (1991, 4, 21, 16, 54, 00)

month1 = mon
year1 = year
day1 = mday
hour1 = hour

# Algorithm 1. Gregorian Date to Julian Day Number
if month1 < 3:
    month1 = month1 + 12
    year1 = year1 - 1

WD = day1 + int(((153 * month1) - 457) / 5) + math.floor(365.25 * year1) - math.floor(0.01 * year1) + math.floor(0.0025 *  year1)
FD = ((hour1 * 3600) + (min * 60) + sec) / 86400
JD = WD + FD

# Algorithm 6. Gregorian Date (Julian Day Number) to Cavernian Date
JDD = JD - 727249.704166666
AY = JDD * 0.793993705929756 + 1

# Algorithm 4. Atrian Yahr Number to Cavernian Date
# (Added the pahrtahvo calculation)
Z = math.floor(AY)
G = Z - 0.25
A = math.floor(G / 290)
C = Z - (A * 290)
Z = (AY - math.floor(AY)) * 78125
vailee = math.floor((C - 0.25) / 29) + 1
yahr = C - ((vailee - 1) * 29)
hahr = 9647 + A
gahrtahvo = math.floor(Z / 15625)
R = Z - (gahrtahvo * 15625)

pt = Z / 3125
pahrtahvo = math.floor(pt)
tahvoP = math.floor( (pt - pahrtahvo) * 5 )

tahvoG = math.floor(R / 625)
R1 = R - (tahvoG * 625)
gorahn = math.floor(R1 / 25)
prorahn = math.floor(R1 - (gorahn * 25))

# (Modified) Algorithm 3. Cavernian Date to Atrian Yahr Number
# We determine the current (positive) D'ni century
dnicent = 0
while (hahr - dnicent) >= 625 and hahr > 0:
    dnicent += 625
WY = yahr + ((vailee - 1) * 29) + ((hahr - dnicent) * 290)
FY = ((gahrtahvo * 15625) + (tahvoG * 625) + (gorahn * 25) + prorahn) / 78125
atrian = int((int(WY + FY) - 0.25) / 290)

# Display options for vailee names
if args.nts:
    vaileeName = dniMonthsNTS[int(vailee)-1]
else:
    vaileeName = dniMonthsOTS[int(vailee)-1]

# Time format display
if args.date:
    if args.atrian:
        print("%d.%d.%d" % (atrian, int(vailee), yahr))
    else:
        print("%d.%d.%d" % (hahr,   int(vailee), yahr))

elif args.time:
    if args.pahrtahvo:
        print("%d:%02d:%02d:%02d" % (pahrtahvo, tahvoP, gorahn, prorahn))
    else:
        print("%d:%02d:%02d:%02d" % (gahrtahvo, tahvoG, gorahn, prorahn))

else:
    if args.atrian:
        if args.pahrtahvo:
            print("%d %s %d, %d:%02d:%02d:%02d" % (atrian, vaileeName, yahr, pahrtahvo, tahvoP, gorahn, prorahn))
        else:
            print("%d %s %d, %d:%02d:%02d:%02d" % (atrian, vaileeName, yahr, gahrtahvo, tahvoG, gorahn, prorahn))
    else:
        if args.pahrtahvo:
            print("%d %s %d, %d:%02d:%02d:%02d" % (hahr,   vaileeName, yahr, pahrtahvo, tahvoP, gorahn, prorahn))
        else:
            print("%d %s %d, %d:%02d:%02d:%02d" % (hahr,   vaileeName, yahr, gahrtahvo, tahvoG, gorahn, prorahn))
