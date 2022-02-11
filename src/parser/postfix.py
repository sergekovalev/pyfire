import src.parser.tokens as TOKENS


def tokenize(tokens):
    for i in range(len(tokens)):
        if tokens[i] == TOKENS.EQ:
            tokens[i-1], tokens[i] = tokens[i], tokens[i-1]

    return tokens
