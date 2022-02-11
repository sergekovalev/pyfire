import src.parser.tokens as TOKENS


def main(code, nodes, index_to):
    node = {
        'type': TOKENS.VARIABLE_DECLARATION,
        'body': {
            'name': code[1],
        }
    }
    
    nodes.append(node)

