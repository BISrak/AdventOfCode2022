alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def main():
    total = parse_rucksack()
    print(total)

def letterconversion(passed_letter):
    return alphabet.find(passed_letter)+1

def parse_rucksack():
    total = 0
    input = open("day3input.txt", "r")
    for line in input:
        input_left_half = []
        input_right_half = []
        for i in range(0, len(line)//2):
            input_left_half.append(line[i])
            
        for i in range(len(line)//2, len(line)):
            input_right_half.append(line[i])
        
        for letter in input_left_half:
            if(input_right_half.count(letter) > 0):
                total += letterconversion(letter)
                break
    return total

main()

#correct answer was 7766