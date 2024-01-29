import hy 
import sys
from icecream import ic
from pathlib import Path
import yaml
import os

state = {'key': []}
config_dict = {}

def FROM(path):
    print('FROM path:', path)
    apath = Path(path) 
    if apath.is_absolute() is False:
        apath = state['cwd'] / path 

    with open(apath) as f:
        stream = hy.read_many(f)
        for expr in stream:
            hy.eval(expr)        

def SET(key, val):
    if state['key'] == []:
        config_dict[key] = val 
    else:
        d = config_dict 
        for k in state['key']:
            if k in d:
                d = d[k]
            else:
                d[k] = {}
                d = d[k]
        d[key] = val

def GET(*args):
    vals = []
    for a in args:
        if isinstance(a, hy.models.Symbol):
            v = config_dict[str(a)]
        else:
            v = a 
        vals.append(v)
    return ''.join(vals)

def KEY(key):
    state['key'].append(key) 

def UNKEY():
    state['key'].pop(-1)

def ENV(var, default = None):
    return os.getenv(var, default)

def OPTSET(cond, key, val):
    if cond is True:
        SET(key, val) 

def IFSET(key):
    return key in config_dict
def main():
    target = Path(sys.argv[1])
    state['cwd'] = target.parent
    FROM(target.name)
    print(config_dict)
    print(yaml.dump(config_dict))

if __name__ == '__main__':
    main()
