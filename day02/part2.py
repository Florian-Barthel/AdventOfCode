from part1 import translation_list, index_dict, calc_score_for_own_move


def loose(opponents_move: str):
    your_move_index = (index_dict[opponents_move] - 1) % 3
    your_move = translation_list[your_move_index]
    score = calc_score_for_own_move(your_move)
    return score


def draw(opponents_move: str):
    your_move = opponents_move
    score = calc_score_for_own_move(your_move)
    return 3 + score


def win(opponents_move: str):
    your_move_index = (index_dict[opponents_move] + 1) % 3
    your_move = translation_list[your_move_index]
    score = calc_score_for_own_move(your_move)
    return score + 6


outcome_dict = {
    'X': loose,
    'Y': draw,
    'Z': win
}


if __name__ == '__main__':
    with open('strategy.txt') as f:
        total_score = 0
        for line in f.readlines():
            opponents_move = line[0]
            win_loose_draw = line[2]
            total_score += outcome_dict[win_loose_draw](opponents_move)
        print(total_score)
