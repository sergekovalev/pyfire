import tokens as TOKENS

pairs = {
    'number': [TOKENS.TYPE_DECLARATION, TOKENS.NUMBER],
    'string': [TOKENS.TYPE_DECLARATION, TOKENS.STRING],
    'var': [TOKENS.VARIABLE_DECLARATION],
    'import': [TOKENS.IMPORT],
    'function': [TOKENS.FUNCTION_DECLARATION],
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
    '(': [TOKENS.ARGS_LIST_START],
    ')': [TOKENS.ARGS_LIST_END]
}


def map_token(ch):
    token = pairs[ch]
    
    if token:
        if token.before or token.after:
            return token.before + ch + token.after
        
        return token
    
    return [ch]


def tokenize(code):
    tokens = []
    
    for token in code:
        tokens += map_token(token)
    
    return tokens



def main(code):
    try:
        return tokenize(code)
    except Exception:
        print(Exception)
        exit()
