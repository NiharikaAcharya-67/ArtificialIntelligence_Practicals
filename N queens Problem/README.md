# N-Queens Problem (Backtracking)

A Python implementation of the classic **N-Queens Problem**, solved
using the **Backtracking** search technique.

---

## 1. Definition

The N-Queens Problem asks: given an `N x N` chessboard, can you place
`N` queens on it such that **no two queens attack each other**? In
chess, a queen can attack any other piece in the same row, same
column, or along any diagonal — so a valid solution must place every
queen in a way that avoids all three of these conflicts.

This is a classic example of a **Constraint Satisfaction Problem
(CSP)** — a problem where we must assign values (queen positions) to
variables (columns) while satisfying a set of constraints (no
attacks).

---

## 2. Problem Representation

- The board is represented as an `N x N` 2D list, where `1` means a
  queen is placed and `0` means the cell is empty.
- Queens are placed **one column at a time**, starting from column 0.
- Because exactly one queen is placed per column, we only ever need
  to check:
  - The same row (to the left, since columns to the right are still
    empty)
  - The upper-left diagonal
  - The lower-left diagonal

This reduces the number of checks needed at each step, since columns
ahead are guaranteed to be empty.

---

## 3. Features

- Solves the N-Queens problem for any board size `N`
- Uses **backtracking** — builds a solution step by step, and undoes
  ("backtracks") a choice as soon as it leads to a conflict
- Detects and reports when **no solution exists** (true for `N = 2`
  and `N = 3`)
- Displays the final board visually using `Q` for queens and `.` for
  empty cells
- Validates user input (N must be a positive whole number)

---

## 4. Uses in Artificial Intelligence

The N-Queens problem is a widely used teaching example in AI for
demonstrating:

- **Backtracking search** — a fundamental problem-solving strategy
  used when a problem must satisfy multiple constraints
  simultaneously
- **Constraint Satisfaction Problems (CSPs)** — used to model
  real-world problems like scheduling, timetabling, Sudoku, and
  resource allocation
- **State space search with pruning** — instead of generating every
  possible arrangement of queens, the algorithm prunes (cuts off)
  branches early as soon as a conflict is detected, making the search
  far more efficient than brute force
- A foundation before studying more advanced CSP techniques, such as
  forward checking, constraint propagation, and heuristics like
  **Minimum Remaining Values (MRV)**

---

## 5. Algorithm Overview (Backtracking)

**Steps:**

1. Start at column 0, with an empty board.
2. For the current column, try placing a queen in each row, one at a
   time:
   - Check if the position is **safe** (no other queen in the same
     row, or on the same upper-left or lower-left diagonal).
   - If safe, place the queen and move on to the next column
     (recursive call).
3. If placing a queen in the next column eventually fails for every
   row (no safe position found), **backtrack**: remove the queen just
   placed and try the next row in the current column.
4. If all `N` columns are successfully filled (`col == N`), a valid
   solution has been found.
5. If every possible placement has been tried and none succeed, no
   solution exists for that value of `N`.

This is a classic example of **Depth First Search combined with
pruning** — the algorithm explores one possible arrangement deeply,
and backs out as soon as it hits a dead end, instead of exploring
every possibility blindly.

---

## 6. Time Complexity

**O(N!)** in the worst case

Because for each column, the algorithm may try up to `N` rows, and
this branches out across `N` columns. In practice, the `is_safe`
pruning drastically cuts down the number of branches actually
explored, making it much faster than checking all `N^N` raw
placements — but the theoretical worst case remains factorial.

---

## 7. Space Complexity

**O(N²)**

This comes from:
- Storing the `N x N` board
- The recursion call stack, which can go as deep as `N` (one call per
  column)

---

## 8. How to Run

```bash
python nqueens.py
```

You will be asked to enter the value of `N` (the board size and
number of queens).

### Example Run (N = 4)

```
Enter the value of N: 4

Solution Found:

. . Q .
Q . . .
. . . Q
. Q . .
```

### Example: No Solution Case (N = 2 or N = 3)

```
Enter the value of N: 3

Note: No solution exists for N = 3.

No solution exists.
```

---

## 9. Advantages

- Much more efficient than brute force, since invalid placements are
  discarded early (pruning)
- Guaranteed to find a solution if one exists
- Simple and elegant to implement using recursion

## 10. Disadvantages

- Still has exponential/factorial worst-case time complexity for
  large `N`
- Does not find **all** possible solutions by default — it stops as
  soon as one valid solution is found
- Becomes slow for very large board sizes (e.g., N > 30) without
  further optimization (such as heuristics or symmetry reduction)

---

## Author

Niharika Acharya
