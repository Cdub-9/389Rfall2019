#!/usr/bin/env python2

import sys
import struct


# You can use this method to exit on failure conditions.
def bork(msg):
    sys.exit(msg)


# Some constants. You shouldn't need to change these.
MAGIC = 0x8BADF00D
VERSION = 1

if len(sys.argv) < 2:
    sys.exit("Usage: python stub.py input_file.fpff")

# Normally we'd parse a stream to save memory, but the FPFF files in this
# assignment are relatively small.
with open(sys.argv[1], 'rb') as fpff:
	data = fpff.read()

# Hint: struct.unpack will be VERY useful.
# Hint: you might find it easier to use an index/offset variable than
# hardcoding ranges like 0:8
magic, version = struct.unpack("<LL", data[0:8])
#print(magic)
#print(hex(magic))
time,   = struct.unpack("<L", data[8:12])
#print(hex(time))
author,   = struct.unpack("<Q", data[12:20])
#print(data[12:20])
#print(author)
#print(hex(author))
sectionCount, = struct.unpack("<L", data[20:24])
#print(sectionCount)

if magic != MAGIC:
	print("bad magic ") 
	print(magic) 
	bork("Bad magic! Got %s, expected %s" % (hex(magic), hex(MAGIC)))

if version != VERSION:
	print("bad version ")
	print(version)    
	bork("Bad version! Got %d, expected %d" % (int(version), int(VERSION)))

print("------- HEADER -------")
print("MAGIC: %s" % hex(magic))
print("VERSION: %d" % int(version))
print("Time: %s" % str(time))
print("Author: %s" % data[12:20])
print("Section Count: %d" % sectionCount)

# We've parsed the magic and version out for you, but you're responsible for
# the rest of the header and the actual FPFF body. Good luck!

print("-------  BODY  -------")
