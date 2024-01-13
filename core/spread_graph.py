"""A spread graph is a directed acyclic graph where each node has a value that is computed from the values of its dependencies."""
from typing import List, Callable
import uuid


class Node:
    """A node in the spread graph.
    
    @param dependencies: A list of nodes that this node depends on.
    @param evaluation: A function that takes in the dependencies and returns a the node's value.
    @param name: A string that identifies the node.
    """
    def __init__(self, description: str, dependencies: List, evaluation: Callable, name: str):
        self.id = uuid.uuid1()
        self.description = description
        self.dependencies = dependencies
        self.evaluation = evaluation
        self.name = name
        self.value = None
        self.is_evaluated = False

    def __eq__(self, __value: 'Node') -> bool:
        return self.id == __value.id

    @property
    def description(self):
        """Returns the description of the node."""
        return self.description

    def evaluate(self):
        """Evaluates the node and returns the value."""
        if self.value is None:
            self.value = self.evaluation(self.dependencies)
            self.is_evaluated = True
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

    def update_evaluation(self, evaluation: Callable):
        """Updates the evaluation function of the node."""
        self.evaluation = evaluation
        self.is_evaluated = False

    @property
    def is_evaluated(self):
        """Returns true if the node has been evaluated."""
        return self.is_evaluated

    @is_evaluated.setter
    def is_evaluated(self, value: bool):
        """Sets the evaluated property of the node."""
        self.is_evaluated = value

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

    def add_node(self, node: Node):
        """Adds a node to the graph."""
        self.nodes.append(node)

    def remove_node(self, node: Node):
        """Removes a node from the graph."""
        self.nodes.remove(node)