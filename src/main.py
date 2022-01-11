import sys
import os

sys.path.insert(0, os.getcwd())

from dotenv import load_dotenv
from time import time
import json
from src.lib.settings import Settings
from lib.helpers import import_module, log
from parser.morpheum.main import main as morpheum_parser
from parser.python.main import main as python_parser
from parser.morpheum.ast.main import main as morpheum_ast
from parser.python.ast.main import main as python_ast
from translator.c.main import main as c_translator
from translator.go.main import main as go_translator


load_dotenv()

Settings().init(root_dir=os.getcwd())

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

if __name__ == '__main__':
    os.system('rm -rf __dist__ && mkdir __dist__')
    
    t = time()
    
    code = import_module(f'{Settings().ROOT_DIR}/samples/code.py')
    
    parsed_code = translator['from'][Settings().CONFIG['source_lang']]['parser'](code)
    log(path='parsed-code.json', content=json.dumps(parsed_code, indent=2))
    
    ast_code = translator['from'][Settings().CONFIG['source_lang']]['ast'](parsed_code)
    log(path='parsed-code.json', content=json.dumps(ast_code, indent=2))

    output_code = translator['to'][Settings().CONFIG['target_lang']](ast_code)
    log(path=f'main.{Settings().CONFIG["target_lang"]}', folder='main', content=output_code)

    print(round((time() - t)*1000), 'ms')
