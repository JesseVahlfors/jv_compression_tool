"""Node classes used to represent Huffman trees (Leaf and Internal nodes)."""

class Node:
    """
    Huffman tree node (base class).

    Nodes compare by weight; if two nodes share the same weight,
    ordering falls back to object identity to ensure a deterministic sort order.
    
    """

    __slots__ = ("weight", "is_leaf")
    def __init__(self, weight: int, is_leaf: bool = False) -> None:
        self.weight = weight
        self.is_leaf = is_leaf

    def __lt__(self, other: "Node") -> bool:
        if self.weight != other.weight:
            return self.weight < other.weight
        
        return id(self) < id(other)

    def __repr__(self) -> str:
        kind = "Leaf" if self.is_leaf else "Internal"
        return f"{kind}(weight={self.weight})"
        

class LeafNode(Node):
    """
    Leaf node representing a single symbol in the Huffman tree.

    Attributes:
        symbol (int): The byte/symbol value (0-255).
        weight (int): The symbol's frequency count.

    """
    __slots__ = ("symbol",)

    def __init__(self, symbol: int, weight: int) -> None:
        super().__init__(weight=weight, is_leaf=True)
        self.symbol = symbol

    def __repr__(self) -> str:
        return f"Leaf(symbol={self.symbol}, weight={self.weight})"

class InternalNode(Node):
    """
    Internal node representing the combination of two child nodes.

    Its weight is the sum of its children's weights.

    """
    __slots__ = ("left", "right")
    def __init__(self, left: Node, right: Node) -> None:
        super().__init__(weight=left.weight + right.weight, is_leaf=False)
        self.left = left
        self.right = right
