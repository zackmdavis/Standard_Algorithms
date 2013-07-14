require '../binary_search_tree'

my_tree = BinarySearchTree.new(Node.new(5, nil, nil, nil))
my_tree.insert(Node.new(2, nil, nil, nil))
my_tree.insert(Node.new(7, nil, nil, nil))
my_tree.insert(Node.new(3, nil, nil, nil))
my_tree.insert(Node.new(6, nil, nil, nil))
my_tree.insert(Node.new(4, nil, nil, nil))
my_tree.insert(Node.new(1, nil, nil, nil))
my_tree.inorder_walk(my_tree.root)
two = my_tree.search(2)
two.inspect
my_tree.delete(two)
my_tree.inorder_walk(my_tree.root)
my_tree.minimum.inspect
my_tree.maximum.inspect
my_tree.successor(my_tree.search(5)).inspect
