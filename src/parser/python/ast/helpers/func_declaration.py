import src.parser.ts.tokens as TOKENS


def main(code, nodes, index_to):
    node = {
        'type': TOKENS.FUNCTION_DECLARATION,
        'body': {
            'name': code[1],
        }
    }
    
    nodes.append(node)
