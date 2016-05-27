#!/usr/bin/python2
import sys
import datetime

for line in sys.stdin:
	line = line.strip()
	words = line.split('\t')

	id = int(words[0])
	time_interval =int(words[1])
	code = int(words[2])

	try:
		call_out = words[6]
		if call_out != '':
			call_out =  float(words[6])
			#date =  datetime.datetime.fromtimestamp(int(time_interval)/1000).strftime('%Y-%m-%d %H:%M:%S')
			#print '%d\t%d\t%s\t%.4f' % (id,code,date,call_out)
			print '%s\t%s\t%.4f' % (code,time_interval,call_out)
			#print '%d\t%s\t%s\t%.4f' % (code,time_interval,date,call_out)
	except IndexError:
		continue