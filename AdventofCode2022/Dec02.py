RPSPoints = 0

RPS     = {"A X": 4,"A Y": 8,"A Z": 3,"B X": 1,"B Y": 5,"B Z": 9,"C X": 7,"C Y": 2,"C Z": 6,}
RPSReal = {"A X": 3,"A Y": 4,"A Z": 8,"B X": 1,"B Y": 5,"B Z": 9,"C X": 2,"C Y": 6,"C Z": 7,}

for lines in open("D:\Programming\AdventofCode\Dec02.txt"):
    RPSPoints += RPS[lines[0:3]]
print(RPSPoints)

RPSPoints = 0

for lines in open("D:\Programming\AdventofCode\Dec02.txt"):
    RPSPoints += RPSReal[lines[0:3]]
print(RPSPoints)