# A = Rock    = X = 1
# B = Paper   = Y = 2
# C = Scissor = Z = 3
# Winning = 6 points
# Losing  = 0 points
# Tie     = 3 points

def parse_file():
    foo = []
    with open("../input/day2.txt") as file:
        count = 0
        for i in file.readlines():
            count += 1
            line = i.strip()
            foo.append((line[0], line[2]))
        return foo


test_values = [("A", "Y"), ("B", "X"), ("C", "Z")]

point_mapper = {
    "A": 1,
    "B": 2,
    "C": 3,
    "X": 1,
    "Y": 2,
    "Z": 3,
}

win_mapper = {
    "A": "Y",
    "B": "Z",
    "C": "X",
}
draw_mapper = {
    "A": "X",
    "B": "Y",
    "C": "Z",
}
lose_mapper = {
    "A": "Z",
    "B": "X",
    "C": "Y",
}

# I should have just mapped wins not calculate who wins using points
def round_score(choice: tuple[str, str], opponent_score, player_score: int) -> tuple[int, int]:
    opponent_score = 0
    player_score = 0
    opponent_move = point_mapper[choice[0]] #("A", "X")
    player_move = point_mapper[choice[1]]

    opponent_score += opponent_move
    player_score += player_move
    if opponent_move == player_move:
        opponent_score += 3
        player_score += 3
    elif opponent_move != player_move:
        result = player_move - opponent_move
        if result == 1 or result == -2:
            player_score += 6
            opponent_score += 0
        else:
            player_score += 0
            opponent_score += 6

    return (opponent_score, player_score)


def part1(rounds: list[tuple[str, str]]):
    total_opponent_score = 0
    total_player_score = 0
    for choice in rounds:
        round_result = round_score(choice, total_opponent_score, total_player_score)
        total_opponent_score += round_result[0]
        total_player_score += round_result[1]
    return (total_opponent_score, total_player_score)


def player_move_calc(opponent_move: str, result: str) -> int:
    player_score = 0
    if result == "Z": # win
        player_score += point_mapper[win_mapper[opponent_move]] + 6
    elif result == "Y": # Draw
        player_score += point_mapper[draw_mapper[opponent_move]] + 3
    else: # Lose
        player_score += point_mapper[lose_mapper[opponent_move]]
    return player_score


def part2(rounds: list[tuple[str, str]]):
    total_player_score = 0
    for choice in rounds:
        opponent_move = choice[0]
        result = choice[1]
        total_player_score += player_move_calc(opponent_move, result)
    return total_player_score


if __name__ == "__main__":
    rounds = parse_file()
    print(part1(rounds))
    print(part2(rounds))