# 0 = Loose
# 1 = Draw
# 2 = Win
decisionDictionary = {
    "A X": "A Z",
    "A Y": "A X",
    "A Z": "A Y",
    "B X": "B X",
    "B Y": "B Y",
    "B Z": "B Z",
    "C X": "C Y",
    "C Y": "C Z",
    "C Z": "C X"
}

# Score results
scoreDictionary = {
    "A X": 4,
    "A Y": 8,
    "A Z": 3,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 7,
    "C Y": 2,
    "C Z": 6
}

file1 = open('input.txt', 'r')
lines = file1.readlines()
score = 0

# Strategy 1
for line in lines:
    line = line.strip()
    score += scoreDictionary[line]

print(f'Score according to plan: {score}')

score = 0

# Strategy 2 - Fixed
for line in lines:
    line = line.strip()
    gameToPlay = decisionDictionary[line]
    score += scoreDictionary[gameToPlay]

print(f'Score according to the real plan: {score}')