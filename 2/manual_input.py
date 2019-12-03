print('Advent of Code, Day 2, Opcode Interpreter')

with open('input.txt', 'r') as f:
    data = list(map(int, f.read().split(',')))
    data[1] = int(input('A? '))
    data[2] = int(input('B? '))

    op_index = 0
    while (len(data) - 4 * op_index >= 4):
        opcode, a0, a1, store = data[4 * op_index: 4 * op_index + 4]
        if opcode == 1:
            data[store] = data[a0] + data[a1]
        elif opcode == 2:
            data[store] = data[a0] * data[a1]
        elif opcode == 99:
            break
        else:
            raise RuntimeError('uh oh stinky')

        op_index += 1

print(data[0])
