
def code_map(Node) -> dict:
    if Node == None:
        return {}
    
    code_map = {}
    code_map[Node.symbol] = 0
    return code_map