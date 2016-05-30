#!/usr/bin/python2
import sys
import datetime

def getCellRegion(cellId):
    if cellId >=1 and cellId <= 3300: #region sur
        tmp = str(cellId)
        if len(tmp) == 1:
            return 7 #suroeste
        else:
            cellComp = int(tmp)
            if len(tmp) > 2:
                tmp2 = tmp[-2:]
                cellComp = int(tmp2)
            if cellComp < 33:
                return 7 #suroeste
            elif cellComp > 66:
                return 9 #sureste
            else:
                return 8 #sur
    elif 3301 <= cellId <= 6600: #region central
        cellComp = int((str(cellId))[-2:])
        if 0 < cellComp < 33:
            return 4  #oeste
        elif cellComp > 66:
            return 6  #este
        else:
            return 5  #centro
    else:#region norte
        cellComp = int((str(cellId))[-2:])
        if 0 < cellComp < 33 :
            return 1 #noroeste
        elif cellComp > 66 or cellComp == 0:
            return 3 #noreste
        else:
            return 2 #norte

for line in sys.stdin:
	line = line.strip()
	words = line.split('\t')

	id = int(words[0])
	time_interval =int(words[1])
	code = words[2]

	try:
		call_out = words[6]
		if call_out != '':
			call_out =  float(words[6])
			region_id = getCellRegion(id)
            		date = datetime.datetime.fromtimestamp(int(time_interval)/1000).strftime('%Y-%m-%d/%H:%M:%S')
			key = str(region_id) + '-' + code
			print '%s\t%s\t%s\t%.4f' % (key,date,time_interval,call_out)
	except IndexError:
		continue
