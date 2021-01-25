import random

maze = []
mazeSize = [int(input("Width: ")),int(input("Height: "))]
#mazeSize = [10,10]
currentPath = [mazeSize[0] * mazeSize[1] - 1]
solution = []

# initalize maze
for i in range(mazeSize[0] * mazeSize[1]):
    maze.append("lb")

# returns list of indexs of neihbors
def getUnvisitedNeihborCells(currentSpace):
    neihbors = []
    # right
    if currentSpace + 1 < mazeSize[0] * mazeSize[1] - 1 and (currentSpace + 1) % mazeSize[0] != 0 and not "v" in maze[currentSpace + 1]:
        neihbors.append(currentSpace + 1)
    # down
    if currentSpace < mazeSize[0] * mazeSize[1] - mazeSize[0] and not "v" in maze[currentSpace + mazeSize[0]]:
        neihbors.append(currentSpace + mazeSize[0])
    # left
    if currentSpace - 1 >= 0 and currentSpace % mazeSize[0] != 0 and not "v" in maze[currentSpace - 1]:
        neihbors.append(currentSpace - 1)
    # up
    if currentSpace >= mazeSize[0] and not "v" in maze[currentSpace - mazeSize[0]]:
        neihbors.append(currentSpace - mazeSize[0])
    return neihbors

# carve maze
while True:
    if len(currentPath) > 0 and currentPath[-1] == 0 and len(solution) == 0:
        solution = currentPath.copy()
    if len(currentPath) == 0:
        break
    elif (unvisitedNeihborCellCount := len(unvisitedNeihborCells := getUnvisitedNeihborCells(currentPath[-1]))) > 0:
        maze[currentPath[-1]] += "v"
        currentPath.append(unvisitedNeihborCells[random.randrange(unvisitedNeihborCellCount)])
        maze[currentPath[-1]] += "v"

        if currentPath[-1] == currentPath[-2] + mazeSize[0]:
            maze[currentPath[-2]] = maze[currentPath[-2]].replace("b", "")   
        if currentPath[-1] == currentPath[-2] - mazeSize[0]:
            maze[currentPath[-1]] = maze[currentPath[-1]].replace("b", "")   
        if currentPath[-1] == currentPath[-2] + 1:
            maze[currentPath[-1]] = maze[currentPath[-1]].replace("l", "")   
        if currentPath[-1] == currentPath[-2] - 1:
            maze[currentPath[-2]] = maze[currentPath[-2]].replace("l", "")   
    else:
        currentPath.pop()

# visualize maze
def mazeVisuale(showSolution):
        
    output = "\nStart Here\n   "
    for i in range(mazeSize[0]*2-3):
        output += "_"
    output += "\n"
    for i in range(mazeSize[0] * mazeSize[1]):
        if "l" in maze[i]:
            output += "|"
        else:
            if showSolution and i in solution:
                output += "#"
            else:          
                output += " "
        if "b" in maze[i]:
            if i == mazeSize[0] * mazeSize[1] - 1:
                output += "_  End Here"
                break
            output += "_"
        else:
            if showSolution and i in solution:
                output += "#"
            else:          
                output += " "
        if (i+1) % mazeSize[0] == 0:
            output += "|\n"
    return output

print(mazeVisuale(True))

print(mazeVisuale(False))