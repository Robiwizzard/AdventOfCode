lista = open("D:\Programming\AdventofCode2022\Dec03.txt")
sharedItems = []
badge = []

for lines in lista:
    half = int((len(lines) / 2))
    for char in lines[0:half]:
        if lines[half:len(lines)-1].find(char) != -1:
            sharedItems.append(char)
            break

def prioCalc(x):
    if ord(x) < 97:
        return ord(x) - 38
    else:
         return ord(x) - 96

mappedList = [prioCalc(x) for x in sharedItems]
print(sum(mappedList))

lista.close()
lista = open("D:\Programming\AdventofCode2022\Dec03.txt")
sharedItems = []

for lines in lista:
    if len(badge) != 3:      
        badge.append(lines[:len(lines)-1])
    else:
        for char in badge[0]:
            if (badge[1].find(char) != -1 and badge[2].find(char) != -1):
                sharedItems.append(char)
                badge = []
                badge.append(lines[:len(lines)-1])
                break

mappedList2 = [prioCalc(x) for x in sharedItems]
print(sum(mappedList2))
lista.close()