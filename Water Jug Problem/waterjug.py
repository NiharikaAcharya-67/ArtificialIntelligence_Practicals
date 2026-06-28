"""
Water Jug Problem (State Space Search)
---------------------------------------
AI Practical - Uninformed Search Algorithm
Author : Niharika Acharya
Algorithm : Breadth-First Search (BFS)
Language : Python 3
"""

from collections import deque


def water_jug_bfs(jug1_capacity, jug2_capacity, goal):
    """
    Solves the Water Jug Problem using Breadth-First Search (BFS).

    State Representation:
        (x, y)
        x = amount of water in Jug 1
        y = amount of water in Jug 2
    """

    # Queue stores (current_state, path_taken)
    queue = deque()
    queue.append(((0, 0), [(0, 0)]))

    # To avoid visiting the same state again
    visited = set()
    visited.add((0, 0))

    while queue:
        (jug1, jug2), path = queue.popleft()

        # Goal Test
        if jug1 == goal or jug2 == goal:
            return path

        # Generate all possible next states
        next_states = [

            # Fill Jug 1
            (jug1_capacity, jug2),

            # Fill Jug 2
            (jug1, jug2_capacity),

            # Empty Jug 1
            (0, jug2),

            # Empty Jug 2
            (jug1, 0),

            # Pour Jug 1 -> Jug 2
            (
                jug1 - min(jug1, jug2_capacity - jug2),
                jug2 + min(jug1, jug2_capacity - jug2)
            ),

            # Pour Jug 2 -> Jug 1
            (
                jug1 + min(jug2, jug1_capacity - jug1),
                jug2 - min(jug2, jug1_capacity - jug1)
            )
        ]

        # Visit each new state
        for state in next_states:
            if state not in visited:
                visited.add(state)
                queue.append((state, path + [state]))

    return None


def get_positive_integer(prompt):
    """
    Keep asking the user for input until a positive integer is given.
    Prevents the program from crashing or behaving oddly on bad input.
    """
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Please enter a number greater than 0.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a whole number.")


# ------------------- Main Program -------------------

jug1 = get_positive_integer("Enter capacity of Jug 1: ")
jug2 = get_positive_integer("Enter capacity of Jug 2: ")
goal = get_positive_integer("Enter goal amount: ")

if goal > max(jug1, jug2):
    print("\nGoal amount cannot be greater than both jug capacities.")
else:
    solution = water_jug_bfs(jug1, jug2, goal)

    if solution:
        print("\nShortest Solution (Using BFS):\n")

        for i, state in enumerate(solution):
            print(f"Step {i}: {state}")

    else:
        print("\nNo solution exists.")
