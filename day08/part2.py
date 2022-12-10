import numpy as np


def max_scenic_score(tree_array: np.ndarray) -> int:
    max_score = 0
    for i in range(1, tree_array.shape[0] - 1):
        for j in range(1, tree_array.shape[1] - 1):
            tree_house_height = tree_array[i, j]
            left = np.flip(tree_array[i, :j])
            right = tree_array[i, j + 1:]
            up = np.flip(tree_array.T[j, :i])
            down = tree_array.T[j, i + 1:]
            score = np.prod([num_trees(direction, tree_house_height) for direction in [left, right, up, down]])
            if score > max_score:
                max_score = score
    return max_score


def num_trees(row_of_trees: np.ndarray, current_house_height: int) -> int:
    indices = np.array(np.where(row_of_trees >= current_house_height))[0]
    if indices.shape[0] > 0:
        return np.min(indices) + 1
    else:
        return row_of_trees.shape[0]


if __name__ == '__main__':
    with open('tree_map.txt') as f:
        shell_output_lines = f.read().splitlines()
        tree_array = np.array(list(map(list, shell_output_lines))).astype(int)
        scenic_score = max_scenic_score(tree_array)
        print(scenic_score)
