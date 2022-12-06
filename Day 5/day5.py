file1 = open('input.txt', 'r')
lines = file1.readlines()

stack1 = []
stack2 = []
stack3 = []
stack4 = []
stack5 = []
stack6 = []
stack7 = []
stack8 = []
stack9 = []

def init_stacks():
    stack1.clear()
    stack2.clear()
    stack3.clear()
    stack4.clear()
    stack5.clear()
    stack6.clear()
    stack7.clear()
    stack8.clear()
    stack9.clear()

def select_stack(stackNumber):
    if stackNumber == 1:
        return stack1
    elif stackNumber == 2:
        return stack2
    elif stackNumber == 3:
        return stack3
    elif stackNumber == 4:
        return stack4
    elif stackNumber == 5:
        return stack5
    elif stackNumber == 6:
        return stack6
    elif stackNumber == 7:
        return stack7
    elif stackNumber == 8:
        return stack8
    elif stackNumber == 9:
        return stack9

def reverse_stacks():
    stack1.reverse()
    stack2.reverse()
    stack3.reverse()
    stack4.reverse()
    stack5.reverse()
    stack6.reverse()
    stack7.reverse()
    stack8.reverse()
    stack9.reverse()

def print_stacks():
    print('-----------------------------------------------------')
    print(stack1)
    print(stack2)
    print(stack3)
    print(stack4)
    print(stack5)
    print(stack6)
    print(stack7)
    print(stack8)
    print(stack9)
    print('-----------------------------------------------------')

def parse_stacks_from_input(lines):
    for x in range(0, 8, 1):
        rowOfboxes = lines[x]
        rowSplit = rowOfboxes.split(' ')
        stackCount = 0
        spaceCount = 0
        for z in range(0, len(rowSplit), 1):
            if rowSplit[z] == '':
                spaceCount += 1
            else:
                if spaceCount > 0:
                    stackCount += int(spaceCount/4) + 1
                else:
                    stackCount += 1
                currentStack = select_stack(stackCount)
                currentStack.append(rowSplit[z].strip())
                spaceCount = 0

def process_movements_cm_9000(lines):
    for x in range(10, len(lines), 1):
        movementInput = lines[x].replace('move ', '').replace('from ', '').replace('to ', '').split(' ')
        fromStack = select_stack(int(movementInput[1]))
        toStack = select_stack(int(movementInput[2]))
        movementCount = int(movementInput[0])
        for i in range(movementCount):
            toStack.append(fromStack.pop())

def process_movements_cm_9001(lines):
    for x in range(10, len(lines), 1):
        movementInput = lines[x].replace('move ', '').replace('from ', '').replace('to ', '').split(' ')
        fromStack = select_stack(int(movementInput[1]))
        toStack = select_stack(int(movementInput[2]))
        movementCount = int(movementInput[0])
        tempStack = []
        for i in range(movementCount):
            tempStack.append(fromStack.pop())
        tempStack.reverse()
        for item in tempStack:
            toStack.append(item)

# CM 9000
init_stacks()
parse_stacks_from_input(lines)
reverse_stacks()
process_movements_cm_9000(lines)
print_stacks()

# CM 9001
init_stacks()
parse_stacks_from_input(lines)
reverse_stacks()
process_movements_cm_9001(lines)
print_stacks()