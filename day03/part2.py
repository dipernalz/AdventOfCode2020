inpt = open('input.txt', 'r').read().split('\n')

p1 = sum(1 if inpt[i][(i * 1) % len(inpt[i])] == '#' else 0 for i in range(len(inpt)))
p2 = sum(1 if inpt[i][(i * 3) % len(inpt[i])] == '#' else 0 for i in range(len(inpt)))
p3 = sum(1 if inpt[i][(i * 5) % len(inpt[i])] == '#' else 0 for i in range(len(inpt)))
p4 = sum(1 if inpt[i][(i * 7) % len(inpt[i])] == '#' else 0 for i in range(len(inpt)))
p5 = sum(1 if inpt[i * 2][(i) % len(inpt[i])] == '#' else 0 for i in range(len(inpt) // 2))
print(p1 * p2 * p3 * p4 * p5)