#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
from datetime import datetime, timezone, timedelta
from math import floor

# Functions equivalents from Brett Middleton's
# "Date Conversion Techniques For the D'ni Scholar":
#    BrettM    python
#    int()  -> math.floor()
#    fix()  -> int()

# timestamp of the HyperCard stack of the original Myst
Myst_tstamp = [1991,4,21,16,54,00]

dniMonths = ["Leefo", "Leebro", "Leesahn", "Leetahr", "Leevot", \
             "Leevofo", "Leevobro", "Leevosahn", "Leevotahr", "Leenovoo"]

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


def currtime():
    impdate = datetime.now(timezone.utc)
    return impdate.year, impdate.month, impdate.day, impdate.hour, impdate.minute, impdate.second



def jday(year, mon, mday, hour, mnt, sec):
    #for the current JD, run jday(*currtime())

    month1 = mon
    year1 = year
    day1 = mday
    hour1 = hour

    # Algorithm 1. Gregorian Date to Julian Day Number
    if month1 < 3:
        month1 = month1 + 12
        year1 = year1 - 1

    WD = day1 + int(((153 * month1) - 457) / 5) + floor(365.25 * year1) - \
         floor(0.01 * year1) + floor(0.0025 *  year1)
    FD = ((hour1 * 3600) + (mnt * 60) + sec) / 86400
    JD = WD + FD + 1721118.5
    
    return JD



def dnitime(year, mon, mday, hour, mnt, sec, textmonth=False, oldhour=False, shortyear=False):
    #for the current D'ni time, run dnitime(*currtime(), textmonth=..., shortyear=...)

    impdate = datetime(year, mon, mday, hour, mnt, sec, tzinfo=timezone.utc)
    
    if impdate.year < 1972:
        impdate = impdate - timedelta(seconds = 16)
    elif impdate.year > 2020:
        impdate = impdate + timedelta(seconds = 11)
    else:
        impdate = impdate + timedelta(seconds = leapSecs[year])

    month1 = impdate.month
    year1  = impdate.year
    day1   = impdate.day
    hour1  = impdate.hour
    min1   = impdate.minute
    sec1   = impdate.second

    # Algorithm 1. Gregorian Date to Julian Day Number
    if month1 < 3:
        month1 = month1 + 12
        year1 = year1 - 1

    WD = day1 + int(((153 * month1) - 457) / 5) + floor(365.25 * year1) - \
         floor(0.01 * year1) + floor(0.0025 *  year1)
    FD = ((hour1 * 3600) + (min1 * 60) + sec1) / 86400
    JD = WD + FD

    # Algorithm 6. Gregorian Date (Julian Day Number) to Cavernian Date
    JDD = JD  - 727249.704166666
    AY  = JDD * 0.793993705929756 + 1

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

    # Pahrtahvo or gahrtahvo?
    if oldhour:
        dnihour = gahrtahvo
        dnimin  = tahvoG
    else:
        dnihour = pahrtahvo
        dnimin  = tahvoP

    # Should the month names be used?
    vaileeName = dniMonths[int(vailee)-1]
    if textmonth:
        dnimonth = vaileeName
    else:
        dnimonth = vailee

    # Should the journal short year be used?
    if shortyear:
        dniyear = atrian
    else:
        dniyear = hahr

    return [dniyear, dnimonth, yahr, dnihour, dnimin, gorahn, prorahn]
