from collections import deque

class BFS:
    def __init__(self, mat, visited):
        self.mat = mat
        self.visited = visited
        self.row = [-1, -1, -1, 0, 1, 0, 1, 1]
        self.col = [-1, 1, 0, -1, -1, 1, 0, 1]

    # Function to check if it is safe to go to position (x, y)
    # from current position. The function returns false if x, y:
    # is not valid matrix coordinates or (x, y) represents water or
    # position (x, y) is already processed
    def is_safe(self, x, y):
        return (x >= 0) and (x < len(self.visited)) and \
            (y >= 0) and (y < len(self.visited[0])) and \
            (self.mat[x][y] == 1 and not self.visited[x][y])

    def process(self, i, j):
        # create an empty queue and enqueue source node
        q = deque()
        q.append((i, j))

        # mark source node as processed
        self.visited[i][j] = True

        # loop till queue is empty
        while q:
            x, y = q.popleft()

            # check for all 8 possible movements from current cell
            # and enqueue each valid movement
            for k in range(len(self.row)):
                if self.is_safe(x + self.row[k], y + self.col[k]):
                    self.visited[x + self.row[k]][y + self.col[k]] = True
                    q.append((x + self.row[k], y + self.col[k]))

class Solution:
    def __init__(self, islands_map=[]):
        self.islands_map = islands_map
        self.visited = []

    def get_num_of_the_islands(self):
        # ...
        rows = len(self.islands_map)
        if rows == 0 :
            return 0
        cols = len(self.islands_map[0])
        no_of_islands = 0
        self.make_visited(rows, cols)

        # Iterate for all cells of the array
        for i in range(rows):
            for j in range(cols):
                if self.islands_map[i][j]==1 and not self.visited[i][j]:
                    no_of_islands += 1
                    BFS(self.islands_map, self.visited).process(i, j)

        return no_of_islands

    def make_visited(self, r, c):
        self.visited = [[False for x in range(c)] for y in range(r)]


def main():
    # ...
    islands_map = [
        [1, 1, 0, 1],
        [1, 0, 0, 0],
        [0, 0, 1, 0],
    ]

    # ...
    print(Solution(islands_map).get_num_of_the_islands())

if __name__ == '__main__':
    main()