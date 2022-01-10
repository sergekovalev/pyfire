import sys

from dotenv import load_dotenv
import json
import lib.settings as settings
import os
import parser.morpheum.main as morpheum_parser
import parser.python.main as python_parser
import parser.morpheum.ast.main as morpheum_ast
import parser.python.ast.main as python_ast
import translator.c.main as c_translator
import translator.go.main as go_translator
from lib.helpers import import_module, log
from time import time

load_dotenv()


args = settings.init(root_dir=os.getcwd())

translator = {
    'from': {
        'morpheum': {
            'parser': morpheum_parser,
            'ast': morpheum_ast,
            'ext': 'mph'
        },
        'python': {
            'parser': python_parser,
            'ast': python_ast,
            'ext': 'py'
        }
    },
    'to': {
        'go': go_translator,
        'c': c_translator,
    }
}

print('@@@@', args)

if __name__ == '__main__':
    os.system('rm -rf __dist__ && mkdir __dist__')
    
    t = time()
    
    code = import_module(f'{settings.ROOT_DIR}/code.mph')
    
    parsed_code = translator['from'][settings.CONFIG['source_lang']].parser(code)
    log(path='parsed-code.json', content=json.dumps(parsed_code, indent=2))

    ast_code = translator['from'][settings.CONFIG['source_lang']]['ast'](parsed_code);
    log(path='parsed-code.json', content=json.dumps(ast_code, indent=2))

    output_code = translator['to'][settings.CONFIG['target_lang']](ast_code)
    log(path=f'main.{settings.CONFIG["target_lang"]}', folder='main', content=output_code)

    
    print(time() - t, 'ms')
