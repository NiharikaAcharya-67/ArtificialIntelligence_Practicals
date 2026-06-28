"""
Depth First Search (DFS)
--------------------------
AI Practical - Uninformed Search Algorithm
Author : Niharika Acharya
Algorithm : Depth First Search (DFS)
Language : Python 3
"""

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

    def depth_first_search(self, start_node: str) -> List[str]:
        """
        Perform Depth First Search traversal.

        Args:
            start_node: Starting node for DFS

        Returns:
            List of visited nodes in DFS order.
        """
        if start_node not in self.adjacency_list:
            raise ValueError(f"'{start_node}' does not exist in the graph.")

        visited: Set[str] = set()
        traversal: List[str] = []
        stack: List[str] = [start_node]

        while stack:
            current_node = stack.pop()

            if current_node not in visited:
                visited.add(current_node)
                traversal.append(current_node)

                # Reverse neighbors so they are visited in the same
                # left-to-right order they were added (since a stack
                # is LIFO - Last In, First Out).
                for neighbor in reversed(self.adjacency_list[current_node]):
                    if neighbor not in visited:
                        stack.append(neighbor)

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

    print("\nDepth First Search Traversal")
    print("------------------------------")
    print("Available nodes:", ", ".join(graph.adjacency_list.keys()))

    start_node = input("Enter the starting node: ").strip().upper()

    try:
        traversal = graph.depth_first_search(start_node)
        print("\nTraversal order:")
        print(" -> ".join(traversal))
    except ValueError as error:
        print(f"\nError: {error}")


if __name__ == "__main__":
    main()
