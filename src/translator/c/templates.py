from src.lib.helpers import tokenize

MAIN_FUNC = '''
int main(int argc, char ** argv) {
  {{content}}
}
'''

FUNC = '''
{{type}} {{name}}({{args}}) {
    {{content}}
}
'''


def main_func(tokens):
    return tokenize(MAIN_FUNC, tokens)


def func(tokens):
    return tokenize(FUNC, tokens)
