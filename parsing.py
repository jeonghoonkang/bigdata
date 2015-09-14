# contact: https://github.com/jeonghoonkang

import cPickle as pickle

filename = 'VTT_GW1_HA12_VM_KV_K.bin'
tsfile = pickle.load(open(filename))

print 
print "loading ... Bin file"

print tsfile

print "keys of %s" %filename, tsfile.keys()
print "tsfile['ts'][0]", tsfile['ts'][0]
print "tsfile['ts'][1]", tsfile['ts'][1]
print "tsfile['ts'][2]", tsfile['ts'][2]
print "tsfile['ts'][10]", tsfile['ts'][10]
print "tsfile['value'][0]", tsfile['value'][0]
print "tsfile['value'][-1]", tsfile['value'][-1]

print "length of key ts is %d" % len(tsfile['ts'])
