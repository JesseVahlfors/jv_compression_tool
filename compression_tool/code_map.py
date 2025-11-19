"""code map building utilities."""
from compression_tool.tree import Node


def build_code_map(node: Node) -> dict[int, str]:
    """
    Build a code map from the root of a Huffman tree.

    Each leaf node is assigned a binary code determined by the path taken
    from the root: going left appends "0" and going right appends "1".
    The function performs a recursive traversal to collect all codes.

    Special case:
        If the tree contains only a single symbol (a single leaf node),
        the code assigned is the empty string "".

    Args: 
        node: The root node of a Huffman tree.

    Returns: 
        A dictionary mapping symbols (0-255) to their Huffman codes
        as strings of "0" and "1".

    Raises:
        TypeError: If 'node' is not an instance of Node.
    """

    if node == None:
        return {}
    
    if not isinstance(node, Node):
        raise TypeError(f"root is not a Node instance: {node!r} ")
    
    if node.is_leaf:
        return {node.symbol: ""}
    
    code_map: dict[int, str] = {}

    def code_builder(node: Node, prefix: str):    
        if node.is_leaf:
            code_map[node.symbol] = prefix
        else:
            code_builder(node.left, prefix + "0")
            code_builder(node.right, prefix + "1")
    
    code_builder(node, "")
    
    return code_map