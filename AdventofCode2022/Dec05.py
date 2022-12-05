lista = open("D:\Programming\AdventofCode2022\Dec05.txt")

crateMatrix=[]
sortedCrateMatrix = []
xCount = 0

for lines in lista:
    if lines[1] == "1":
        break
    crateMatrix.append([])
    for char in lines:
        if char == "[" or char == "]" or char == " " or char == "\n":
            continue
        else:
            crateMatrix[xCount].append(char)
    xCount += 1

#print(crateMatrix)

for i in range(0,len(crateMatrix)+1):
    sortedCrateMatrix.append([])
    for j in range (0,len(crateMatrix)):
        if crateMatrix[j][i] != '0':
            sortedCrateMatrix[i].append(crateMatrix[j][i])
        else:
            continue
for i in range(0,len(sortedCrateMatrix)):
    sortedCrateMatrix[i].reverse()

#print(sortedCrateMatrix)
lista.close()

r = open("D:\Programming\AdventofCode2022\Dec05_01.txt")

moveCrate = []
xCount = 0

for lines in r:
    moveCrate.append([])
    f = lines.split()
    moveCrate[xCount].append(int(f[1]))
    moveCrate[xCount].append(int(f[3]))
    moveCrate[xCount].append(int(f[5]))
    xCount+=1

#print(moveCrate)

#for i in moveCrate:
#    for j in range(0,i[0]):
#        sortedCrateMatrix[(i[2]-1)].append(sortedCrateMatrix[(i[1]-1)][-1])
#        sortedCrateMatrix[(i[1]-1)] = sortedCrateMatrix[(i[1]-1)][:-1]

for i in moveCrate:
    for j in range((len(sortedCrateMatrix[(i[1]-1)])-i[0]),(len(sortedCrateMatrix[(i[1]-1)]))):
        sortedCrateMatrix[(i[2]-1)].append(sortedCrateMatrix[(i[1]-1)][j])
    sortedCrateMatrix[(i[1]-1)] = sortedCrateMatrix[(i[1]-1)][0:len(sortedCrateMatrix[(i[1]-1)])-i[0]]

print(sortedCrateMatrix)





