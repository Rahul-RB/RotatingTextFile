from datetime import datetime
from src import CustomRotatingFileHandler as CRFH

i=0
def condition():
	return i%10 == 0

with CRFH("x.txt",condition,10) as fp:
	while i<112:
		fp.write(str(datetime.now().microsecond)+"\n")
		i += 1
