from collections import deque
def is_goal(state, goal):
    return state == goal

def get_next_states(state, jug1_capacity, jug2_capacity):
    j1, j2 = state
    states = []
    states.append((jug1_capacity, j2))
    states.append((j1, jug2_capacity))
    states.append((0, j2))
    states.append((j1, 0))
    pour = min(j1, jug2_capacity - j2)
    states.append((j1 - pour, j2 + pour))
    pour = min(j2, jug1_capacity - j1)
    states.append((j1 + pour, j2 - pour))
    return states

def water_jug_bfs(jug1_capacity, jug2_capacity, initial_state, goal_state):
    visited = set()
    queue = deque([(initial_state, [])])

    while queue:
        state, path = queue.popleft()

        if is_goal(state, goal_state):
            return path + [state]  # Return the path including the goal state

        if state in visited:
            continue

        visited.add(state)

        for next_state in get_next_states(state, jug1_capacity, jug2_capacity):
            if next_state not in visited:
                queue.append((next_state, path + [state]))

    return None
   
jug1_capacity = int(input("Enter capacity of Jug 1: "))
jug2_capacity = int(input("Enter capacity of Jug 2: "))

initial_jug1 = int(input("Enter initial amount in Jug 1: "))
initial_jug2 = int(input("Enter initial amount in Jug 2: "))
initial_state = (initial_jug1, initial_jug2)

goal_jug1 = int(input("Enter goal amount in Jug 1: "))
goal_jug2 = int(input("Enter goal amount in Jug 2: "))
goal_state = (goal_jug1, goal_jug2)

result = water_jug_bfs(jug1_capacity, jug2_capacity, initial_state, goal_state)

if result:
    for step in result:
        print(step)
else:
    print("No solution found.")