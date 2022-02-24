import src.parser.tokens as TOKENS
from src.lib.extensions import List

from src.parser.ast.helpers.func_declaration import main as func_declaration_helper
from src.parser.ast.helpers.expr_declaration import main as expr_declaration_helper


def create_node(nodes, code, index_from, index_to):
    token = code[0]
    
    if token == TOKENS.FUNCTION_DECLARATION:
        func_declaration_helper(code, nodes, index_to)

    elif token == TOKENS.EQ:
        expr_declaration_helper(code, nodes, index_from, index_to)


def tree(tokens):
    nodes = []
    
    index_from = 0
    
    for i in range(len(tokens)):
        token = tokens[i]
        
        if token == TOKENS.ENDL:
            index_to = i

            tokens.set_index_from(index_from)
            create_node(nodes, tokens, index_from, index_to)
            tokens.set_index_from(0)
            
            index_from = index_to
    
    return nodes


def ast(code):
    return {
        'type': TOKENS.MODULE,
        'name': 'main',
        'start': code['start'],
        'end': code['end'],
        'body': tree(List(code['tokens']))
    }


def main(code):
    return ast(code)
