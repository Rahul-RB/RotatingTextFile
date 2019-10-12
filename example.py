from datetime import datetime
from RotatingTextFile import RotatingTextFile as rtf
i=0
def condition():
	return i%10 == 0

with rtf("tmp.log",condition,10) as fp:
	while i<112:
		fp.write(str(datetime.now().microsecond)+"\n")
		i += 1
