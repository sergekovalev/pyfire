import src.parser.ts.tokens as TOKENS


def parse_args(code, index_from, index_to):
    args = []

    code.set_index_from(index_from)
    
    args = code[index_from:index_to]
    
    code.set_index_from(0)
    
    return args


def parse_body(code, index_to):
    return []


def main(code, nodes, index_to):
    args_index_from = code.index(TOKENS.OPEN_BRACKET) + 1
    args_index_to = code.index(TOKENS.CLOSE_BRACKET, args_index_from, index_to)
    
    node = {
        'type': TOKENS.FUNCTION_DECLARATION,
        'name': code[1],
        'args': parse_args(
            code=code,
            index_from=args_index_from,
            index_to=args_index_to
        ),
        'body': parse_body(code, index_to)
    }
    
    nodes.append(node)
