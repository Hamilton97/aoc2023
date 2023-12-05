import os
import re

from pathlib import Path


def get_game_data(data: str) -> list[tuple[str, int]]:
    pattern = r'(\d+)\s+(\w+)'
    # Find all matches in the input string
    matches = re.findall(pattern, data.split(":")[-1])
    # Extracted the results
    return [(match[1], int(match[0])) for match in matches]    


def compute_cube_power(data: list[tuple[int, str]]) -> int:
    """finds the max cube value for a game by color for a single game"""
    power = 1
    for color in ['red', 'green', 'blue']:
        vals = []
        for dat in data:
            x, y = dat
            if x == color:
                vals.append(y)
        power *= max(vals)
            
    return power
        

def main():
    with open(os.path.join(Path(__file__).parent, 'input.txt')) as f:
        data = [line.strip() for line in f.readlines()]
    
    sum = 0
    for index, line in enumerate(data, start=1):
        game_data = get_game_data(line)
        power_value = compute_cube_power(game_data)
        print(f"Game {index} Power Value: {power_value}")
        sum += power_value
    print(f"Sum of the power sets: {sum}")


if __name__ == '__main__':
    main()