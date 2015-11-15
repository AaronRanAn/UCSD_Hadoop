#!/usr/bin/env python
import sys

# --------------------------------------------------------------------------
#This reducer code will input a <word, value> input file, and join words together
# Note the input will come as a group of lines with same word (ie the key)
# As it reads words it will hold on to the value field
#
# It will keep track of current word and previous word, if word changes
#   then it will perform the 'join' on the set of held values by merely printing out
#   the word and values.  In other words, there is no need to explicitly match keys b/c
#   Hadoop has already put them sequentially in the input
#
# At the end it will perform the last join
#
#
#  Note, there is NO error checking of the input, it is assumed to be correct, meaning
#   it has word with correct and matching entries, no extra spaces, etc.
#
#  see https://docs.python.org/2/tutorial/index.html for python tutorials
#
#  San Diego Supercomputer Center copyright
# --------------------------------------------------------------------------

ABC_dict={}

# see https://docs.python.org/2/tutorial/datastructures.html for list details

kvs=[]

for line in sys.stdin:
    line       = line.strip()       #strip out carriage return
    key_value  = line.split('\t')   #split line, into key and value, returns a list
    kvs.append(key_value)

    if key_value[0]=="ABC":
        if ABC_dict.has_key(key_value[1])==False:
            ABC_dict.update({key_value[1]:0})

for key_value in kvs:

    if ABC_dict.has_key(key_value[0]):
        ABC_dict[key_value[0]]+=int(key_value[1])

for key, value in ABC_dict.iteritems() :
    print( '%s %s' % (key, value)) 
