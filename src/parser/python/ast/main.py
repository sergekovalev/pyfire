import src.parser.python.tokens as TOKENS
from src.lib.extensions import List

from src.parser.python.ast.helpers.func_declaration import main as func_declaration_helper
from src.parser.python.ast.helpers.var_declaration import main as var_declaration_helper


def create_node(nodes, code, index_to):
    token = code[0]
    
    if token == TOKENS.VARIABLE_DECLARATION:
        if code[2] == TOKENS.EQ:
            var_declaration_helper(code, nodes, index_to)

    elif token == TOKENS.FUNCTION_DECLARATION:
        func_declaration_helper(code, nodes, index_to)


def tree(code):
    nodes = []
    
    index_from = 0
    
    for i in range(len(code)):
        token = code[i]
        
        if token == TOKENS.ENDL:
            index_to = i

            code.set_index_from(index_from)
            create_node(nodes, code, index_to)
            code.set_index_from(0)
            
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
