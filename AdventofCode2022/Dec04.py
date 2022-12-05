lista = open("D:\Programming\AdventofCode2022\Dec04.txt")
numExtractor = []
numWriter = []
fullCover = 0


for lines in lista:
    for char in lines:
        if char == "-" or char == ",":
            numExtractor.append(int(''.join(numWriter)))
            numWriter = []
        elif char == "\n" and numWriter != []:
            numExtractor.append(int(''.join(numWriter)))
            numWriter = []
            if (numExtractor[0] >= numExtractor[2] and numExtractor[1] <= numExtractor[3]) or ((numExtractor[0] <= numExtractor[2] and numExtractor[1] >= numExtractor[3])):
                fullCover += 1
            numExtractor = []
        else:
            numWriter.append(char)

print(fullCover)
lista.close()

lista = open("D:\Programming\AdventofCode2022\Dec04.txt")

partialCover = 0
numWriter = []

for lines in lista:
    for char in lines:
        if char == "-" or char == ",":
            numExtractor.append(int(''.join(numWriter)))
            numWriter = []
        elif char == "\n" and numWriter != []:
            numExtractor.append(int(''.join(numWriter)))
            numWriter = []
            if (numExtractor[1] >= numExtractor[2] and numExtractor[1] <= numExtractor[3]) or (numExtractor[3] >= numExtractor[0] and numExtractor[3] <= numExtractor[1]):
                partialCover += 1
            print(numExtractor)
            numExtractor = []
        else:
            numWriter.append(char)

print(partialCover)
lista.close()