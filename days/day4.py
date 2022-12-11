test_values = [
    "2-4,6-8",
    "2-3,4-5",
    "5-7,7-9",
    "2-8,3-7", # fully contains
    "6-6,4-6", # fully contains
    "2-6,4-8",
]

def part1(arr: list[str]):
    count = 0
    for i in arr:
        section_1, section_2 = i.split(",")
        s1_left, s1_right = section_1.split("-")
        s2_left, s2_right = section_2.split("-")
        if s1_left <= s2_left and s1_right >= s2_right:
            count += 1
        if s1_left >= s2_left and s1_right <= s2_right:
            count += 1
    return count


if __name__ == "__main__":
    print(part1(test_values))