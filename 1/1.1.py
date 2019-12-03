print('Advent of Code, Day 1, Part 1')

with open('input.txt', 'r') as f:
    fuel = sum(map(lambda m: int(m) // 3 - 2, f.read().split('\n')[:-1]))

print(f'Fuel: {fuel}')