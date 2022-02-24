import src.parser.tokens as TOKENS
import src.lib.helpers

operations = []
postfix_tokens = []
stack = []


def tokenize(tokens):
    for token in tokens:
        postfix_tokens.append(token)

    return postfix_tokens
