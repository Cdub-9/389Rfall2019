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
headerSize = 24

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
s1t, s1l = struct.unpack( "<LL", data[headerSize:headerSize+8]) 
s1v = data[headerSize+8:headerSize+32]
print('Section 1')
print(s1t)
print(s1l)
print(s1v)
currSize = headerSize+32

s2t, s2l = struct.unpack( "<LL", data[currSize:currSize+8]) 
s2v1, s2v2 = struct.unpack("<dd", data[currSize+8:currSize+24])
print('Section 2')
print(s2t)
print(s2l)
print s2v1
print s2v2

currSize = currSize + 24 
s3t, s3l = struct.unpack( "<LL", data[currSize:currSize+8]) 
print('Section 3')
print(s3t)
print(s3l)
#print(data[currSize+8:currSize+currSize+(202776+8)])


currSize = currSize + (202776+8) 
s4t, s4l = struct.unpack( "<LL", data[currSize:currSize+8]) 
s4v = data[currSize+8:currSize+52]
print('Section 4')
print(s4t)
print(s4l)
print(s4v)

currSize = currSize+52 
s5t, s5l = struct.unpack( "<LL", data[currSize:currSize+8]) 
s5v = data[currSize+8:currSize+88]
print('Section 5')
print(s5t)
print(s5l)
print s5v
