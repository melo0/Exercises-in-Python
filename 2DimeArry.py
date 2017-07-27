x = [int(z) for z in raw_input().split(',')]
result = []
for i in range( 0, x[0]):
	result.append([])
	for j in range(0, x[1]):
		result[i].append(i*j)
print result
