from compression_tool.tree import Node, InternalNode


def build_code_map(node: Node) -> dict:
    if node == None:
        return {}
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