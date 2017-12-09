#!/usr/bin/env python3


def get_largest_register_and_highest_value(instructions, registers):
    highest_value = 0
    for instruction in instructions:
        register_to_change = instruction[0]
        change = instruction[1]
        amount = int(instruction[2])
        condition = instruction[3].split()
        condition_register = instruction[4]
        condition[0] = "registers['" + condition_register + "']"
        condition = " ".join(condition)
        condition_amount = int(instruction[6])

        if eval(condition):
                change_register(change, registers, register_to_change, amount)

        value = registers[register_to_change]
        if value > highest_value:
            highest_value = value
    return max(registers.values()), highest_value


def change_register(change, registers, register_to_change, amount):
    if change == "inc":
        registers[register_to_change] += amount
    elif change == "dec":
        registers[register_to_change] -= amount


def process_file(input_file):
    instructions = []
    for line in input_file:
        line = line.replace("\n", "").split()
        instructions.append(line)
    registers = {}
    for instruction in instructions:
        registers[instruction[0]] = 0
        instruction[3] = " ".join(instruction[4:7])
    return instructions, registers


def main():
    with open('input_08.txt', 'r') as file:
        instructions, registers = process_file(file)
        largest_register, highest_value = get_largest_register_and_highest_value(instructions, registers)
        print("largest register: " + str(largest_register) + "\nhighest value: " + str(highest_value))

if __name__ == "__main__":
    main()
