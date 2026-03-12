#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#from __future__ import division
import math
import sys
from argparse import RawTextHelpFormatter
import argparse

parser = argparse.ArgumentParser(description="""
Converts numbers between base 10 and 25, with various formats. The default format uses brackets, e.g. "11|12|6". For the D'ni to decimal conversion, the integer part of the result can also be spelled in D'ni, as long as it is below 6 digits.

Algorithm based on: "The math behind converting from any base to any base without going through base 10" (http://is.gd/aa9xJb).

If you want to convert from D\'ni to decimal, digit the D'ni number in the format of your choice as a string, e.g.:

Default format:       dninum.py -d  '11|12|6|.|15'
Alphanumeric format:  dninum.py -ad 'BC6.F'
DniFont format:       dninum.py -fd '!@6.%'
                      (be sure to use single quotes to avoid history expansion)

If you want to convert from decimal to D'ni (with approximate fractional part), digit the decimal number as usual, e.g.:

Default format:       dninum.py -n   7181.6  (output: 11|12|6|.|15|0|0|0|0|0|0)
DniFont format:       dninum.py -fn  7181.6  (output: !@6.%000000)
Alphanumeric format:  dninum.py -an  7181.6  (output: BC6.F000000)
Text format:          dninum.py -tn  7181.6  (output: naygahfahrah naygahbreesee vahgahfah)
Text format:          dninum.py -tsn 7181.6  (output: négafara négabrísí vagafa)
""", formatter_class=RawTextHelpFormatter)

direction = parser.add_mutually_exclusive_group(required=True)
direction.add_argument("-n", "--dec", help="converts from base 10 to base 25", type=float, action="store")
direction.add_argument("-d", "--dni", help="converts from base 25 to base 10", type=str,   action="store")

format = parser.add_mutually_exclusive_group()
format.add_argument("-f", "--font",  help="use the DniFont format for digits > 9, e.g. !@6.", action="store_true")
format.add_argument("-a", "--alpha", help="use alphanumeric digits, e.g. BC6", action="store_true")
format.add_argument("-t", "--text",  help="spell the number in words (only integer part)", action="store_true")

parser.add_argument("-s", "--nts",  help="use NTS spelling", action="store_true")

args = parser.parse_args()

dniAlphaDigitsDni = {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,\
                     "A":10,"B":11,"C":12,"D":13,"E":14,"F":15,"G":16,"H":17,\
                     "I":18,"J":19,"K":20,"L":21,"M":22, "N":23,"O":24,".":25}

dniFontDigitsDni  = {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,
                     ")":10,"!":11,"@":12,"#":13,"$":14,"%":15,"^":16,"&":17,\
                     "*":18,"(":19,"[":20,"]":21,"\\":22,"{":23,"}":24,".":25}

dniAlphaDigitsDec = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E",\
                     "F","G","H","I","J","K","L","M", "N","O","."]

dniFontDigitsDec  = ["0","1","2","3","4","5","6","7","8","9",")","!","@","#","$",\
                     "%","^","&","*","(","[","]","\\","{","}","."]

dniDigitsSpellOts = ["roon","fah","bree","sehn","tor","vaht","vahgahfah","vahgahbree","vahgahsen","vahgahtor","nayvoo","naygahfah","naygahbree","naygahsen","naygahtor","heebor","heegahfah","heegahbree","heegahsen","heegahtor","rish","rigahfah","rigahbree","rigahsen","rigahtor","."]

dniDigitsSpellNts = ["rún","fa","brí","sen","tor","vat","vagafa","vagabrí","vagasen","vagator","névú","négafa","négabrí","négasen","négator","híbor","hígafa","hígabrí","hígasen","hígator","riš","rigafa","rigabrí","rigasen","rigator","."]

dniDigitsPowersOts = ["","see","rah","lahn","mel","blo"]

dniDigitsPowersNts = ["","sí","ra","lan","mel","blo"]


# FUNCTIONS

def dec2dni(dec):
    dni = []
    dec = math.fabs(dec)
    dec_i = int(dec)
    dec_d = dec - dec_i
    cont = 0

    while dec_i > 0 :         # integer part
        dni.insert(0, dec_i % 25)
        dec_i  = dec_i // 25

    # insert 25 to represent the decimal separator
    # this will help replacing the digits in a loop
    dni.insert(len(dni),25)

    while dec_d > 0 :         # fractional part
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


# INPUT/OUTPUT

if args.dec:
    resultSep = dec2dni(args.dec)
    result = []
    result_dec = []
    spell_count = 0
    spell_text = []
    for i in range(0,len(resultSep)):
        result_dec.append(resultSep[i])
        if resultSep[i] == 25:
            break
        spell_count += 1

    if args.text:
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
        else:
            print("number too long to spell in D'ni!")
    else:
        if args.font:
            for i in range(0,len(resultSep)):
                result.append(dniFontDigitsDec[resultSep[i]])
            resultStr = ''.join(map(str,result))
        elif args.alpha:
            for i in range(0,len(resultSep)):
                result.append(dniAlphaDigitsDec[resultSep[i]])
            resultStr = ''.join(map(str,result))
        else:
            for i in range(0,len(resultSep)):
                if resultSep[i] == 25: resultSep[i] = "."
            resultStr = '|'.join(map(str,resultSep))

        if resultStr.endswith("."):
            resultStr = resultStr[:-1]
        if resultStr.endswith("|"):
            resultStr = resultStr[:-1]
        print(resultStr)


elif args.dni:
    input = []

    if args.font:
        for i in args.dni:
            input.append(dniFontDigitsDni[i])
        result = dni2dec(input)
        print("%f" % (result))

    elif args.alpha:
        for i in args.dni:
            input.append(dniAlphaDigitsDni[i.upper()])
        result = dni2dec(input)
        print("%f" % (result))

    else:
        dnisep = args.dni.split("|")
        i = 0
        while i < len(dnisep):
            if dnisep[i] == ".":
                dnisep[i] = 25
            elif int(dnisep[i]) > 24:
                sys.exit("At least one digit is too big!")
            i += 1
        result = dni2dec(map(float,dnisep))
        print("%f" % (result))
