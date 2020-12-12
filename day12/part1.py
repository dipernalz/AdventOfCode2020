inpt = open('input.txt', 'r').read().split('\n')

def travel(direction, dist):
	global x, y
	if direction == 'N':
		y += dist
	elif direction == 'S':
		y -= dist
	elif direction == 'E':
		x += dist
	elif direction == 'W':
		x -= dist

x, y = 0, 0
direction = 'E'
directionLst = ['N', 'E', 'S', 'W']
for i in inpt:
	instr = i[0]
	n = int(i[1:])
	if instr == 'F' or instr in directionLst:
		travel(direction if instr == 'F' else instr, n)
	elif instr == 'R':
		direction = directionLst[int((directionLst.index(direction) + n / 90) % 4)]
	elif instr == 'L':
		direction = directionLst[int((directionLst.index(direction) - n / 90) % 4)]

print(abs(x) + abs(y))