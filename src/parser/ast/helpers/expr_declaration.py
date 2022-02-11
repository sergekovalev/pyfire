import re
import src.parser.tokens as TOKENS


def define_type(expr):
    res = {'type': None, 'value': expr}

    if expr in [TOKENS.PLUS, TOKENS.MINUS, TOKENS.MULTIPLY, TOKENS.DIVISION, TOKENS.POWER]:
        res = {'type': TOKENS.OPERATION, 'value': expr}
    elif expr == 'None':
        res['type'] = TOKENS.NULL
    elif re.match(r'\d+', expr):
        res['type'] = TOKENS.INTEGER
    elif re.match(r'\d+\.\d+', expr):
        res['type'] = TOKENS.FLOAT
    elif re.match(r'".*"', expr) or re.match(r'\'.*\'', expr):
        res['type'] = TOKENS.STRING
    else:
        res['type'] = TOKENS.UNDEFINED
        
    return res


def build_expr(tokens, index_from, index_to):
    expr = []
    
    i = index_from + 2
    length = index_to
    
    while i < length:
        token = tokens[i]
        
        expr.append(define_type(token))
        
        i += 1
    
    return expr


def main(tokens, nodes, index_from, index_to):
    node = {
        'type': TOKENS.EXPRESSION,
        'var_name': tokens[1],
        'is_const': tokens[1] == tokens[1].upper(),
        'body': build_expr(tokens, index_from, index_to)
    }
    
    nodes.append(node)
