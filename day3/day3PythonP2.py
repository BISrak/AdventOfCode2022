alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def main():
    total = parse_rucksack()
    print(total)

def letterconversion(passed_letter):
    return alphabet.find(passed_letter)+1

def parse_rucksack():
    total = 0
    currentline = 0
    first_group = []
    second_group = []
    third_group = []
    input = open("day3input.txt", "r")
    for line in input:
        if (currentline == 0):
            for i in range(0, len(line)):
                first_group.append(line[i])
            currentline += 1
            print("line 1")
        elif (currentline == 1):
            for i in range(0, len(line)):
                second_group.append(line[i])
            currentline += 1
            print("line2")
        else:
            for i in range(0, len(line)):
                third_group.append(line[i])
            currentline = 0
            print("line 3 reset")
            for letter in first_group:
                if(second_group.count(letter) > 0):
                    print("first found")
                    if(third_group.count(letter) > 0):
                        print("second found! converting")
                        total += letterconversion(letter)
                        first_group = []
                        second_group = []
                        third_group = []
                        break
    input.close()
    return total

main()

#correct answer was 2415