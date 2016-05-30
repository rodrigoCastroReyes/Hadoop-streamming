#!/usr/bin/python2
from operator import itemgetter
import sys
import datetime

saved_band_hour = None
saved_code = None
count_call_out = 0
cont_num = 0

for line in sys.stdin:
	line = line.strip()
	code,band_hour,call_out = line.split('\t')

	try: 
		band_hour = int(band_hour)
		call_out = float(call_out)
	except ValueError:
		continue 

	if  saved_band_hour == band_hour : # si la banda horaria es igual a la banda horaria que hemos registrado antes(current_band_hour), sumamos la actividad de llamadas
		count_call_out += call_out
		cont_num+=1
	else:
		if saved_band_hour:
			print '%s\t%d\t%.4f' % (saved_code, saved_band_hour, (count_call_out/cont_num))
		cont_num = 0
		saved_band_hour = band_hour
		count_call_out = call_out
		saved_code = code

#ultima iteracion
if saved_band_hour == band_hour:
	print '%s\t%d\t%.4f' % (saved_code, saved_band_hour, count_call_out)