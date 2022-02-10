import sys
import os

sys.path.insert(0, os.getcwd())

from dotenv import load_dotenv
from time import time
import json
from src.lib.settings import Settings
from lib.helpers import import_module, log, cp
from src.parser.main import main as parser
from src.parser.ast.main import main as ast
from translator.cpp.main import main as cpp_translator
from translator.c.main import main as c_translator
from translator.go.main import main as go_translator

load_dotenv()

Settings().init(root_dir=os.getcwd())
cfg = Settings().CONFIG

translator = {
    'from': {
        'parser': parser,
        'ast': ast,
    },
    'to': {
        'go': go_translator,
        'c': c_translator,
        'cpp': cpp_translator,
    }
}


def create_dist_folder():
    os.system('rm -rf __dist__ && mkdir __dist__')


def get_source_code():
    path = f'{Settings().ROOT_DIR}/samples/code.py'
    
    return import_module(path)


def get_parsed_code(code):
    outcode = translator['from']['parser'](code)
    log(path='parsed-code.json', content=json.dumps(outcode, indent=2))
    
    return outcode


def get_ast_code(code):
    outcode = translator['from']['ast'](code)
    log(path='ast-code.json', content=json.dumps(outcode, indent=2))
    
    return outcode


def get_out_code(code):
    outcode = translator['to'][cfg['target']['lang']](code)
    log(path=f'main.{cfg["target"]["lang"]}', folder=cfg['target']['folder'], content=outcode)
    
    return outcode


def copy_scripts():
    if cfg["target"]["lang"] not in ['c', 'cpp']:
        return
        
    cp_path_from = f'{Settings().ROOT_DIR}/src/translator/{cfg["target"]["lang"]}/scripts'
    cp_path_to = f'{Settings().ROOT_DIR}/__dist__'
    
    cp(f'{cp_path_from}/CMakeLists.txt', f'{cp_path_to}/CMakeLists.txt')
    cp(f'{cp_path_from}/run.sh', f'{cp_path_to}/run.sh')


if __name__ == '__main__':
    t = time()

    create_dist_folder()
    
    source_code = get_source_code()
    parsed_code = get_parsed_code(source_code)
    ast_code = get_ast_code(parsed_code)
    out_code = get_out_code(ast_code)
    
    copy_scripts()

    print(round((time() - t) * 1000), 'ms')
