class Tree_Traversal(object):
    """
    Base class for Tree Traversals.

    """

    def __init__(self, unsorted_tree):
        """
        Initialises a tree.
        :param tree_dict: input dictionary, containing tree branches as keys
            Example: {('1', '2'):1, ('2', '8'):1, ('1', '3'):1}
        """
        self.unsorted_tree = unsorted_tree
        self.sorted_tree = dict()
        self.root_node = self.find_starting_node()
        self.sort_sankey(self.root_node)

    def find_starting_node(self):
        """
        Finds a root of the tree.
        :return: root node
        """
        uniq_nodes = set()
        uniq_child_nodes = set()
        for key, value in self.unsorted_tree.items():
            parent, child = key[0], key[1]
            uniq_nodes.update(parent, child)
            uniq_child_nodes.update(key[1])
        for node in uniq_nodes:
            if node not in uniq_child_nodes:
                return node

    def sort_sankey(self, start):
        """
        If Splunk Sankey diagram is displayed as a table, it is unsorted.
            This function sorts the Sankey diagram tree branches and displays them in the order
            left to right and top to bottom.
        :param start: Root node as returned by find_starting_node() function
        :return: None
        """
        start_keys = list()
        for key, value in self.unsorted_tree.items():
            parent, child = key[0], key[1]
            if parent == start:
                self.sorted_tree[key] = value
                start_keys.append(child)
        for st_key in start_keys:
            self.sort_sankey(st_key)


if __name__ == "__main__":

    unsorted_tree = {('1', '2'):1, ('2', '8'):1, ('1', '3'):1,
                     ('3', '4'):1, ('4', '9'):1, ('9', '22'):1,
                     ('4', '23'):1, ('3', '5'):1, ('3', '6'):1,
                     ('1', '7'):1}

    T = Tree_Traversal(unsorted_tree)
    print(T.sorted_tree)
