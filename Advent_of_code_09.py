#!/usr/bin/env python3

import fileinput


def count_points(chars_list):
    point_of_group = 0
    sum = 0
    in_garbage = False
    in_group = False
    negated = False
    for index, char in enumerate(chars_list):
        if char == "!":
            negated = not negated
        elif char == "{" and not in_garbage and not negated:
            in_group = True
            point_of_group += 1
        elif char == "}" and not in_garbage and in_group and not negated:
            sum += point_of_group
            if point_of_group > 0:
                point_of_group -= 1
            if point_of_group == 0:
                in_group = False
        elif char == "<" and not negated:
            in_garbage = True
        elif char == ">" and in_garbage and not negated:
            in_garbage = False
        if char != "!" and negated:
            negated = not negated
    return sum


def count_garbage(chars_list):
    sum = 0
    in_garbage = False
    negated = False
    for index, char in enumerate(chars_list):
        if char == "!":
            negated = not negated
        elif char == "<" and not in_garbage and not negated:
            in_garbage = True
        elif char == ">" and in_garbage and not negated:
            in_garbage = False
        elif char != "!" and in_garbage and not negated:
            sum += 1
        if char != "!" and negated:
            negated = not negated
    return sum


def process_file(input_file):
    chars = []
    while True:
        char = input_file.read(1)
        if char == "\n":
            break
        else:
            chars.append(char)
    return chars


def main():
    with open('input_09.txt', 'r') as file:
        chars_list = process_file(file)
        print(count_points(chars_list))
        print(count_garbage(chars_list))


if __name__ == "__main__":
    main()
