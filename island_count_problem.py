# Eliza Nip
#CS325
#Question 3
#Count island
def count_islands(graph):
    # Base case: If there's no graph, return 0
    if graph is None:
        return 0
    # If base case is false,record the length of row,column
    row = len(graph)
    column = len(graph[0])
    # Set count to count island
    count = 0

    # Loop thru i rows
    for i in range(row):
        # Loop thru k columns
        for k in range(column):
            # Eg first element would be [i][k]->[0][0].
            # If element is 1, go to the next helper function
            if graph[i][k] == 1:
                search_island(graph, row, column, i, k)
                # Increment count by 1
                count += 1
    return count
# Perform DFS
def search_island(graph, row, column, rX, cY):
    # Check value atm is 0.
    if graph[rX][cY] == 0:
        return
    graph[rX][cY] = 0
    # Keep track on visted nodes, check last element of row and column
    if rX < 0 or cY < 0 or rX >= row or cY >= column:
        return
    else: 
        # Check right element, left element, top, down
        if rX != row - 1:
            search_island(graph, row, column, rX + 1 ,cY)
        if rX != 0:
            search_island(graph, row, column, rX - 1 ,cY)
        if cY != column - 1:
            search_island(graph, row, column, rX, cY + 1)
        if cY != 0:
            search_island(graph, row, column, rX, cY - 1)

inputGraph = [[1,1,1,0,0],
             [0,0,0,0,1],
             [1,0,0,0,1],
             [0,0,0,0,0]]
print ("Number of Island:",count_islands(inputGraph))
    







