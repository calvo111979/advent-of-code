import itertools as it
# # read the file into an array
file = [int(number) for number in open('input9.txt').read().split('\n') if number != '']

maxValue = 25
minValue = 0
result = []

# for the length of the 25th value and on we check every combination
for num in range(len(file[25:])):
    result = (['OK' for i in it.combinations(file[minValue:maxValue],2) if sum(i) == file[maxValue]])
    # throws an index error as the wrong line makes result empty
    if 'OK' not in result: 
        print('This is it! Invalid number: ', file[maxValue])
        nextPartInput = file[maxValue]
        break

    print('Everything is',result,' value:',file[maxValue])

    # we iterate in the next 25 values
    minValue += 1
    maxValue += 1

# i = [35,20,15,25,47,40,62,55,65,95,102,117,150,182,127,219,299,277,309,576]
# myNum = 127
myNum = nextPartInput

def findNum(myList):
    gotIt = False

    for num in range(len(myList)):
        workList = myList[:num+1]
        for suma in it.accumulate(workList):
            if suma > myNum:
                break
            if suma == myNum:
                print('max:',max(workList),'+ min: ',min(workList), ' = ',max(workList)+min(workList))
                gotIt = True
                break
        if gotIt:
            break
    return gotIt,myList


fin, lista = findNum(file)

while not fin:
    fin,lista = findNum(lista[1:])

