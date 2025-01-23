input = open("day2input.txt", "r")
totalPoints = 0

for line in input:

    # A statements
    if(line[0] == "A" and line[2] == "Z"):
        totalPoints += 8
        pass
    if(line[0] == "A" and line[2] == "Y"):
        totalPoints += 4
        pass
    if (line[0] == "A" and line[2] == "X"):
        totalPoints += 3
        pass

    # B statements
    if(line[0] == "B" and line[2] == "Z"):
        totalPoints += 9
        pass
    if(line[0] == "B" and line[2] == "Y"):
        totalPoints += 5
        pass
    if (line[0] == "B" and line[2] == "X"):
        totalPoints += 1
        pass

    # C statements
    if(line[0] == "C" and line[2] == "Z"):
        totalPoints += 7
        pass
    if(line[0] == "C" and line[2] == "Y"):
        totalPoints += 6
        pass
    if (line[0] == "C" and line[2] == "X"):
        totalPoints += 2
        pass

print(totalPoints)
# 13490 was the correct answer