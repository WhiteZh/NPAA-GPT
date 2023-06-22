from npaa.repl import repl
from os import environ

openai_api_key = None

try:
    openai_api_key = environ['OPENAI_API_KEY']
except KeyError as e:
    if e.args[0] == 'OPENAI_API_KEY' and len(e.args) == 1:
        raise RuntimeError('OPENAI_API_KEY not found!')
    else:
        raise e

if openai_api_key:
    repl(key=openai_api_key, role='tester')
