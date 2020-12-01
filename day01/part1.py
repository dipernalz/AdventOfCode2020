inpt = list(map(int, open('input.txt', 'r').read().split('\n')))

for i in range(len(inpt)):
	for j in range(1, len(inpt)):
		if inpt[i] + inpt[j] == 2020:
			print(inpt[i] * inpt[j])
