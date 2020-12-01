inpt = list(map(int, open('input.txt', 'r').read().split('\n')))

for i in range(len(inpt)):
	for j in range(1, len(inpt)):
		for k in range(2, len(inpt)):
			if inpt[i] + inpt[j] + inpt[k] == 2020:
				print(inpt[i] * inpt[j] * inpt[k])
