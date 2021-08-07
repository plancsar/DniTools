#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
from argparse import RawTextHelpFormatter
from datetime import datetime,timedelta,tzinfo
from pytz import timezone
from tzlocal import get_localzone

parser = argparse.ArgumentParser(description="""
Prints the next four Eder Gira sunsets and sunrises, in KI time.
""", formatter_class=RawTextHelpFormatter)

parser.add_argument("-l", "--local", help="print the dates in your local time", action="store_true")
args = parser.parse_args()

#          Negilahn   Dereno     Payiferen  Tetsonot
tstamps = [946713600, 946718065, 946720085, 946730009]
pdtimes = []

for ts in tstamps:
    startdate = datetime.fromtimestamp(ts, tz=timezone('UTC') )

    portal = startdate

    while True:
        portal += timedelta(hours=15.718056)
        if portal > datetime.now(timezone('UTC')):
            break
            
    if ts != 946730009:
        portal -= timedelta(hours=15.718056)

    portal += timedelta(hours=2, minutes=-14, seconds=16)

    if args.local:
        portal1 = portal.astimezone(get_localzone())
    else:
        portal1 = portal.astimezone(timezone('America/Denver'))

    pdtimes.append( str(format(portal1.month, "02d")) +"/"+ str(format(portal1.day, "02d")) +" "+ str(format(portal1.hour, "02d")) +":"+ str(format(portal1.minute, "02d")) )
    
    portal2 = portal1 + timedelta(hours=15.718056)
    pdtimes.append( str(format(portal2.month, "02d")) +"/"+ str(format(portal2.day, "02d")) +" "+ str(format(portal2.hour, "02d")) +":"+ str(format(portal2.minute, "02d")) )
    
    portal3 = portal2 + timedelta(hours=15.718056)
    pdtimes.append( str(format(portal1.month, "02d")) +"/"+ str(format(portal3.day, "02d")) +" "+ str(format(portal3.hour, "02d")) +":"+ str(format(portal3.minute, "02d")) )
    
    portal4 = portal3 + timedelta(hours=15.718056)
    pdtimes.append( str(format(portal1.month, "02d")) +"/"+ str(format(portal4.day, "02d")) +" "+ str(format(portal4.hour, "02d")) +":"+ str(format(portal4.minute, "02d")) )


print("Actual portal times may be a few minutes early or late.\n\nNegilahn ↑\tDereno ↓   \tPayiferen ↓\tTetsonot ↑")

for x in range(0, 4):
    print("%s\t%s\t%s\t%s" % ( pdtimes[x], pdtimes[x+4], pdtimes[x+8], pdtimes[x+12] ) )


# Timestamp: 2000-01-01T08:00:00Z
startdate = datetime.fromtimestamp(946713600, tz=timezone('UTC') )


sunrise = startdate

while True:
    sunrise += timedelta(hours=10)
    if sunrise > datetime.now(timezone('UTC')):
        break

sunrise -= timedelta(hours=15.718056)
sunrise += timedelta(hours=6, minutes=6)

if args.local:
    sunrise1 = sunrise.astimezone(get_localzone())
else:
    sunrise1 = sunrise.astimezone(timezone('America/Denver'))

sunset = sunrise + timedelta(hours=5, minutes=48)

if sunrise < datetime.now(timezone('UTC')):
    phase = "day"
else:
    phase = "night"

if args.local:
    sunset1 = sunset.astimezone(get_localzone())
else:
    sunset1 = sunset.astimezone(timezone('America/Denver'))


print("\nEder Gira (it's %s now)\nSunrises\tSunsets" % phase)
print("%02d/%02d %02d:%02d\t%02d/%02d %02d:%02d" % (sunrise1.month, sunrise1.day, sunrise1.hour, sunrise1.minute, sunset1.month, sunset1.day, sunset1.hour, sunset1.minute))
sunrise1 += timedelta(hours=10)
sunset1  += timedelta(hours=10)
print("%02d/%02d %02d:%02d\t%02d/%02d %02d:%02d" % (sunrise1.month, sunrise1.day, sunrise1.hour, sunrise1.minute, sunset1.month, sunset1.day, sunset1.hour, sunset1.minute))
sunrise1 += timedelta(hours=10)
sunset1  += timedelta(hours=10)
print("%02d/%02d %02d:%02d\t%02d/%02d %02d:%02d" % (sunrise1.month, sunrise1.day, sunrise1.hour, sunrise1.minute, sunset1.month, sunset1.day, sunset1.hour, sunset1.minute))
sunrise1 += timedelta(hours=10)
sunset1  += timedelta(hours=10)
print("%02d/%02d %02d:%02d\t%02d/%02d %02d:%02d" % (sunrise1.month, sunrise1.day, sunrise1.hour, sunrise1.minute, sunset1.month, sunset1.day, sunset1.hour, sunset1.minute))

if args.local:
    print("\nTimes are in your local time.")
else:
    print("\nTimes are in KI time.")
