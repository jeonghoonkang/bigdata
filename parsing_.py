# contact: https://github.com/jeonghoonkang

import cPickle as pickle
import sys


try:
	filename = sys.argv[1]
except IndexError as err:
	print('IndexError: ' + str(err))
	print('Usage: python parsing <filename>')
	exit()
tsfile = pickle.load(open(filename))

print 
print "loading ... Bin file"

print tsfile
print 

print "keys of %s" %filename
print tsfile.keys()
print

print "tsfile['ts'][0]"
print tsfile['ts'][0]
print

print "tsfile['ts'][1]"
print tsfile['ts'][1]
print

print "tsfile['ts'][2]"
print tsfile['ts'][2]
print

print "tsfile['ts'][10]"
print tsfile['ts'][10]
print

print "tsfile['value'][0]"
print tsfile['value'][0]
print

print "tsfile['value'][-1]"
print tsfile['value'][-1]
print

print "length of key ts is %d" % len(tsfile['ts'])

