file = open('input8.txt').read().split('\n')


#while True:
inx = 0
accumulator = 0
indx = []

while True:
	if not inx in indx:
		if inx >= len(file):
			print('solution is',accumulator)
		else:
			indx.append(inx)
			op,value = file[inx].split(' ')
			if op == 'jmp':
				inx += int(value)
			elif op == 'nop':
				inx += 1
			elif op == 'acc':
				accumulator += int(value)
				inx += 1
			print(op,value)
	else:
		break

print(accumulator)

