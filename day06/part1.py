print(sum(len(set(i) - {'\n'}) for i in open('input.txt', 'r').read().split('\n\n')))