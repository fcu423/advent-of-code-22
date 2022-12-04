file1 = open('input.txt', 'r')
lines = file1.readlines()

priorityString = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
totalPriority = 0

# Priority of misplaced items
for line in lines:
    compartment1 = line[:int((len(line)/2))]
    compartment2 = line[int(len(line)/2):]
    for char in compartment1:
        if compartment2.find(char) != -1:
            totalPriority += priorityString.find(char) + 1
            break

print(totalPriority)

# Priority of badges
totalPriority = 0
for x in range(0, len(lines), 3):
    line1 = set(lines[x])
    line2 = set(lines[x+1])
    line3 = set(lines[x+2])
    commonItemSet = line1.intersection(line2, line3)
    commonItemSet.discard("\n")
    totalPriority += priorityString.find(commonItemSet.pop()) + 1

print(totalPriority)