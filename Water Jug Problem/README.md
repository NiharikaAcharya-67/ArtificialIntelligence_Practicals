# Water Jug Problem (State Space Search)

A Python implementation of the classic **Water Jug Problem**, solved
using **Breadth-First Search (BFS)** over the problem's state space.

---

## 1. Definition

The Water Jug Problem is a classic AI search problem. You are given
two jugs of fixed capacities (with no measuring marks), and an
unlimited water supply. The goal is to find a sequence of steps
(filling, emptying, or pouring water between jugs) that results in
exactly a **goal amount** of water in either jug.

This problem is a great example of how a real-world puzzle can be
represented as a **state space search problem**, where each state
represents a snapshot of the world, and search algorithms (like BFS)
are used to find a path from the start state to a goal state.

---

## 2. State Space Representation

Each **state** is represented as a tuple:

```
(x, y)
```

- `x` = current amount of water in Jug 1
- `y` = current amount of water in Jug 2

The **start state** is always `(0, 0)` — both jugs empty.

The **goal state** is reached when either `x == goal` or `y == goal`.

### Possible actions (state transitions) from any state `(x, y)`:

| Action               | Resulting state                                                    |
|----------------------|----------------------------------------------------------------------|
| Fill Jug 1            | `(jug1_capacity, y)`                                                |
| Fill Jug 2            | `(x, jug2_capacity)`                                                |
| Empty Jug 1            | `(0, y)`                                                            |
| Empty Jug 2            | `(x, 0)`                                                            |
| Pour Jug 1 → Jug 2     | Pour until Jug 1 is empty or Jug 2 is full, whichever happens first |
| Pour Jug 2 → Jug 1     | Pour until Jug 2 is empty or Jug 1 is full, whichever happens first |

Each action generates a new state, forming a **state space graph** —
which is exactly what BFS traverses to find the goal.

---

## 3. Features

- Models a real-world puzzle as a state space search problem
- Uses BFS to guarantee the **shortest sequence of steps** to the goal
- Avoids revisiting the same state (no infinite loops)
- Detects and reports when **no solution exists**
- Validates user input (capacities and goal must be positive numbers)
- User can input their own jug capacities and goal amount

---

## 4. Uses in Artificial Intelligence

The Water Jug Problem is a classic teaching example used to
demonstrate:

- **State space representation** — how a real-world problem can be
  modeled as states, actions, and transitions
- **Uninformed search** — solving a problem without any
  problem-specific heuristic, relying purely on systematic
  exploration (BFS)
- **Search tree / search graph concepts** — visualizing how a
  starting state branches into many possible future states
- **Goal-based agents** — an agent whose actions are driven by
  reaching a defined goal state
- Foundational understanding before moving to **informed search**
  algorithms (like A*) that use heuristics to search more efficiently

---

## 5. Algorithm Overview (BFS Applied to the Water Jug Problem)

**Steps:**

1. Start at state `(0, 0)` and add it to a queue, along with the path
   taken to reach it (initially just itself).
2. Mark `(0, 0)` as visited.
3. While the queue is not empty:
   - Remove (dequeue) the front state.
   - If either jug's amount equals the goal, return the path — this
     is the shortest solution.
   - Otherwise, generate all 6 possible next states (fill, empty, or
     pour, as described above).
   - For each next state not already visited, mark it visited and
     add it to the queue along with the updated path.
4. If the queue becomes empty without finding the goal, no solution
   exists.

Because BFS explores states level by level, the first time the goal
is reached, it is guaranteed to be via the **shortest possible
sequence of actions**.

---

## 6. Time Complexity

**O(C1 × C2)**

Where:
- `C1` = capacity of Jug 1
- `C2` = capacity of Jug 2

This is because the total number of possible states is bounded by
`(C1 + 1) × (C2 + 1)` — every combination of water levels in both
jugs — and BFS visits each state at most once.

---

## 7. Space Complexity

**O(C1 × C2)**

This comes from:
- The `visited` set, which can store up to all possible states
- The `queue`, which can hold multiple states (along with their paths)
  at once

---

## 8. How to Run

```bash
python waterjug.py
```

You will be asked to enter the capacity of Jug 1, Jug 2, and the goal
amount of water.

### Example Run

```
Enter capacity of Jug 1: 4
Enter capacity of Jug 2: 3
Enter goal amount: 2

Shortest Solution (Using BFS):

Step 0: (0, 0)
Step 1: (0, 3)
Step 2: (3, 0)
Step 3: (3, 3)
Step 4: (4, 2)
```

### Example: No Solution Case

If the goal amount cannot be reached with the given jug capacities
(based on the mathematical rule that only multiples of
`gcd(jug1_capacity, jug2_capacity)` are reachable), the program will
print:

```
No solution exists.
```

---

## 9. Advantages

- Guarantees the shortest solution, since BFS explores level by level
- Simple and systematic — does not rely on guesswork or heuristics
- Easily adaptable to jugs of any capacity

## 10. Disadvantages

- Can become slow and memory-heavy for very large jug capacities,
  since the number of possible states grows with `C1 × C2`
- Does not use any problem-specific knowledge to search smarter or
  faster (that would require an informed search algorithm)

---

## Author

Niharika Acharya
