from compression_tool.tree import Node, InternalNode


def build_code_map(node: Node) -> dict:
    if node == None:
        return {}
    if not isinstance(node, Node):
        raise TypeError(f"root is not a Node instance: {node!r} ")
    map = {}
    prefix=''

    def code_builder(node: Node, prefix: str, map: dict):    
        if node.is_leaf:
            map[node.symbol] = prefix
        if isinstance(node, InternalNode):
            code_builder(node.left, prefix + "0", map)
            code_builder(node.right, prefix + "1", map)
    
    code_builder(node, prefix, map)
    
    return map