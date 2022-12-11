# I hate parsing
def parse_file() -> list:
    values = []
    elf = []
    with open("../input/day1.txt","r") as file:
        line_count = 0
        for (i, line) in enumerate(file.readlines()):
            line_count += 1
            if line.strip() != "":
                elf.append(int(line.strip()))
            else:
                values.append(elf)
                elf = []
            if i == line_count - 1:
                values.append(elf)
    return values


def part1(calories: list):
    most_calories = 0
    for i in calories:
        if most_calories < sum(i):
            most_calories = sum(i)
    print(most_calories)


def part2(calories: list):
    new_calories = []
    for i in calories:
        new_calories.append(sum(i))
    scuffed = sorted(set(new_calories), reverse=True)
    return (scuffed[0], scuffed[1], scuffed[2])


if __name__ == "__main__":
    calories = parse_file()
    part1(calories)
    print(part2(calories))