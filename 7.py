from collections import deque

# Function to check if a state is valid
def valid(m_l, c_l, m_r, c_r):
    if (m_l >= 0 and m_r >= 0 and c_l >= 0 and c_r >= 0 and
        (m_l == 0 or m_l >= c_l) and (m_r == 0 or m_r >= c_r)):
        return True
    return False

# Function to generate the next possible states
def next_states(s):
    m_l, c_l, b = s
    m_r, c_r = 3 - m_l, 3 - c_l
    next_s = []
    if b == 1:  # Boat on the left side
        moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]  # People who can move
        for m, c in moves:
            new_m_l = m_l - m
            new_c_l = c_l - c
            new_m_r = m_r + m
            new_c_r = c_r + c
            if valid(new_m_l, new_c_l, new_m_r, new_c_r):
                next_s.append((new_m_l, new_c_l, 0))
    else:  # Boat on the right side
        moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]
        for m, c in moves:
            new_m_l = m_l + m
            new_c_l = c_l + c
            new_m_r = m_r - m
            new_c_r = c_r - c
            if valid(new_m_l, new_c_l, new_m_r, new_c_r):
                next_s.append((new_m_l, new_c_l, 1))
    return next_s

# Function to solve the problem using BFS
def bfs_mc():
    init_s = (3, 3, 1)
    goal_s = (0, 0, 0)
    q = deque([(init_s, [])])  # Queue holds (state, path)
    visited = set([init_s])

    while q:
        (s, p) = q.popleft()

        # Check if the goal is reached
        if s == goal_s:
            return p + [s]

        # Generate next possible states and add to the queue if not visited
        for next_s in next_states(s):
            if next_s not in visited:
                visited.add(next_s)
                q.append((next_s, p + [s]))

    return None  # No solution found

# Function to print the solution
def print_sol(sol):
    if sol:
        print("Solution found:")
        for step in sol:
            print(f"M left: {step[0]}, C left: {step[1]}, Boat: {'Left' if step[2] == 1 else 'Right'}")
    else:
        print("No solution found.")

# Solve the problem
sol = bfs_mc()
print_sol(sol)