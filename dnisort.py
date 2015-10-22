#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import re
import argparse
from argparse import RawTextHelpFormatter

parser = argparse.ArgumentParser(description="""
Sorts a csv database of D'ni words (or any wordlist for that matter) in D'ni
alphabetical order, using NTS or Dnifont encoding (OTS is too irregular to
sort properly).
The program prints to the standard output; to save to a file use

$ dnisort.py csvfile.csv > output.csv
""", formatter_class=RawTextHelpFormatter)
parser.add_argument("csv", help="CSV database wordlist", action="store")
parser.add_argument("-f", "--dfont", help="use the Dnifont format", action="store_true")
args = parser.parse_args()


def dfont2nts(in_dfont):
	out_nts = in_dfont.replace("c", "ç")
	out_nts = out_nts.replace("x", "c")
	out_nts = out_nts.replace("k", "x")
	out_nts = out_nts.replace("K", "k")
	out_nts = out_nts.replace("d", "ð")
	out_nts = out_nts.replace("D", "d")
	out_nts = out_nts.replace("S", "š")
	out_nts = out_nts.replace("T", "þ")
	out_nts = out_nts.replace("I", "á")
	out_nts = out_nts.replace("A", "é")
	out_nts = out_nts.replace("E", "í")
	out_nts = out_nts.replace("O", "ó")
	out_nts = out_nts.replace("U", "ú")
	out_nts = out_nts.replace("å", "æ")
	return out_nts


# sorting string
sortstring = "vbtsšjgyxkaáfpiíeérmþðdhoóçwuúclæzn"

#if args.dfont: sortstring = "vbtsSjgykKaIfpiEeArmTdDhoOcwuUxlåzn"

list_unord = {}
list_index = []
tabs = []

if args.csv == "":
	parser.print_usage()
	sys.exit()

csv_file = open(args.csv, 'rU')
header = csv_file.readline().rstrip('\n') # keep the header for later

for line in csv_file:
	tabs = line.rstrip('\n').split('\t')
	
	# remove empty lines
	if tabs[0].rstrip('\n') == "": continue
	
	# if using Dnifont, convert the line to NTS
	if args.dfont:
		col1 = dfont2nts(tabs[0])
	else:
		col1 = tabs[0]
		
	# each line is indentified by the item in the first column,
	# stripped of any characters beside alphanumeric ones
	in_item = re.sub('[^vbtsšjgyxkaáfpiíeérmþðdhoóçwuúclæzn]+', '', col1.lower())

	# I need a separate index of the identifiers to use with sorted()
	list_index.insert(len(list_index), in_item)

	list_unord[in_item] = line.rstrip('\n')
csv_file.close()

# the lambda function sorts the array according to the sorting string,
# but halts if it finds a character not in the sorting string,
# which is why I had to strip it from non-alphabetic characters

list_ord = sorted(list_index, key=lambda word: [sortstring.index(c) for c in word])

# print the list to the standard output
print header
for item in list_ord:
	print list_unord[item]

