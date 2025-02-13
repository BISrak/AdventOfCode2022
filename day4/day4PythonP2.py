input = open("C:\GitHub\AdventOfCode2022\day4\day4input.txt", "r")
total_counter = 0
for line in input:
    sections_list = line.split(",")
    list_one = sections_list[0].split("-")
    list_two = sections_list[1].split("-")
    range_number_one = int(list_one[1]) - int(list_one[0])
    range_number_two = int(list_two[1]) - int(list_two[0])
    full_section_one = []
    full_section_two = []
    counter = 0
    overlap = False

    if(range_number_one != 0):
        for i in range(int(list_one[0]),int(list_one[1]) +1):
            full_section_one.append(i)
    else:
        full_section_one.append(int(list_one[0]))

    if(range_number_two != 0):
        for i in range(int(list_two[0]),int(list_two[1]) +1):
            full_section_two.append(i)
    else:
        full_section_two.append(int(list_two[0]))

    for i in range(len(full_section_one)):
        if(full_section_one[i] in full_section_two):
            counter += 1
            overlap = True

    if (overlap == True):
        total_counter += 1
print(total_counter)

# 903 right answer, got it right off the bat, only really had to change one thing lol, which was adding the overlap check above