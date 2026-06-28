# Depth First Search (DFS)

A Python implementation of the **Depth First Search (DFS)** algorithm,
where the user enters their own graph/tree and the program finds the
DFS traversal order.

---

## 1. Definition

Depth First Search (DFS) is an **uninformed (blind) search algorithm**
used to traverse or search a graph or tree. It starts at a chosen node
(called the *root* or *start node*) and explores as far as possible
along each branch before backtracking — going **deep into one path
first**, rather than exploring level by level.

It uses a **stack (LIFO – Last In, First Out)** data structure (either
explicitly, or implicitly through recursion) to decide which node to
visit next, and a **visited set** to make sure no node is processed
more than once.

---

## 2. Features

- Explores as deep as possible along one path before backtracking
- Memory-efficient compared to BFS for deep graphs (doesn't need to
  store an entire level at once)
- Never revisits a node (no infinite loops, even in cyclic graphs)
- Works on both **graphs** and **trees**
- Can handle disconnected nodes safely
- Can be implemented using either a stack or recursion
- The user can input their own custom graph instead of a fixed one

---

## 3. Uses in Artificial Intelligence

DFS is one of the foundational **uninformed search strategies** in AI,
used as a base technique for exploring a problem's entire state space.
Common AI applications include:

- **State-space search** — exploring all possible states of a problem
  (e.g., puzzle solving, maze solving) when memory is limited
- **Backtracking algorithms** — used in problems like the N-Queens
  problem, Sudoku solvers, and constraint satisfaction problems
- **Topological sorting** — ordering tasks based on dependencies
  (e.g., scheduling, build systems)
- **Cycle detection** — checking whether a graph contains a cycle
- **Maze and pathfinding problems** — exploring one path fully before
  trying another
- **Game tree exploration** — exploring possible move sequences in
  games (e.g., minimax algorithm)
- Used as a **building block** for more advanced search and
  optimization algorithms

---

## 4. Algorithm Overview

**Steps:**

1. Start at the given start node and push it onto a stack.
2. While the stack is not empty:
   - Pop the top node from the stack — this is the *current node*.
   - If it has not been visited, mark it visited and add it to the
     traversal result.
   - Push all of its unvisited neighbors onto the stack.
3. Repeat until the stack is empty.
4. Return the traversal order.

Because the most recently added node is always explored next (LIFO),
DFS dives deep into one branch before backtracking to explore others.

---

## 5. Time Complexity

**O(V + E)**

Where:
- `V` = number of vertices (nodes)
- `E` = number of edges

This is because every node is visited once (`V`), and every edge is
checked once when exploring neighbors (`E`).

---

## 6. Space Complexity

**O(V)**

This comes from:
- The `visited` set, which can store up to all `V` nodes
- The `stack` (or call stack, if implemented recursively), which in
  the worst case (e.g., a long single path) can hold up to `V` nodes
  at once

---

## 7. How to Run

```bash
python dfs.py
```

You will be asked to enter the graph's edges one at a time, then the
starting node.

### Example Run

```
Enter the edges of your graph/tree.
Format: SourceNode DestinationNode   (example: A B)
Type 'done' when you are finished.

Edge (or 'done'): A B
Edge (or 'done'): A C
Edge (or 'done'): B D
Edge (or 'done'): B E
Edge (or 'done'): C F
Edge (or 'done'): C G
Edge (or 'done'): done

Depth First Search Traversal
------------------------------
Available nodes: A, B, C, D, E, F, G
Enter the starting node: A

Traversal order:
A -> B -> D -> E -> C -> F -> G
```

---

## 8. Advantages

- Uses less memory than BFS for deep graphs, since it doesn't need to
  store an entire level of nodes at once
- Simple to implement, especially using recursion
- Well suited for problems involving backtracking

## 9. Disadvantages

- Does **not** guarantee the shortest path (unlike BFS)
- Can go very deep down one path before realizing it's a dead end,
  which can be slow on large or infinite graphs
- May get stuck exploring a long, irrelevant branch before reaching
  the actual goal

---

## BFS vs DFS (Quick Comparison)

| Aspect              | BFS                          | DFS                          |
|---------------------|-------------------------------|-------------------------------|
| Data structure      | Queue (FIFO)                  | Stack (LIFO) / Recursion      |
| Exploration style   | Level by level (breadth-wise) | Path by path (depth-wise)     |
| Shortest path        | Guaranteed (unweighted graph) | Not guaranteed                |
| Memory usage         | Can be high (stores a level)  | Generally lower                |
| Time complexity       | O(V + E)                      | O(V + E)                      |
| Space complexity      | O(V)                          | O(V)                          |

---

## Author

Niharika Acharya
