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
scorePlan1 = 0
scoreRealPlan = 0

for line in lines:
    line = line.strip()
    # Strategy 1
    scorePlan1 += scoreDictionary[line]
    # Strategy 2 - Fixed
    gameToPlay = decisionDictionary[line]
    scoreRealPlan += scoreDictionary[gameToPlay]

print(f'Score according to plan: {scorePlan1}')

print(f'Score according to the real plan: {scoreRealPlan}')