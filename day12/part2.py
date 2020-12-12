inpt = open('input.txt', 'r').read().split('\n')

x, y = 0, 0
wx, wy = 10, 1
for i in inpt:
	instr = i[0]
	n = int(i[1:])
	if instr == 'N':
		wy += n
	elif instr == 'S':
		wy -= n
	elif instr == 'E':
		wx += n
	elif instr == 'W':
		wx -= n
	elif instr == 'F':
		x += n * wx
		y += n * wy
	elif instr == 'R':
		if n == 90:
			wx, wy = wy, -wx
		elif n == 180:
			wx, wy = -wx, -wy
		elif n == 270:
			wx, wy = -wy, wx
	elif instr == 'L':
		if n == 90:
			wx, wy = -wy, wx
		elif n == 180:
			wx, wy = -wx, -wy
		elif n == 270:
			wx, wy = wy, -wx

print(abs(x) + abs(y))