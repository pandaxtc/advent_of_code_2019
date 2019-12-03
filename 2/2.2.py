print('Advent of Code, Day 1, Part 2')

with open('input.txt', 'r') as f:
    og_data = list(map(int, f.read().split(',')))

    for i in range(100):
        for j in range(100):
            data = og_data.copy()
            data[1] = i # fixer upper
            data[2] = j

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

            if data[0] == 19690720: # provided
                print(100 * i + j)
                exit(0)
