input = open("day2input.txt", "r")
totalPoints = 0
# roundwon = None

for line in input:
    # print(line[0])
    # print(line[2])
    if (line[2] == "Y"):
        totalPoints += 2
    elif (line[2]) == "X":
        totalPoints += 1
    else:
        totalPoints += 3

    # A statements
    if(line[0] == "A" and line[2] == "Y"):
        totalPoints += 6
        pass
    if(line[0] == "A" and line[2] == "X"):
        totalPoints += 3
        pass

    # B statements
    if(line[0] == "B" and line[2] == "Z"):
        totalPoints += 6
        pass
    if(line[0] == "B" and line[2] == "Y"):
        totalPoints += 3
        pass

    # C statements
    if(line[0] == "C" and line[2] == "X"):
        totalPoints += 6
        pass
    if(line[0] == "C" and line[2] == "Z"):
        totalPoints += 3
        pass

    # if (roundwon == True):
    #     totalPoints += 6
    # elif (roundwon == False):
    #     totalPoints += 3
    # else:
    #     pass
    # roundwon = None
input.close()
print(totalPoints)
# got the correct answer 17189