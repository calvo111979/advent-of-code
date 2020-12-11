file = open('input8.txt').read().split('\n')[:-1]

def checkOperation(file):
    inx = 0
    accumulator = 0
    indx = []
    while True:
        if not inx in indx:
            if inx >= len(file):
                print('solution is',accumulator)
                return
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
        else:
            return


for i,op in enumerate(file):
    auxFile = [putoVic for putoVic in file]
    if op.split(' ')[0] == 'nop':
        auxFile[i] = ' '.join(['jmp',op.split(' ')[1]])
        checkOperation(auxFile)
    elif op.split(' ')[0] == 'jmp':
        auxFile[i] = ' '.join(['nop',op.split(' ')[1]])
        checkOperation(auxFile)