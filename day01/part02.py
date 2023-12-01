import os
import re
from pathlib import Path

char = str

# words that represent number now count
input_string = "two1nine"

MAPPING = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

PATTERN = r'zero|one|two|three|four|five|six|seven|eight|nine|0|1|2|3|4|5|6|7|8|9'

def main():
    
    # open the input file for reading
    with open(os.path.join(Path(__file__).parent, 'input.txt')) as f:
        streams = [line.strip() for line in f.readlines()]
    
    # we need to get the first int value form the stream
    values = []
    for stream in streams:
        # iterate over each value, find the int
        digits = re.findall(PATTERN, stream)
        # do some additional processing, converts the word to the number (str)
        for idx, val in enumerate(digits):
            if val.isalpha():
                digits[idx] = MAPPING.get(val)
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
