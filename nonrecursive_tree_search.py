#!/usr/bin/env python3

# I usually think of depth-first tree search in terms of recursive function
# invocations, but we should be able to manage the node-stack ourselves instead
# of leaving it implicit in the call stack!

# Let's consider a tree where the leaf nodes have values, and, given a tree, we
# want to find the greatest value contained amongst its leaves.

import inspect
import logging
import sys
import unittest


class Node:
    def __init__(self, value, children=None):
        # assert that leaves have initial values and internal nodes do not
        if children is None:
            assert value is not None
        else:
            assert value is None

        self.value = value

        # default may be changed by parent Node's __init__ializer!
        self.parent = None

        if children is None:
            self.children = []
        else:
            self.children = children
            for child in children:
                child.parent = self

    def __repr__(self):
        return "<Node: id={} value={} ({} children)>".format(
            id(self), self.value, len(self.children))


def recursive_search(node,
                     # Yes, I know the gotcha about mutable default
                     # values. Wait for it ...
                     visit_order=[]):
    visit_order.append(node)
    if not node.children:
        return node.value
    else:
        return max(recursive_search(child)
                   for child in node.children)

def stack_search(root,
                 # Wait for it ...
                 visit_order=[]):
    stack = [root]
    while stack:
        node = stack.pop()
        visit_order.append(node)
        if not node.children:
            # propagate what we've learned up the tree
            messenger = node
            while (messenger.parent is not None and
                   (messenger.parent.value is None or
                    messenger.parent.value < messenger.value)):
                logging.debug(
                    "setting value of {} to {} because of child {}".format(
                        messenger.parent, messenger.value, messenger))
                messenger.parent.value = messenger.value
                messenger = messenger.parent
        else:
            for child in reversed(node.children):
                stack.append(child)
    return root.value


our_tree = Node(None,
                [Node(None,
                      [Node(None,
                            [Node(1),
                             Node(2),
                             Node(None,
                                  [Node(3),
                                   Node(None,
                                        [Node(4),
                                         Node(None,
                                              [Node(3)]),
                                         Node(2)])])])]),
                 Node(None,
                      [Node(None,
                            [Node(None,
                                  [Node(1),
                                   Node(2),
                                   Node(None,
                                        [Node(3)])])])])])


class RecursiveSearchTestCase(unittest.TestCase):
    def test_equivalence(self):
        search_methods = [recursive_search, stack_search]

        for search_method in search_methods:
            self.assertEqual(4, search_method(our_tree))

        self.assertEqual(
            # We have fun around here.
            *[inspect.signature(
                search_method).parameters['visit_order'].default
              for search_method in search_methods]
        )


if __name__ == "__main__":
    if sys.argv[1:]:
        arg, *_rest = sys.argv[1:]
    else:
        arg = None

    if arg == "debug":
        logging_kwargs = {'level': logging.DEBUG}
    else:
        logging_kwargs = {}

    sys.argv[1:] = []
    logging.basicConfig(**logging_kwargs)
    unittest.main()
