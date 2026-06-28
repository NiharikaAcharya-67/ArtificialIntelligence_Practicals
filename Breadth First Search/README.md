# Breadth First Search (BFS)

A Python implementation of the **Breadth First Search (BFS)** algorithm,
where the user enters their own graph/tree and the program finds the
BFS traversal order.

---

## 1. Definition

Breadth First Search (BFS) is an **uninformed (blind) search
algorithm** used to traverse or search a graph or tree. It starts at
a chosen node (called the *root* or *start node*) and explores all of
its neighboring nodes first, before moving on to the neighbors of
those neighbors — exploring the graph **level by level** (breadth-wise),
rather than going deep into one path first.

It uses a **queue (FIFO – First In, First Out)** data structure to
decide which node to visit next, and a **visited set** to make sure no
node is processed more than once.

---

## 2. Features

- Explores nodes level by level (breadth-wise)
- Guarantees the **shortest path** between two nodes in an unweighted
  graph
- Never revisits a node (no infinite loops, even in cyclic graphs)
- Works on both **graphs** and **trees**
- Can handle disconnected nodes safely
- Simple to implement using a queue
- The user can input their own custom graph instead of a fixed one

---

## 3. Uses in Artificial Intelligence

BFS is one of the foundational **uninformed search strategies** taught
in AI, used as a base for solving search problems where the path cost
is not known or all edges are considered equal. Common AI applications
include:

- **State-space search** — exploring all possible states of a problem
  (e.g., puzzle solving, maze solving)
- **Finding the shortest solution path** in problems like the 8-puzzle,
  water-jug problem, or maze navigation
- **Web crawlers** — exploring links level by level starting from a
  homepage
- **Social network analysis** — finding degrees of connection (e.g.,
  "friends of friends")
- **Robotics & pathfinding** — exploring possible moves before
  deciding an action
- Used as a **building block** for more advanced informed search
  algorithms (like A*, which build on these same traversal ideas with
  added heuristics)

---

## 4. Algorithm Overview

**Steps:**

1. Start at the given start node.
2. Mark the start node as visited and add it to a queue.
3. While the queue is not empty:
   - Remove (dequeue) the front node — this is the *current node*.
   - Add it to the traversal result.
   - For each neighbor of the current node:
     - If the neighbor has not been visited, mark it visited and add
       it to the queue.
4. Repeat until the queue is empty.
5. Return the traversal order.

Because all neighbors at the current level are added to the queue
before moving to the next level, BFS guarantees that nodes closer to
the start node are visited first.

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
- The `queue`, which in the worst case (e.g., a wide graph) can hold
  up to `V` nodes at once

---

## 7. How to Run

```bash
python bfs.py
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

Breadth First Search Traversal
------------------------------
Available nodes: A, B, C, D, E, F, G
Enter the starting node: A

Traversal order:
A -> B -> C -> D -> E -> F -> G
```

---

## 8. Advantages

- Simple and easy to implement
- Guarantees the shortest path in unweighted graphs
- Complete — will always find a solution if one exists (in a finite
  graph)

## 9. Disadvantages

- Can use a lot of memory for large graphs, since it stores all nodes
  at the current level
- Slower than informed search algorithms (like A*) when a good
  heuristic is available, since BFS doesn't use any extra
  problem-specific knowledge

---

## Author

Niharika Acharya
