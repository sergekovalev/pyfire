import src.parser.tokens as TOKENS

pairs = {
    'number': [TOKENS.TYPE_DECLARATION, TOKENS.NUMBER],
    'string': [TOKENS.TYPE_DECLARATION, TOKENS.STRING],
    'import': [TOKENS.IMPORT],
    'def': [TOKENS.FUNCTION_DECLARATION],
    '=': [TOKENS.EQ],
    '==': [TOKENS.IS_EQ],
    '>': [TOKENS.GT],
    '>=': [TOKENS.GTE],
    '<': [TOKENS.LT],
    '<=': [TOKENS.LTE],
    '+': [TOKENS.PLUS],
    '-': [TOKENS.MINUS],
    ';': [TOKENS.ENDL],
    'end': [TOKENS.END_OF_BLOCK],
    '{': [TOKENS.OPEN_CURLY_BRACKET],
    '}': [TOKENS.CLOSE_CURLY_BRACKET],
    '(': [TOKENS.OPEN_BRACKET],
    ')': [TOKENS.CLOSE_BRACKET],
    '\'': [TOKENS.SINGLE_QUOTE],
    '"': [TOKENS.DOUBLE_QUOTE],
    ':': [TOKENS.COLON],
    ',': [TOKENS.COMMA],
    '.': [TOKENS.DOT]
}


def map_token(ch):
    token = pairs[ch] if ch in pairs.keys() else None
    
    if token:
        if type(token) is dict and (token['before'] or token['after']):
            return token['before'] + ch + token['after']
        
        return token
    
    return [ch]


def tokenize(code):
    tokens = []
    
    for token in code:
        tokens += map_token(token)
    
    return tokens


def main(code):
    return tokenize(code)
