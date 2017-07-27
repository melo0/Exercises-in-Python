x = [z for z in raw_input().split(',')]
result = []
for i in range( 0, int(x[0])):
	result.append([])
	for j in range(0, int(x[1])):
		result[i].append(i*j)
print result
