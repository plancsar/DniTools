#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
from math import floor, ceil
from datetime import datetime, timezone, timedelta
import time
import pytz
import argparse
from argparse import RawTextHelpFormatter

parser = argparse.ArgumentParser(description="""
Converts a D'ni date, as described in the Myst Online: Uru Live game by Cyan, Inc., to a Gregorian date.
The date can be given as Hahr:Vailee:Yahr (default) or Hahrtee_Fahrah:Vailee:Yahr.
The time can be given as Pahrtahvo:Tahvo:Gorahn:Prorahn (default) or Gahrtahvo:Tahvo:Gorahn:Prorahn.
Algorithms based on: Middleton B., 2004 - Date Conversion Techniques For the D'ni Scholar (http://home.earthlink.net/~seizuretown/myst/conversion/D%27ni%20Calendar%20Conversion.pdf).
""", formatter_class=RawTextHelpFormatter)

parser.add_argument("-d", "--date", help="""prints the date only""", action="store_true")
parser.add_argument("-t", "--time", help="""prints the time only""", action="store_true")
parser.add_argument("-g", "--gahrtahvo", help="""input use gahrtahvotee instead of pahrtahvotee""", action="store_true")
parser.add_argument("-a", "--atrian", help="""input use hahrtee fahrah instead of the full hahr""", action="store_true")
parser.add_argument("indate", nargs="+", type=int, action="store", help="input a D'ni date to convert [HHHH VV YY PT T GG PR]")

args = parser.parse_args()

# Functions equivalents from Brett Middleton's
# "Date Conversion Techniques For the D'ni Scholar":
#    BrettM    python
#    int()  -> floor()
#    fix()  -> int()

leapSecs = { 1972: -16, 1973: -14, 1974: -13, 1975: -12, 1976: -11, \
             1977: -10, 1978:  -9, 1979:  -8, 1980:  -7, 1981:  -7, \
             1982:  -6, 1983:  -5, 1984:  -4, 1985:  -4, 1986:  -3, \
             1987:  -3, 1988:  -2, 1989:  -2, 1990:  -1, 1991:   0, \
             1992:   1, 1993:   2, 1994:   3, 1995:   4, 1996:   4, \
             1997:   5, 1998:   6, 1999:   6, 2000:   6, 2001:   6, \
             2002:   6, 2003:   6, 2004:   6, 2005:   7, 2006:   7, \
             2007:   7, 2008:   8, 2009:   8, 2010:   8, 2011:   8, \
             2012:   9, 2013:   9, 2014:   9, 2015:  10, 2016:  11, \
             2017:  11, 2018:  11, 2019:  11, 2020:  11 }

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
#(year, mon, mday, hour, min, sec) = (1991, 4, 21, 16, 54, 00)

(hahr, vailee, yahr, pahrtahvo, tahvoP, gorahn, prorahn) = args.indate


# Algorithm 3. Cavernian Date to Atrian Yahr Number
if args.atrian:
    atrian = hahr
    WY = yahr + ((vailee - 1) * 29) + (atrian * 290)
else:
    WY = yahr + ((vailee - 1) * 29) + ((hahr - 9647) * 290)

if args.gahrtahvo:
    gahrtahvo = pahrtahvo
    tahvoG = tahvoP
    FY = ((gahrtahvo * 15625) + (tahvoG * 625) + (gorahn * 25) + prorahn) / 78125
else:
    FY = ((pahrtahvo * 3125)  + (tahvoP * 625) + (gorahn * 25) + prorahn) / 78125

AY = WY + FY

# Algorithm 5. Atrian Yahr Number to Julian Day Number
AYD = AY - 1.0
JDD = AYD * 1.25945582758621
JD  = JDD + 727249.704166666

# Algorithm 2. Julian Day Number to Gregorian Date
Z = floor(JD)
G = Z - 0.25
A = floor(G / 36524.25)
B = A - (0.25 * A)
year = floor((G + B) / 365.25)
C = Z + B - floor(365.25 * year)
month = int(((5 * C) + 456) / 153)
day = C - int(((153 * month) - 457) / 5)

if month > 12:
    year = year + 1
    month = month - 12

# bce = "CE"
# if year < 1:
#     year = 1 - year
#     bce = "BCE"

Z = (JD - floor(JD)) * 86400
hour = int(Z / 3600)
R = Z - (hour * 3600)
minute = int(R / 60)
second = R - (minute * 60)


day = floor(day + 0.75)  # not sure why, but this fixes a rounding error
second = ceil(second)
if second > 59: second = second - 1

outdate_utc = datetime(year, month, day, hour, minute, second, tzinfo=timezone.utc)

# Checking for leap seconds
if outdate_utc.year < 1972:
    outdate_utc = outdate_utc + timedelta(seconds = 16)
elif outdate_utc.year > 2020:
    outdate_utc = outdate_utc - timedelta(seconds = 11)
else:
    outdate_utc = outdate_utc - timedelta(seconds = leapSecs[year])

outdate_ki = outdate_utc.astimezone(pytz.timezone('America/Denver'))

# Time format displays
print(outdate_utc.strftime('%B %d, %Y, %H:%M:%S %Z'))
print(outdate_ki.strftime('%B %d, %Y, %H:%M:%S %Z'))
# print(outdate_utc.strftime('%Y %m %d %H %M %S'))
