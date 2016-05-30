import sys

def readFile(filename):#read a text file
	array = []
	with open(filename) as file:
		for line in file:
			line = line.rstrip('\n')
			#0	2013-12-13/06:10:00	6	0.0062
			code_country,date,hour_band,call_out = line.split('\t')
			code_country = int(code_country)
			if code_country in [0,7,39]:
				print"%d,%s,%s,%s"%(code_country,date,hour_band,call_out)

filename = sys.argv[1]
readFile(filename)