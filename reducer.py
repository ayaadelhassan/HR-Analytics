#!/usr/bin/env python3
# -*-coding:utf-8 -*
import sys
from operator import itemgetter
distances=[]
estimate_class = -1
k=3
#k=int(sys.argv[1])

for lines in sys.stdin:
	lines=lines.strip()
	elements = lines.split(',')
	distances.append(elements)
distances = sorted(distances,key=itemgetter(-1))
#print(distances[0])
num_0=0
num_1=0
for i in range(k):
	try:
		#print(distances[i][-2])
		if int(distances[i][-2])==0:
			num_0+=1
		elif int(distances[i][-2])==1:
			num_1+=1

	except ValueError:
		continue
		
if num_0>num_1:
	estimate_class=0
elif num_1>num_0:
	estimate_class=1		
print (estimate_class)

