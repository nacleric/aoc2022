test_values = [
    "2-4,6-8",
    "2-3,4-5",
    "5-7,7-9",
    "2-8,3-7", # fully contains
    "6-6,4-6", # fully contains
    "2-6,4-8",
]

def parse_file():
    foo = []
    with open("../input/day4.txt") as file:
        for i in file.readlines():
            foo.append(i.strip())
    return foo


def part1(arr: list[str]):
    count = 0
    for i in arr:
        section_1, section_2 = i.split(",")
        s1_left, s1_right = section_1.split("-")
        s2_left, s2_right = section_2.split("-")

        # Forgot to convert this to integers WHY DOES IT STILL RUN
        if int(s1_left) <= int(s2_left) and int(s1_right) >= int(s2_right):
            count += 1
        elif int(s1_left) >= int(s2_left) and int(s1_right) <= int(s2_right):
            count += 1
    return count


def part2(arr: list[str]):
    count = 0
    for i in arr:
        section_1, section_2 = i.split(",")
        s1_left, s1_right = section_1.split("-")
        s2_left, s2_right = section_2.split("-")
        if int(s1_left) <= int(s2_right) and int(s1_right) >= int(s2_left):
            count += 1
    return count

if __name__ == "__main__":
    arr = parse_file()
    # print(part1(test_values))
    print(part1(arr))
    # print(part2(test_values))
    print(part2(arr))


