#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#from __future__ import division
import math
import sys

dniFontDigitsDni  = {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,
                     ")":10,"!":11,"@":12,"#":13,"$":14,"%":15,"^":16,"&":17,\
                     "*":18,"(":19,"[":20,"]":21,"\\":22,"{":23,"}":24,".":25}

dniFontDigitsDec  = ["0","1","2","3","4","5","6","7","8","9",")","!","@","#","$",\
                     "%","^","&","*","(","[","]","\\","{","}","."]

dniDigitsSpellOts = ["roon","fah","bree","sehn","tor","vaht","vahgahfah","vahgahbree","vahgahsen","vahgahtor","nayvoo","naygahfah","naygahbree","naygahsen","naygahtor","heebor","heegahfah","heegahbree","heegahsen","heegahtor","rish","rigahfah","rigahbree","rigahsen","rigahtor","."]

dniDigitsSpellNts = ["rún","fa","brí","sen","tor","vat","vagafa","vagabrí","vagasen","vagator","névú","négafa","négabrí","négasen","négator","híbor","hígafa","hígabrí","hígasen","hígator","riš","rigafa","rigabrí","rigasen","rigator","."]

dniDigitsPowersOts = ["","see","rah","lahn","mel","blo"]

dniDigitsPowersNts = ["","sí","ra","lan","mel","blo"]



def dninum(dec, spell=False):
    resultB = []
    dec = math.fabs(dec)
    dec_i = int(dec)
    dec_d = dec - dec_i
    cont = 0
    while dec_i > 0 :
        resultB.insert(0, dec_i % 25)
        dec_i  = dec_i // 25
    resultB.insert(len(resultB),25)
    while dec_d > 0 :
        dec_25 = dec_d * 25
        dec_d = dec_25 - int(dec_25)
        resultB.insert(len(resultB), int(dec_25))
        cont = cont + 1
        if cont > 6 :
            break

    result     = []
    result_dec = []

    if spell == False:
        for i in range(0,len(resultB)):
            result.append(dniFontDigitsDec[resultB[i]])
        resultStr = ''.join(map(str,result))
        if resultStr.endswith("."):
            resultStr = resultStr[:-1]
        return resultStr

    else:
        spell_count = 0
        for i in range(0,len(resultB)):
            result_dec.append(resultB[i])
            if resultB[i] == 25:
                break
            spell_count += 1
        spell_text = []

        if spell_count < 7:
            for i in range(2,spell_count+2):
                if dniDigitsSpellOts[result_dec[-i]] != "roon":
                    spell_text.append(dniDigitsSpellOts[result_dec[-i]] + dniDigitsPowersOts[i-2] + " ")
            spell_str = "".join(map(str,spell_text[::-1]))
            spell_str = spell_str.replace("rra", "ra")
        else:
            spell_str = "number too long to spell in D'ni"

        return spell_str


def decnum(dni):
    input = []
    for i in range(0,len(dni)):
        input.append(dniFontDigitsDni[dni[i]])

    result = 0
    dot = 0
    for d in input :
        if dot == 0 :
            if d == 25 :
                dot = 1
            else:
                result = 25 * result + d
        else:
            result = (d / 25**dot) + result
            dot = dot + 1
    return result
