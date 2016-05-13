# Motive of project is to keep cleaning  cache memory if  total memory usage is more than 60% of the original ram usage

import os

f = os.popen('free -g')
now = f.read()

param = now.split()

print param

totalram = int(param[7])

print "Total ram available is :",totalram
freerequired =  int(totalram/2.3)

print "Free required :",freerequired
used = totalram - freerequired

if freerequired <= param[9]:
	print "Need to clean cache memory"
	os.system("sync; echo 1 > /proc/sys/vm/drop_caches")
	