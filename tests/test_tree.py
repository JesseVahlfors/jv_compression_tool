from src.compression_tool.tree import Node, LeafNode, InternalNode

def test_node_initialization():
    node = Node(weight=5)
    assert node.weight == 5
    assert node.is_leaf == False

def test_leafnode_initialization():
    leaf = LeafNode(symbol=97, weight=3)
    assert leaf.symbol == 97
    assert leaf.weight == 3
    assert leaf.is_leaf == True

def test_internalnode_initialization():
    left = LeafNode(symbol = 97, weight = 3)
    right = LeafNode(symbol = 80, weight = 5)
    internal = InternalNode(left, right)

    assert internal.weight == 8
    assert left == left
    assert right == right
    assert internal.is_leaf == False

def test_node_comparison():
    n1 = Node(weight=2)
    n2 = Node(weight=5)

    assert n1 < n2

def test_repr_on_nodes():
    node1 = Node(weight=7)
    l = LeafNode(symbol = 97, weight = 3)
    r = LeafNode(symbol = 80, weight = 5)
    internal_node = InternalNode(l, r)

    assert repr(node1) == "Internal(weight=7)"
    assert repr(l) == "Leaf(symbol=97, weight=3)"
    assert repr(internal_node) == "Internal(weight=8)"