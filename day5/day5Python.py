input = open("C:\GitHub\AdventOfCode2022\day5\day5input.txt", "r")
list_of_stacks = [ [],[],[],[],[],[],[],[],[] ]
letters_on_top_of_crates = ""
current_line = 0
#honestly i could have made a list containing each list and iterated through that list instead of hard coding it
#if i had had 20 or more then making a list of lists would have been needed
#actually i do need to refactor all this to be lists, because the instructors later require them to be in lists. DONE!
for line in input:
    if(current_line < 8):

        for i in range (len(list_of_stacks)):
            stack_line = line[1+(i*4):2+(i*4)]
            if(stack_line != " "):
                list_of_stacks[i].append(stack_line)
            
    # Once you get all the stacks filled out the lists get reversed so we can use .pop since we need to remove the "top" crate from the list
    if (current_line == 8):
        for i in range(len(list_of_stacks)):
            list_of_stacks[i].reverse()

    #This... gonna say needs to start at the end, but .pop removes the last item from a given list and append adds it to the end
    if (current_line > 9):
        #A variable to hold the instructions
        instructions = line.split(" ")
        for i in range (int(instructions[1])):
            list_of_stacks[int(instructions[5]) - 1].append(list_of_stacks[int(instructions[3]) - 1].pop()) 

    current_line += 1


for i in range (len(list_of_stacks)):
    print(list_of_stacks[i])
    if (len(list_of_stacks[i]) != 0):
        print(list_of_stacks[i][len(list_of_stacks[i]) - 1])
        letters_on_top_of_crates += list_of_stacks[i][len(list_of_stacks[i]) - 1]


print(letters_on_top_of_crates)
print(list_of_stacks[3])

#Right answer is JDTMRWCQJ