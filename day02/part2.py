print(sum(1 if (s.split(" ")[2][int(s.split(" ")[0].split('-')[0]) - 1] == s.split(" ")[1][0]) ^ (s.split(" ")[2][int(s.split(" ")[0].split('-')[1]) - 1] == s.split(" ")[1][0]) else 0 for s in open('input.txt', 'r').read().split('\n')))