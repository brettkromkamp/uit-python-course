# Introductory Python Course 2021 - UiT
# By Brett Alistair Kromkamp (brettkromkamp@gmail.com - https://brettkromkamp.com)
#
# A more up-to-date Python tree implementation is available,
# here: https://github.com/brettkromkamp/typed-tree

from enum import Enum


# --------------------------------------------------------------------------------
class TraversalMode(Enum):
    DEPTH = 1
    BREADTH = 2


# --------------------------------------------------------------------------------
class Node:
    def __init__(self, identifier):
        self.identifier = identifier
        self.children = []

    def add_child(self, identifier):
        self.children.append(identifier)


# --------------------------------------------------------------------------------
class Tree:
    def __init__(self):
        self.nodes = {}

    def add_node(self, identifier, parent=None):
        node = Node(identifier)
        self[identifier] = node

        if parent is not None:
            self[parent].add_child(identifier)

        return node

    def display(self, identifier, depth=0):
        children = self[identifier].children
        if depth == 0:
            print(f"{identifier}")
        else:
            print("\t" * depth, f"{identifier}")

        depth += 1
        for child in children:
            self.display(child, depth)  # Recursive call

    def traverse(self, identifier, mode=TraversalMode.DEPTH):
        yield identifier
        queue = self[identifier].children
        while queue:
            yield queue[0]
            expansion = self[queue[0]].children
            if mode == TraversalMode.DEPTH:
                queue = expansion + queue[1:]  # Depth-first traversal
            elif mode == TraversalMode.BREADTH:
                queue = queue[1:] + expansion  # Width-first traversal

    # https://docs.python.org/3/reference/datamodel.html#emulating-container-types
    def __getitem__(self, key):
        return self.nodes[key]

    def __setitem__(self, key, item):
        self.nodes[key] = item

    def __len__(self):
        return len(self.nodes)


if __name__ == "__main__":
    tree = Tree()

    tree.add_node("harry")  # root node
    tree.add_node("jane", "harry")
    tree.add_node("bill", "harry")
    tree.add_node("joe", "jane")
    tree.add_node("diane", "jane")
    tree.add_node("george", "diane")
    tree.add_node("mary", "diane")
    tree.add_node("jill", "george")
    tree.add_node("carol", "jill")
    tree.add_node("grace", "bill")
    tree.add_node("mark", "jane")

    tree.display("harry")
    print("***** DEPTH-FIRST ITERATION *****")
    for node in tree.traverse("harry"):
        print(node)
    print("***** BREADTH-FIRST ITERATION *****")
    for node in tree.traverse("harry", mode=TraversalMode.BREADTH):
        print(node)
    print("***** EMULATING CONTAINER TYPES *****")
    print(tree["harry"].identifier)
