import hy 
import sys

config_dict = {}

def FROM(path):
    stream = hy.read_many(path)
    for expr in stream:
        hy.eval(expr)        

def SET(key, val):
    config_dict[key] = val 

def main():
    FROM(sys.argv[1])
    print(config_dict)

if __name__ == '__main__':
    main()
