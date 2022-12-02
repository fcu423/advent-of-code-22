file1 = open('input.txt', 'r')
lines = file1.readlines()
caloriesPerElf = []
caloriesCount = 0

for line in lines:
    line = line.strip()
    if line == '':
        caloriesPerElf.append(caloriesCount)
        caloriesCount = 0
    else:
        caloriesCount += int(line)

caloriesPerElf.sort(reverse=True)

# Max calories on one elf
print(f'Elf with most calories: {caloriesPerElf[0]}')

# Top 3 elves calories
print(f'Number of calories of the top 3 elves: {caloriesPerElf[0] + caloriesPerElf[1] + caloriesPerElf[2]}')