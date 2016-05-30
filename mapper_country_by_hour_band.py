#!/usr/bin/python2
import sys
import datetime

#bandas horarias de una hora
def get_hour_band(time_interval):
	date =  datetime.datetime.fromtimestamp(int(time_interval)/1000)
	return date.hour

for line in sys.stdin:
	line = line.strip()
	words = line.split('\t')

	id = int(words[0])
	time_interval =int(words[1])
	code = int(words[2])
	
	try:
		call_out = words[6]
		band_hour = get_hour_band(time_interval)
		if call_out != '':
			call_out =  float(words[6])
			print '%s\t%s\t%.4f' % (code,band_hour,call_out)
	except IndexError:
		continue