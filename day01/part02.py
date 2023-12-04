import os
import re
from pathlib import Path


char = str

m = {
    'one':    1,
    'two':    2,
    'three':  3,
    'four':   4,
    'five':   5,
    'six':    6,
    'seven':  7,
    'eight':  8,
    'nine':   9,
}


def main():
    
    # open the input file for reading
    with open(os.path.join(Path(__file__).parent, 'input.txt')) as f:
        data = [line.strip() for line in f.readlines()]
    
    sum = 0
    for line in data:
        fst, lst, s = None, None, ""
        for c in line:
            dig = None
            if c.isdigit():
                dig = c
            else:
                s += c
                for k,v in m.items():
                    if s.endswith(k):
                        dig = str(v)

            if dig is not None:
                lst = dig
                if fst is None:
                    fst = dig
        sum += int(fst + lst)

    print(sum)
        
    # we need to get the first int value form the stream
if __name__ == '__main__':
    main()
