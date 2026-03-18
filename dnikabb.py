#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#from __future__ import division
import math
import sys
from argparse import RawTextHelpFormatter
import argparse

parser = argparse.ArgumentParser(description="""
D'ni Qabbālā!

Default values are based on the letter-number relation:
   v/b  t   s/sh  j/g   y   k/kh  ah/ai  f/p   i/ee  e/ay  r    m
    1   2    3     4    5    6      7     8     9     10   11   12
   th  d/dh  h    o/oy  ch   w    uh/oo  ts     l     a    z    n
   13   14   15    16   17   18     19   20     21    22   23   24
    
With the --alpha option, the values are based on the alphabetic order:
    v   b   t   s   sh  j   g   y   kh  k   ah  ai  f   p   i   ee  e   ay
    1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18
    r   m   th  dh  d   h   o   oy  ch  w   uh  oo  ts  l   a   z   n  
    19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35
""", formatter_class=RawTextHelpFormatter)

parser.add_argument("dniword", help="input in Old Transliteration Standard (e.g. \"shooteejoo\")", type=str, action="store")
parser.add_argument("-a", "--alpha", help="use alphabetic order for values", action="store_true")
parser.add_argument("-v", "--verbose", help="breakdown the value assignments", action="store_true")
args = parser.parse_args()

# CONSTANTS AND FUNCTIONS

dniFontDigitsDni={"v": 1, "b": 2, "t": 3, "s": 4, "S": 5, "j": 6, "g": 7, "y": 8, "k": 9, "K":10, "a":11, "I":12, "f":13, "p":14, "i":15, "E":16, "e":17, "A":18, "r":19, "m":20, "T":21, "d":22, "D":23, "h":24, "o":25, "O":26, "c":27, "w":28, "u":29, "U":30, "x":31, "l":32, "å":33, "z":34, "n":35}

dniNumDigitsDni={"v": 1, "b": 1, "t": 2, "s": 3, "S": 3, "j": 4, "g": 4, "y": 5, "k": 6, "K": 6, "a": 7, "I": 7, "f": 8, "p": 8, "i": 9, "E": 9, "e":10, "A":10, "r":11, "m":12, "T":13, "d":14, "D":14, "h":15, "o":16, "O":16, "c":17, "w":18, "u":19, "U":19, "x":20, "l":21, "å":22, "z":23, "n":24}

def ots2dfont(dnitext):
    dfont = dnitext.lower()
    dfont = dfont.replace(u"k", u"K")
    dfont = dfont.replace(u"d", u"D")
    dfont = dfont.replace(u"ch", u"c")
    dfont = dfont.replace(u"ts", u"x")
    dfont = dfont.replace(u"Kh", u"k")
    dfont = dfont.replace(u"Dh", u"d")
    dfont = dfont.replace(u"sh", u"S")
    dfont = dfont.replace(u"th", u"T")
    dfont = dfont.replace(u"ih", u"i")
    dfont = dfont.replace(u"ay", u"A")
    dfont = dfont.replace(u"ai", u"I")
    dfont = dfont.replace(u"ee", u"E")
    dfont = dfont.replace(u"oy", u"O")
    dfont = dfont.replace(u"oo", u"U")
    dfont = dfont.replace(u"a", u"å")
    dfont = dfont.replace(u"åh", u"a")
    dfont = dfont.replace(u"eh", u"e")
    dfont = dfont.replace(u"uh", u"u")

    dfont = dfont.replace(u"åe'gurå", u"å'gura")
    dfont = dfont.replace(u"Itrus", u"Atrus")
    dfont = dfont.replace(u"åtrus", u"Atrus")
    dfont = dfont.replace(u"cånnen", u"Kånen")
    dfont = dfont.replace(u"ghen", u"gen")
    dfont = dfont.replace(u"er'xånå", u"er'Kana")
    dfont = dfont.replace(u"jålåK", u"jalaK")
    dfont = dfont.replace(u"KåDiS", u"KADiS")
    dfont = dfont.replace(u"Kemo", u"KEmo")
    dfont = dfont.replace(u"minKåtå", u"minKata")
    dfont = dfont.replace(u"såmEhn", u"sameen")
    dfont = dfont.replace(u"samEhn", u"sameen")
    dfont = dfont.replace(u"tomånå", u"tomana")
    dfont = dfont.replace(u"tomån", u"toman")
    dfont = dfont.replace(u"xogål", u"xogal")
    dfont = dfont.replace(u"whårK", u"warK")

    dfont = dfont.replace(u"re'rot", u"reh'rot")
    dfont = dfont.replace(u"reåpo", u"rehapo")
    dfont = dfont.replace(u"reapo", u"rehapo")
    dfont = dfont.replace(u"reår", u"rehar")
    dfont = dfont.replace(u"rear", u"rehar")
    dfont = dfont.replace(u"reåza", u"rehaza")
    dfont = dfont.replace(u"reazå", u"rehaza")
    dfont = dfont.replace(u"reåzå", u"rehaza")
    dfont = dfont.replace(u"reaza", u"rehaza")
    dfont = dfont.replace(u"reAvu", u"rehAvu")
    dfont = dfont.replace(u"reEbor", u"rehEbor")
    dfont = dfont.replace(u"reEK", u"rehEK")
    dfont = dfont.replace(u"reer", u"reher")
    dfont = dfont.replace(u"reev", u"rehev")
    dfont = dfont.replace(u"reoSå", u"rehoSa")
    dfont = dfont.replace(u"reoSa", u"rehoSa")
    dfont = dfont.replace(u"reUr", u"rehUr")
    dfont = dfont.replace(u"reUsåtA", u"rehUsatA")
    dfont = dfont.replace(u"reUsatA", u"rehUsatA")
    dfont = dfont.replace(u"reUxA", u"rehUxA")

    if dfont[-1] == u"å": dfont = dfont[:-1] + u"a"
    if dfont[-1] == u"i": dfont = dfont[:-1] + u"E"
    
    return dfont

# INPUT/OUTPUT

dnifont = ots2dfont(args.dniword)
dninum = 0
dniseq = []
if args.alpha:
    for i in dnifont:
        dninum = dninum + dniFontDigitsDni.get(i, 0)
        dniseq.append(dniFontDigitsDni.get(i, 0))
else:
    for i in dnifont:
        dninum = dninum + dniNumDigitsDni.get(i, 0)
        dniseq.append(dniNumDigitsDni.get(i, 0))

print("%s = %d" % (args.dniword, dninum))
if args.verbose:
    print(" %s" % ('  '.join(map(str,dnifont))))
    for i in dniseq:
        print("%2d " % (i), end='')
    print()
