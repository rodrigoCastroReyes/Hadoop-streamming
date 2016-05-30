#!/usr/bin/python2
from operator import itemgetter
import sys
import datetime
#bandas horarias de una hora

def get_hour_band(time_interval):
	date =  datetime.datetime.fromtimestamp(int(time_interval)/1000)
	return date.hour

saved_id_region = None
saved_band_hour = None
saved_time_interval = None
saved_code = None
count_call_out = 0

for line in sys.stdin:
	line = line.strip()
	key, time_interval, call_out = line.split('\t')
	region_id,code = key.split('-')
	try: 
		region_id = int(region_id)
		call_out = float(call_out)
	except ValueError:
		continue 

	band_hour = get_hour_band(time_interval)

	if  saved_band_hour == band_hour : # si la banda horaria es igual a la banda horaria que hemos registrado antes(current_band_hour), sumamos la actividad de llamadas
		count_call_out += call_out
	else:
		if saved_band_hour:
			date = datetime.datetime.fromtimestamp(int(saved_time_interval)/1000).strftime('%Y-%m-%d/%H:%M:%S')
			print '%d\t%s\t%s\t%d\t%.4f' % (saved_id_region, saved_code ,date ,saved_band_hour, count_call_out)
		saved_id_region = region_id
		saved_code = code
		saved_time_interval = time_interval
		saved_band_hour = band_hour
		count_call_out = call_out

#ultima iteracion
if  saved_band_hour == band_hour :
	date = datetime.datetime.fromtimestamp(int(saved_time_interval)/1000).strftime('%Y-%m-%d/%H:%M:%S')
	print '%d\t%s\t%s\t%d\t%.4f' % (saved_id_region, saved_code ,date ,saved_band_hour, count_call_out)