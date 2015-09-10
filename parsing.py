# author: https://github.com/jeonghoonkang
 
import cPickle as pickle
  
 filename = 'VTT_GW1_HA12_VM_KV_K.bin'
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
