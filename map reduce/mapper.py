#!/usr/bin/env python3
# -*-coding:utf-8 -*
import sys
import math
#inputval=[1,35,5,8,1,0,49,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1]
inputval=[1,57,1,24,0,0,10,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0]
for lines in sys.stdin:
	square_dist = 0.0
	lines = lines.strip()
	features = lines.split(',')
	for i in range(len(features)-1):
		if features[i]!='':
			square_dist += (float(features[i]) - float(inputval[i]))**2
	dist = math.sqrt(square_dist)
	features.append((str(dist)))
	print (','.join(features))

