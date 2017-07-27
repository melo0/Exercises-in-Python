# sqrt of formula
import math
resault = []
h = [x for x in raw_input().split(',')]
c=50
d=30
for i in h:
	resault.append(str(int(math.sqrt((2*c*(float(i)))/d))))
print ','.join(resault)
