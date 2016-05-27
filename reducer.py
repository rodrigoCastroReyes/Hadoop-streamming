#!/usr/bin/python2
from operator import itemgetter
import sys

current_code = None
current_call_out = 0
word = None

for line in sys.stdin:
	line = line.strip()
	code, call_out = line.split('\t')
	try: 
		call_out = float(call_out)
	except ValueError:
		continue 

	if current_code == code:
		current_call_out +=call_out
	else:
		if current_code:
			print '%s\t%.4f' % (current_code, current_call_out)
		current_code = code
		current_call_out = call_out

#ultima iteracion
if current_code == code:
	print '%s\t%.4f' % (current_code, current_call_out)