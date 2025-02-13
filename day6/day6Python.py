
#for sample answer is 5
#also there is only 1 line in this data
def main():
    answer = getprocesssedletters()
    print(answer)

def getprocesssedletters():
    input = open("C:\GitHub\AdventOfCode2022\day6\day6input.txt", "r")
    print("process started")
    for line in input:
        four_letter_list = []
        every_letter = []
        for i in range(len(line)):
            every_letter.append(line[i])
            if i < 4:
                four_letter_list.append(line[i])
            else:
                four_letter_list.pop(0)
                four_letter_list.append(line[i])
            if len(set(four_letter_list)) > 3:
                return (len(every_letter))
            
main()

# answer 1262