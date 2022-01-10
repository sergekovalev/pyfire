# from setuptools import setup, find_packages
#
# setup(name='pyfire', version='1.0', packages=find_packages())
import sys
import os
sys.path.insert(0, os.getcwd())
from dotenv import load_dotenv
import json
from time import time
import lib.settings as settings
from lib.helpers import import_module, log
from parser.morpheum.main import main as morpheum_parser
from parser.python.main import main as python_parser
import parser.morpheum.ast.main as morpheum_ast
import parser.python.ast.main as python_ast
import translator.c.main as c_translator
import translator.go.main as go_translator


load_dotenv()

settings.init(root_dir=os.getcwd())

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
    
    code = import_module(f'{settings.ROOT_DIR}/samples/code.py')
    
    parsed_code = translator['from'][settings.CONFIG['source_lang']]['parser'](code)
    log(path='parsed-code.json', content=json.dumps(parsed_code, indent=2))

    ast_code = translator['from'][settings.CONFIG['source_lang']]['ast'](parsed_code);
    log(path='parsed-code.json', content=json.dumps(ast_code, indent=2))

    output_code = translator['to'][settings.CONFIG['target_lang']](ast_code)
    log(path=f'main.{settings.CONFIG["target_lang"]}', folder='main', content=output_code)

    print(time() - t, 'ms')
