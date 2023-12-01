import os
from pathlib import Path

char = str

def main():
    
    # open the input file for reading
    with open(os.path.join(Path(__file__).parent, 'input.txt')) as f:
        streams = [line.strip() for line in f.readlines()]
    
    # we need to get the first int value form the stream
    values = []
    for stream in streams:
        # iterate over each value, find the int
        digits = []
        for char in stream:
            if char.isdigit():
                digits.append(char)
            else:
                continue
        
        # get the first and last from the list and concat
        # add a check if the len of digits from the stream is one duplicate it
        if len(digits) == 1: 
            val = int(f'{digits[0]}{digits[0]}')
        else:
            val = int(f'{digits[0]}{digits[-1]}')
        
        values.append(val)
        val = None
    
    print(f"Sum: {sum(values)}")

if __name__ == '__main__':
    main()