file1 = open('input.txt', 'r')
lines = file1.readlines()
rangesDuplicatedCount = 0
rangesAnyOverlap = 0

for line in lines:
    ranges = line.split(",")
    range1 = ranges[0].split("-")
    range2 = ranges[1].split("-")
    
    if int(range1[0]) <= int(range2[0]) and int(range1[1]) >= int(range2[1]): # range1 contains range2
        rangesDuplicatedCount += 1
        rangesAnyOverlap += 1
    elif int(range2[0]) <= int(range1[0]) and int(range2[1]) >= int(range1[1]): #range 2 contains range 1
        rangesDuplicatedCount += 1
        rangesAnyOverlap += 1
    elif int(range1[1]) >= int(range2[0]) and int(range1[1]) <= int(range2[1]): #range 1 ends inside range 2
        rangesAnyOverlap += 1
    elif int(range2[1]) >= int(range1[0]) and int(range2[1]) <= int(range1[1]): #range 2 ends inside range 1
        rangesAnyOverlap += 1
    elif int(range1[0]) >= int(range2[0]) and int(range1[0]) <= int(range2[1]): #range 1 starts inside range 2
        rangesAnyOverlap += 1
    elif int(range2[0]) >= int(range1[0]) and int(range2[0]) <= int(range1[1]): #range 2 starts inside range 1
        rangesAnyOverlap += 1
        
print(rangesDuplicatedCount)
print(rangesAnyOverlap)