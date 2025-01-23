input = open("day1input.txt", "r")
caloriesList = [0]
greatestNumber = 0
currentItem = 0
lines = 0

# not looking for just the biggest number, need the biggest number when you add 
# all the lines together delimited by an empty string
print(input)
for x in input:
    if (x == '\n'):
        currentItem += 1
        caloriesList.append(0)
        
    if (x != '\n'):
        caloriesList[currentItem] += (int(x.strip()))
        lines += 1
input.close()
print(lines)
print(currentItem)

for i in range(0, len(caloriesList)):
    if (greatestNumber < caloriesList[i]):
        greatestNumber = caloriesList[i]
    
# answer is currently too high -fixed
# its adding a ton of whitespace on every single item grabbed from the txt file -doesnt matter
# to check for an empty line you need to look for a '\n' and not '' >.<
print(greatestNumber)
#answer was 67450 Day 1 part 1 complete