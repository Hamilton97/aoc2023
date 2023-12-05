import os
import re

from pathlib import Path


# these are the break conditions
m = {
    'red': 12,
    'green': 13,
    'blue': 14
}


def get_game_id(data: str) -> int:
    """ extracts game id from the string """
    pattern = r'\b(\d+)\b'
    match = re.search(pattern, data.split(":")[0])
    return int(match.group(1))


def get_game_data(data: str) -> list[tuple[str, int]]:
    pattern = r'(\d+)\s+(\w+)'
    # Find all matches in the input string
    matches = re.findall(pattern, data.split(":")[-1])
    # Extracted the results
    return [(match[1], int(match[0])) for match in matches]    


def main():
    with open(os.path.join(Path(__file__).parent, 'input.txt')) as f:
        data = [line.strip() for line in f.readlines()]
    
    sum = 0
    for line in data:
        game_id = get_game_id(line)
        game_data = get_game_data(line)

        if not any([gdat[1] > m.get(gdat[0]) for gdat in game_data]):
            print(f'Adding Game ID: {game_id}')
            sum += game_id
        else:
            print(f"Game {game_id} not valid")
    print(f'Total: {sum}')


if __name__ == '__main__':
    main()