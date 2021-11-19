# Introductory Python Course 2021 - UiT
# By Brett Alistair Kromkamp (brettkromkamp@gmail.com - https://brettkromkamp.com)
#
# An alternative and slightly more advanced Python tree implementation is available,
# here: https://github.com/brettkromkamp/typed-tree
#
# Example tree:
# Harry
#          Jane
#                  Joe
#                  Diane
#                          George
#                                  Jill
#                                          Carol
#                          Mary
#                  Mark
#          Bill
#                  Grace

from enum import Enum


# --------------------------------------------------------------------------------
class TraversalMode(Enum):
    DEPTH = 1
    BREADTH = 2


# --------------------------------------------------------------------------------
class Node:
    def __init__(self, identifier, name):
        self.identifier = identifier
        self.name = name
        self.children = []

    def add_child(self, identifier):
        self.children.append(identifier)


# --------------------------------------------------------------------------------
class Tree:
    def __init__(self):
        self.nodes = {}

    def add_node(self, identifier, parent=None, name="Undefined"):
        node = Node(identifier, name)
        self[identifier] = node

        if parent:
            self[parent].add_child(identifier)

        return node

    def display(self, identifier, depth=0):
        node = self[identifier]
        children = node.children
        if depth:
            print("\t" * depth, f"{node.name}")
        else:
            print(f"{node.name}")

        depth += 1
        for child in children:
            self.display(child, depth)  # Recursive call

    def traverse(self, identifier, mode=TraversalMode.DEPTH):
        yield self[identifier]
        queue = self[identifier].children
        while queue:
            yield self[queue[0]]
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

    tree.add_node("harry", name="Harry")  # Root node
    tree.add_node("jane", parent="harry", name="Jane")
    tree.add_node("bill", parent="harry", name="Bill")
    tree.add_node("joe", parent="jane", name="Joe")
    tree.add_node("diane", parent="jane", name="Diane")
    tree.add_node("george", parent="diane", name="George")
    tree.add_node("mary", parent="diane", name="Mary")
    tree.add_node("jill", parent="george", name="Jill")
    tree.add_node("carol", parent="jill", name="Carol")
    tree.add_node("grace", parent="bill", name="Grace")
    tree.add_node("mark", parent="jane", name="Mark")

    tree.display("harry")
    print("***** DEPTH-FIRST ITERATION *****")
    for node in tree.traverse("harry"):
        print(node.name)
    print("***** BREADTH-FIRST ITERATION *****")
    for node in tree.traverse("harry", mode=TraversalMode.BREADTH):
        print(node.name)
    print("***** EMULATING CONTAINER TYPES *****")
    print(tree["harry"].name)
