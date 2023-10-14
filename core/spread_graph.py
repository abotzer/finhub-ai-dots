"""A spread graph is a directed acyclic graph where each node has a value that is computed from the values of its dependencies."""
from typing import List, Callable


class Node:
    """A node in the spread graph.
    
    @param dependencies: A list of nodes that this node depends on.
    @param evaluation: A function that takes in the dependencies and returns a the node's value.
    @param name: A string that identifies the node.
    """
    def __init__(self, dependencies: List, evaluation: Callable, name: str):
        self.dependencies = dependencies
        self.evaluation = evaluation
        self.name = name
        self.value = None
        self.evaluated = False

    def evaluate(self):
        """Evaluates the node and returns the value."""
        if self.value is None:
            self.value = self.evaluation(self.dependencies)
            self.evaluated = True
        return self.value

    def get_value(self):
        """Returns the value of the node."""
        return self.value

    def add_dependency(self, dependency):
        """Adds a dependency to the node."""
        self.dependencies.append(dependency)

    def remove_dependency(self, dependency):
        """Removes a dependency from the node."""
        self.dependencies.remove(dependency)

    def get_dependencies(self):
        """Returns the dependencies of the node."""
        return self.dependencies

    def dependencies_satisfied(self):
        """Returns true if the node has no dependencies or if all of its dependencies have been evaluated."""
        return len(self.dependencies) == 0 or all([dependency.evaluated for dependency in self.dependencies])

    def is_evaluated(self):
        """Returns true if the node has been evaluated."""
        return self.evaluated

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class SpreadGraph:
    """A spread graph is a directed acyclic graph where each node has a value that is 
    computed from the values of its dependencies
    
    @param nodes: A list of nodes in the graph
    """
    def __init__(self, nodes: List[Node]) -> None:
        self.nodes = nodes
    
    def evaluate(self):
        """Evaluates all nodes in the graph."""
        while any([not node.is_evaluated() for node in self.nodes]):
            ready_nodes = [node for node in self.nodes if node.dependencies_satisfied()]
            for node in ready_nodes:
                node.evaluate()
