
index_dict = {
    'X': 0,
    'A': 0,
    'rock': 0,

    'Y': 1,
    'B': 1,
    'paper': 1,

    'Z': 2,
    'C': 2,
    'scissors': 2
}

translation_list = ['rock', 'paper', 'scissors']


def calc_score_for_own_move(your_move: str):
    if translation_list[index_dict[your_move]] == 'rock':
        return 1
    if translation_list[index_dict[your_move]] == 'paper':
        return 2
    if translation_list[index_dict[your_move]] == 'scissors':
        return 3


def calc_score_for_game(your_move: str, opponents_move: str):
    # draw
    if index_dict[your_move] == index_dict[opponents_move]:
        return 3
    # win
    elif index_dict[your_move] == (index_dict[opponents_move] + 1) % 3:
        return 6
    # loose
    else:
        return 0


if __name__ == '__main__':
    with open('strategy.txt') as f:
        total_score = 0
        for line in f.readlines():
            your_move = line[2]
            opponents_move = line[0]
            total_score += calc_score_for_own_move(your_move)
            total_score += calc_score_for_game(your_move=your_move, opponents_move=opponents_move)
        print(total_score)
