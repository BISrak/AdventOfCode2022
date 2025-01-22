input = open("day1input.txt", "r")
caloriesList = [0]
greatestNumber = 0
currentItem = 0
lines = 0
greatestThreeTotal = 0

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


caloriesList.sort()
greatestThreeTotal += caloriesList[len(caloriesList)-1]
greatestThreeTotal += caloriesList[len(caloriesList)-2]
greatestThreeTotal += caloriesList[len(caloriesList)-3]
print("Single greatest amount carried")
print(greatestNumber)
print("Top 3 greatest amount total")
print(greatestThreeTotal)
#199357 this was correct, Day 1 complete
