import heapq

class PuzzleState:
    def __init__(self, board, moves=0, previous=None):
        self.board = board
        self.moves = moves
        self.previous = previous
        self.zero_pos = board.index(0)

    def __lt__(self, other):
        return (self.moves + self.manhattan_distance()) < (other.moves + other.manhattan_distance())

    def manhattan_distance(self):
        distance = 0
        for i, value in enumerate(self.board):
            if value == 0:
                continue
            target_x, target_y = divmod(value, 3)
            current_x, current_y = divmod(i, 3)
            distance += abs(target_x - current_x) + abs(target_y - current_y)
        return distance

    def is_goal(self, goal):
        return self.board == goal

    def get_neighbors(self):
        neighbors = []
        x, y = divmod(self.zero_pos, 3)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
       
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                new_pos = nx * 3 + ny
                new_board = self.board[:]
                new_board[self.zero_pos], new_board[new_pos] = new_board[new_pos], new_board[self.zero_pos]
                neighbors.append(PuzzleState(new_board, self.moves + 1, self))
        return neighbors

def astar_solver(initial, goal):
    open_list = []
    closed_set = set()
    heapq.heappush(open_list, PuzzleState(initial))
   
    while open_list:
        current = heapq.heappop(open_list)

        if current.is_goal(goal):
            return current

        closed_set.add(tuple(current.board))

        for neighbor in current.get_neighbors():
            if tuple(neighbor.board) in closed_set:
                continue
            heapq.heappush(open_list, neighbor)

    return None

def print_solution(solution):
    path = []
    while solution:
        path.append(solution.board)
        solution = solution.previous
    path.reverse()
   
    for step in path:
        print_board(step)

def print_board(board):
    for i in range(0, 9, 3):
        print(board[i:i+3])
    print()

if __name__ == "__main__":
    initial = list(map(int, input("Enter the initial state (9 numbers 0-8): ").split()))
    goal = list(map(int, input("Enter the goal state (9 numbers 0-8): ").split()))
   
    solution = astar_solver(initial, goal)
   
    if solution:
        print("Solution found! Sequence of moves:")
        print_solution(solution)
    else:
        print("No solution found.")