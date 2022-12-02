chonkList = [0]
indexCounter = 0

for lines in open("D:\Programming\AdventofCode\Dec01.txt"):
    if lines == "\n":
        indexCounter += 1; chonkList.append(0) 
    else:
         chonkList[indexCounter] += int(lines)

print(max(chonkList),sum(sorted(chonkList,reverse=True)[0:3]))