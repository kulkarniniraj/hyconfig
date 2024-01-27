import hy 
import sys
from icecream import ic
from pathlib import Path
import yaml

state = {}
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
    config_dict[key] = val 

def GET(*args):
    vals = []
    for a in args:
        if isinstance(a, hy.models.Symbol):
            v = config_dict[str(a)]
        else:
            v = a 
        vals.append(v)
    return ''.join(vals)

def main():
    target = Path(sys.argv[1])
    state['cwd'] = target.parent
    FROM(target.name)
    print(config_dict)
    print(yaml.dump(config_dict))

if __name__ == '__main__':
    main()
