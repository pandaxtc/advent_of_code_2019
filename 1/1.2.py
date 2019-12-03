print('Advent of Code, Day 1, Part 2')

mass2fuel = lambda mass: mass // 3 - 2

with open('input.txt', 'r') as f:
    masses = map(int, f.read().split('\n')[:-1])
    calc_fuel = lambda mass: 0 if mass2fuel(mass) <= 0 else mass2fuel(mass) + calc_fuel(mass2fuel(mass))
    fuel = sum(map(calc_fuel, masses))

print(f'Fuel: {fuel}')