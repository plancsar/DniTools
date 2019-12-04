#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
from argparse import RawTextHelpFormatter
import math
import argparse
import sys

parser = argparse.ArgumentParser(description="""
Converts numbers between base 10 and 25, with various formats. The default
format uses brackets, e.g. [11|12|6]. For the D'ni to decimal conversion, 
the integer part of the result is also spelled in D'ni, as long as it is 
below 6 digits.
Algorithm based on: "The math behind converting from any base to any base
without going through base 10" (http://is.gd/aa9xJb).

If you want to convert from D\'ni to decimal, digit the D'ni number in the
format of your choice, separated by spaces, e.g.:

Default format:         dninum.py -d 11 12 6 . 15
DniFont format:         dninum.py -fd ! @ 6 . %   (BUGGED)
Alphanumeric format:    dninum.py -ad B C 6 . F

If you want to convert from decimal to D'ni (with approximate fractional part),
digit the decimal number as usual, e.g.:

Default format:         dninum.py -n 7181.6     (output: [11|12|6|.|15|0|...])
DniFont format:         dninum.py -fn 7181.6    (output: !@6.%00...)
Alphanumeric format:    dninum.py -an 7181.6    (output: BC6.F00...)
""", formatter_class=RawTextHelpFormatter)

parser.add_argument("-s", "--nts", help="use NTS spelling.", action="store_true")

format = parser.add_mutually_exclusive_group()
format.add_argument("-f", "--font", help="use the DniFont format for digits > 9, e.g. !@6.", action="store_true")
format.add_argument("-a", "--alpha", help="use alphanumeric digits, e.g. BC6", action="store_true")

direction = parser.add_mutually_exclusive_group(required=True)
direction.add_argument("-n", "--dec", help="converts from base 10 to base 25", type=float, action="store")
direction.add_argument("-d", "--dni", nargs="+", help="converts from base 25 to base 10", type=str, action="store")

args = parser.parse_args()

dniAlphaDigitsDni = {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,\
                     "A":10,"B":11,"C":12,"D":13,"E":14,"F":15,"G":16,"H":17,\
                     "I":18,"J":19,"K":20,"L":21,"M":22, "N":23,"O":24,".":25}

dniFontDigitsDni  = {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,
                     "\)":10,"!":11,"@":12,"#":13,"$":14,"%":15,"^":16,"&":17,\
                     "*":18,"\(":19,"[":20,"]":21,"\\":22,"\{":23,"\}":24,".":25}

dniAlphaDigitsDec = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E",\
                     "F","G","H","I","J","K","L","M", "N","O","."]

dniFontDigitsDec  = ["0","1","2","3","4","5","6","7","8","9",")","!","@","#","$",\
                     "%","^","&","*","(","[","]","\\","{","}","."]

dniDigitsSpellOts = ["roon","fah","bree","sehn","tor","vaht","vahgahfah","vahgahbree","vahgahsen","vahgahtor","nayvoo","naygahfah","naygahbree","naygahsen","naygahtor","heebor","heegahfah","heegahbree","heegahsen","heegahtor","rish","rigahfah","rigahbree","rigahsen","rigahtor","."]

dniDigitsSpellNts = ["rún","fa","brí","sen","tor","vat","vagafa","vagabrí","vagasen","vagator","névú","négafa","négabrí","négasen","négator","híbor","hígafa","hígabrí","hígasen","hígator","riš","rigafa","rigabrí","rigasen","rigator","."]

dniDigitsPowersOts = ["","see","rah","lahn","mel","blo"]

dniDigitsPowersNts = ["","sí","ra","lan","mel","blo"]


def dec2dni(dec):
    dni = []
    dec = math.fabs(dec)
    dec_i = int(dec)
    dec_d = dec - dec_i
    cont = 0
    while dec_i > 0 :
        dni.insert(0, dec_i % 25)
        dec_i  = dec_i // 25
    dni.insert(len(dni),25)
    while dec_d > 0 :
        dec_25 = dec_d * 25
        dec_d = dec_25 - int(dec_25)
        dni.insert(len(dni), int(dec_25))
        cont = cont + 1
        if cont > 6 :
            break

    return dni

def dni2dec(dni):
    dec = 0
    dot = 0
    for d in dni :
        if dot == 0 :
            if d == 25 :
                dot = 1
            else:
                dec = 25 * dec + d
        else:
            dec = (d / 25**dot) + dec
            dot = dot + 1

    return dec


if args.dec:
    resultB = dec2dni(args.dec)
    result = []
    result_dec = []
    spell_count = 0
    spell_text = []
    for i in range(0,len(resultB)):
        result_dec.append(resultB[i])
        if resultB[i] == 25:
            break
        spell_count += 1

    if args.font:
        for i in range(0,len(resultB)):
            result.append(dniFontDigitsDec[resultB[i]])
        print('base25: '+''.join(map(str,result)))
    elif args.alpha:
        for i in range(0,len(resultB)):
            result.append(dniAlphaDigitsDec[resultB[i]])
        print('base25: '+''.join(map(str,result)))
    else:
        for i in range(0,len(resultB)):
            if resultB[i] == 25: resultB[i] = "."
        print('base25: ['+'|'.join(map(str,resultB))+']')

    if spell_count < 7:
        for i in range(2,spell_count+2):
            if args.nts:
                if dniDigitsSpellNts[result_dec[-i]] != "rún":
                    spell_text.append(dniDigitsSpellNts[result_dec[-i]] + dniDigitsPowersNts[i-2] + " ")
            else:
                if dniDigitsSpellOts[result_dec[-i]] != "roon":
                    spell_text.append(dniDigitsSpellOts[result_dec[-i]] + dniDigitsPowersOts[i-2] + " ")

        spell_str = "".join(map(str,spell_text[::-1]))
        spell_str = spell_str.replace("rra", "ra")
        print(spell_str)


elif args.dni:
    input = []
    if args.font:
        print("This option is bugged, even if you do get a result it could be wrong!")
        for i in range(0,len(args.dni)):
            input.append(dniFontDigitsDni[args.dni[i]])
        result = dni2dec(input)
        print("base10: %f" % (result))
    elif args.alpha:
        for i in range(0,len(args.dni)):
            input.append(dniAlphaDigitsDni[args.dni[i].upper()])
        result = dni2dec(input)
        print("base10: %f" % (result))
    else:
        for i in range(0,len(args.dni)):
            if args.dni[i] == ".":
                args.dni[i] = 25
            elif int(args.dni[i]) > 24:
                sys.exit("At least one digit is too big!")
        result = dni2dec(map(float,args.dni))
        print("base10: %f" % (result))
