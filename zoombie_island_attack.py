# Eliza Nip
#CS325
#Question 4
#Zombie attack
import collections

def zombie_attack(grid):
    # Base case: If there's no grid, return -1
    if grid is None:
        return -1
    # If base case is false,record the length of row,column
    row = len(grid)
    column = len(grid[0])
    # keep track of total number of days
    day = 0
    # Set deque that element can be added from left/right side
    queue = collections.deque()
    # Loop thru i rows
    for i in range(row):
        # Loop thru k columns
        for k in range(column):
            # Human on 0 day
            if grid[i][k] == 1:
                day += 1
            # Zombie on 0 day
            if grid[i][k] == 2:
                # Pop into queue
                queue.append((i,k))
    # Iterate thru queue
    # Do BFS here, look around (left,right,up,down)to find human,turn 1 into 2, pop zombie
    while queue:
        size = len(queue)
        day += 1
        for _ in range(size):
            # https://pythontic.com/containers/deque/popleft#:~:text=popleft()%20removes%20an%20element,deque%20and%20returns%20the%20value.
            # popleft() removes an element from the left side of the deque and returns the value.
            i,k = queue.popleft()
            # Direction : Left, right, up, down
            for deltaX, deltaY in [(1,0),(0,1),(-1,0),(0,-1)]:
                nextX = i+deltaX
                nextY = k+deltaY
                # Look around, turn human 1 into zombie 2. Pop zombies, do -1 day to adjust day count
                if 0 <= nextX < row and 0 <= nextY < column and grid[nextX][nextY] == 1:
                    grid[nextX][nextY] = 2
                    queue.append((nextX,nextY))
                    day -= 1
    # Check for non-zombie existance
    for i in range(row):
        for k in range(column):
            if grid[i][k] == 1:
                return -1                
    
    return day - 1

inputGrid = [[1,2,1,0,0],
             [0,0,0,0,1],
             [2,0,0,0,2],
             [0,0,0,0,0]]
print("Number of Days to turn whole group in zombiesss:",zombie_attack(inputGrid))





    
