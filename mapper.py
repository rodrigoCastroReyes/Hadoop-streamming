#!/usr/bin/python2
import sys

for line in sys.stdin:
	line = line.strip()
	words = line.split('\t')

	id = words[0]
	time_interval = words[1]
	code = int(words[2])

	try:
		call_out = words[6]
		if call_out != '':
			call_out =  float(words[6])
			print '%d\t%.4f' % (code ,call_out)
			#print '%s\t%s\t%.4f' % (code, time_interval ,call_out)
			#print '%s' % (time_interval)
	except IndexError:
		continue