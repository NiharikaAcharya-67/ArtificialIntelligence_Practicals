"""
Breadth First Search (BFS)
--------------------------
AI Practical - Uninformed Search Algorithm
Author : Niharika Acharya
Algorithm : Breadth First Search (BFS)
Language : Python 3
"""

from collections import deque
from typing import Dict, List, Set


class Graph:
    """Graph represented using an adjacency list."""

    def __init__(self) -> None:
        self.adjacency_list: Dict[str, List[str]] = {}

    def add_edge(self, source: str, destination: str) -> None:
        """
        Add a directed edge to the graph.

        Args:
            source: Starting node
            destination: Ending node
        """
        self.adjacency_list.setdefault(source, []).append(destination)
        self.adjacency_list.setdefault(destination, [])

    def breadth_first_search(self, start_node: str) -> List[str]:
        """
        Perform Breadth First Search traversal.

        Args:
            start_node: Starting node for BFS

        Returns:
            List of visited nodes in BFS order.
        """
        if start_node not in self.adjacency_list:
            raise ValueError(f"'{start_node}' does not exist in the graph.")

        visited: Set[str] = set()
        traversal: List[str] = []
        queue: deque = deque([start_node])
        visited.add(start_node)

        while queue:
            current_node = queue.popleft()
            traversal.append(current_node)

            for neighbor in self.adjacency_list[current_node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return traversal


def build_graph_from_user() -> Graph:
    """
    Build a graph using edges typed in by the user.

    The user enters one edge at a time as "A B" (meaning A -> B),
    and types "done" when finished.
    """
    graph = Graph()

    print("Enter the edges of your graph/tree.")
    print("Format: SourceNode DestinationNode   (example: A B)")
    print("Type 'done' when you are finished.\n")

    while True:
        edge_input = input("Edge (or 'done'): ").strip()

        if edge_input.lower() == "done":
            break

        parts = edge_input.split()
        if len(parts) != 2:
            print("Please enter exactly two node names separated by a space.")
            continue

        source, destination = parts[0].upper(), parts[1].upper()
        graph.add_edge(source, destination)

    return graph


def main() -> None:
    """Program entry point."""
    graph = build_graph_from_user()

    if not graph.adjacency_list:
        print("\nNo edges were entered. Exiting.")
        return

    print("\nBreadth First Search Traversal")
    print("------------------------------")
    print("Available nodes:", ", ".join(graph.adjacency_list.keys()))

    start_node = input("Enter the starting node: ").strip().upper()

    try:
        traversal = graph.breadth_first_search(start_node)
        print("\nTraversal order:")
        print(" -> ".join(traversal))
    except ValueError as error:
        print(f"\nError: {error}")


if __name__ == "__main__":
    main()
