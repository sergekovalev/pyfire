import src.parser.morpheum.tokens as TOKENS


def create_node(nodes, code, index_from, index_to):
  # code.setLowerIndex(index_from)

  node = None

  if code[index_from] == TOKENS.VARIABLE_DECLARATION:
    if code.at(2) == TOKENS.EQ:
      node = {
        'type': TOKENS.VARIABLE_DECLARATION,
        'body': {
          'name': code.at(1),
        }
      }

      nodes.push(node)

      node = {
        'type': TOKENS.EXPRESSION,
      }

      nodes.push(node)

  # code.setLowerIndex(0)


def tree(code):
    nodes = []

    index_from = 0
    index_to = 0

    for i in range(code):
        token = code[i]

        if token == TOKENS.ENDL:
            index_to = i

            create_node(nodes, code, index_from, index_to)

            index_from = index_to

    return nodes


def ast(code):
    return {
        'type': 'module',
        'start': code.start,
        'end': code.end,
        'body': tree(code.tokens)
    }


def main(code):
    return ast(code)