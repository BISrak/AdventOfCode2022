input = open("C:\GitHub\AdventOfCode2022\day7\day7inputsample.txt", "r")

for line in input:
    # If line contains $ its a command
    # If line contains numbers followed by text, the numbers are the size of the of the file name, which is the text afterwards
    # In the readme, it looks like i might want to make an object that builds itself up using the commands to be able to correctly catalog everything. Probably need a 
    # {
    # "directoryName":"e", 
    # "size": 123,
    #   {"directoryName":"i", "size":123}
    # }
    #double check knowledge of making nested objects
    pass