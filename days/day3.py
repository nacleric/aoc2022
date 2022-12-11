test_values = [
    "vJrwpWtwJgWrhcsFMMfFFhFp",
    "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
    "PmmdzqPrVvPwwTWBwg",
    "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
    "ttgJtRGJQctTZtZT",
    "CrZsJsPPZsGzwwsLwLmpwMDw",
]

import string

def parse_file():
    foo = []
    with open("../input/day3.txt") as file:
        for i in file.readlines():
            foo.append(i.strip())
    return foo

alphabet = list(string.ascii_lowercase) + list(string.ascii_uppercase)

def part1(rucksacks: list[str]):
    points = 0
    for rucksack in rucksacks:
        midpoint = int(len(rucksack)/2)
        rucksack_1 = rucksack[:midpoint]
        rucksack_2 = rucksack[midpoint:]
        similarity = list(set(rucksack_1).intersection(rucksack_2))[0] # Access single item list
        points += alphabet.index(similarity) + 1
    print(points)

def part2(rucksacks: list[str]):
    points = 0
    grouped_rucksacks = [rucksacks[i:i + 3] for i in range(0, len(rucksacks), 3)]
    for group in grouped_rucksacks:
        similarity = list(set(group[0]).intersection(group[1], group[2]))[0] # Access single item list
        points += alphabet.index(similarity) + 1
    print(points)


if __name__ == "__main__":
    # rucksacks = test_values
    rucksacks = parse_file()
    part1(rucksacks)
    part2(rucksacks)