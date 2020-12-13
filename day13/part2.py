inpt = open('input.txt', 'r').read().split('\n')[1].split(',')

inptLst = []
for i in range(len(inpt)):
	if inpt[i] != 'x':
		inptLst.append((i, int(inpt[i])))
searchLst, n, addend = [inptLst[0]], 0, 1
for i in range(1, len(inptLst)):
	searchLst.append(inptLst[i])
	addend *= searchLst[-2][1]
	while (n + searchLst[-1][0]) % searchLst[-1][1] != 0:
		n += addend
print(n)