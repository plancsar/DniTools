#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
from math import floor
from datetime import datetime, timezone, timedelta
from convertdate import julian
import argparse
from argparse import RawTextHelpFormatter

parser = argparse.ArgumentParser(description="""
Prints the current D'ni date, as described in the Myst Online: Uru Live game by Cyan, Inc.
The date is given as Hahr:Vailee:Yahr (default) or Hahrtee_Fahrah:Vailee:Yahr.
The time is given as Pahrtahvo:Tahvo:Gorahn:Prorahn (default) or Gahrtahvo:Tahvo:Gorahn:Prorahn.
Algorithms based on: Middleton B., 2004 - Date Conversion Techniques For the D'ni Scholar (http://home.earthlink.net/~seizuretown/myst/conversion/D%27ni%20Calendar%20Conversion.pdf).
""", formatter_class=RawTextHelpFormatter)

parser.add_argument("-n", "--nts",       help="use the New Transliteration System for vailee", action="store_true")
parser.add_argument("-d", "--date",      help="prints the date only",                          action="store_true")
parser.add_argument("-t", "--time",      help="prints the time only",                          action="store_true")
parser.add_argument("-c", "--clock",     help="prints the time only, in decimal format",       action="store_true")
parser.add_argument("-s", "--short",     help="prints vaileetee as numbers",                   action="store_true")
parser.add_argument("-g", "--gahrtahvo", help="use gahrtahvotee instead of pahrtahvotee",      action="store_true")
parser.add_argument("-a", "--atrian",    help="use hahrtee fahrah instead of the full hahr",   action="store_true")
parser.add_argument("-j", "--julian",    help="input is in the Julian (Old) Calendar",         action="store_true")
parser.add_argument("-x", "--indate",    help="input a Gregorian/Julian date to convert [YYYY MM DD HH MM SS]", nargs="+", type=int, default=[])
parser.add_argument("-q", "--agm",       help="print in AGM script format",                    action="store_true")
parser.add_argument("-z", "--nosep",     help="like --short but with spaces for separator (handy for piping )", action="store_true")

args = parser.parse_args()

# Functions equivalents from Brett Middleton's
# "Date Conversion Techniques For the D'ni Scholar":
#    BrettM    python
#    int()  -> math.floor()
#    fix()  -> int()

dniMonthsOTS = ["Leefo", "Leebro", "Leesahn", "Leetahr", "Leevot", \
                "Leevofo", "Leevobro", "Leevosahn", "Leevotahr", "Leenovoo"]
dniMonthsNTS = ["Lífo", "Líbro", "Lísan", "Lítar", "Lívot", \
                "Lívofo", "Lívobro", "Lívosan", "Lívotar", "Línovú"]

leapSecs = { 1972: -16, 1973: -14, 1974: -13, 1975: -12, 1976: -11, \
             1977: -10, 1978:  -9, 1979:  -8, 1980:  -7, 1981:  -7, \
             1982:  -6, 1983:  -5, 1984:  -4, 1985:  -4, 1986:  -3, \
             1987:  -3, 1988:  -2, 1989:  -2, 1990:  -1, 1991:   0, \
             1992:   1, 1993:   2, 1994:   3, 1995:   4, 1996:   4, \
             1997:   5, 1998:   6, 1999:   6, 2000:   6, 2001:   6, \
             2002:   6, 2003:   6, 2004:   6, 2005:   7, 2006:   7, \
             2007:   7, 2008:   8, 2009:   8, 2010:   8, 2011:   8, \
             2012:   9, 2013:   9, 2014:   9, 2015:  10, 2016:  11, \
             2017:  11, 2018:  11, 2019:  11, 2020:  11, 2021:  11, \
             2022:  11, 2023:  11, 2024:  11, 2025:  11 }

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

# Baseline conversion date (UTC time), equivalent to 9647 Leefo 1, 00:00:00:00
#(year, mon, mday, hour, mnt, sec) = (1991, 4, 21, 16, 54, 00)

bce = 0
if args.indate:
    (year, mon, mday, hour, mnt, sec) = args.indate
    if args.julian:
        (year, mon, mday) = julian.to_gregorian(year, mon, mday)
    if (year == 1 or year == 0) and (mon == 1 and mday == 1 and hour == 0 and mnt == 0 and sec <= 16):
        bce = 2 - year
        impdate = datetime(year+bce, mon, mday, hour, mnt, sec, tzinfo=timezone.utc)
    elif year <= 0:
        impdate = datetime(1-year, mon, mday, hour, mnt, sec, tzinfo=timezone.utc)
        bce = 5
    elif year > 0:
        impdate = datetime(year, mon, mday, hour, mnt, sec, tzinfo=timezone.utc)
else:
    impdate = datetime.now(timezone.utc)

# Checking for leap seconds
if bce > 0:
    impdate = impdate - timedelta(seconds = 16)
else:
    if impdate.year < 1972:
        impdate = impdate - timedelta(seconds = 16)
    elif impdate.year > 2020:
        impdate = impdate + timedelta(seconds = 11)
    else:
        impdate = impdate + timedelta(seconds = leapSecs[year])

if bce > 2:
    year1  = 1 - impdate.year
elif bce > 0:
    year1  = impdate.year - bce
else:
    year1  = impdate.year
month1 = impdate.month
day1   = impdate.day
hour1  = impdate.hour
mnt1   = impdate.minute
sec1   = impdate.second


# Algorithm 1. Gregorian Date to Julian Day Number
if month1 < 3:
    month1 = month1 + 12
    year1 = year1 - 1

WD = day1 + int(((153 * month1) - 457) / 5) + floor(365.25 * year1) - \
     floor(0.01 * year1) + floor(0.0025 *  year1)
FD = ((hour1 * 3600) + (mnt1 * 60) + sec1) / 86400
JD = WD + FD

# Algorithm 6. Gregorian Date (Julian Day Number) to Cavernian Date
JDD = JD - 727249.704166666
AY = JDD * 0.793993705929756 + 1

# Algorithm 4. Atrian Yahr Number to Cavernian Date
# (Added the pahrtahvo calculation)
Z = floor(AY)
G = Z - 0.25
A = floor(G / 290)
C = Z - (A * 290)
Z = (AY - floor(AY)) * 78125
vailee = floor((C - 0.25) / 29) + 1
yahr = C - ((vailee - 1) * 29)
hahr = 9647 + A
gahrtahvo = floor(Z / 15625)
R = Z - (gahrtahvo * 15625)

pt = Z / 3125
pahrtahvo = floor(pt)
tahvoP = floor( (pt - pahrtahvo) * 5 )

tahvoG = floor(R / 625)
R1 = R - (tahvoG * 625)
gorahn = floor(R1 / 25)
prorahn = floor(R1 - (gorahn * 25))

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
if args.agm:
    print("%s %d, %d, and the time is %d:%02d:%02d" % \
      (vaileeName, yahr, hahr, pahrtahvo, tahvoP, gorahn))

elif args.clock:
    if args.gahrtahvo:
        gahrtahvo = gahrtahvo + tahvoG/25 + gorahn/625 + prorahn/15625
        print("%.4f" % (gahrtahvo))
    else:
        pahrtahvo = pahrtahvo + tahvoP/5 + gorahn/125 + prorahn/3125
        print("%.4f" % (pahrtahvo))

elif args.nosep:
    print( "%d %d %d  %d %02d %02d %02d" % \
      (hahr, int(vailee), yahr, pahrtahvo, tahvoP, gorahn, prorahn) )

else:
    if args.atrian:
        dniyear = atrian
    else:
        dniyear = hahr

    if args.gahrtahvo:
        dnihour = gahrtahvo
        dnimin  = tahvoG
    else:
        dnihour = pahrtahvo
        dnimin  = tahvoP

    dnitime = "%d:%02d:%02d:%02d" % (dnihour, dnimin, gorahn, prorahn)

    if args.short:
        dnidate = "%d.%d.%d" % (dniyear, int(vailee), yahr)
    else:
        dnidate = "%d %s %d" % (dniyear, vaileeName, yahr)

    if args.date:
        print(dnidate)
    elif args.time:
        print(dnitime)
    else:
        print("%s, %s" % (dnidate, dnitime))
