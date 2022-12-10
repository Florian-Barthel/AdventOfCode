import numpy as np


def get_visible_trees_left(tree_array: np.ndarray, seen_trees: np.ndarray):
    num_trees = 0
    for i in range(tree_array.shape[0]):
        current_tree_height = -1
        for j in range(tree_array.shape[1]):
            if tree_array[i, j] > current_tree_height:
                if seen_trees[i, j] == 0:
                    num_trees += 1
                current_tree_height = tree_array[i, j]
                seen_trees[i, j] = 1
    return num_trees, seen_trees


if __name__ == '__main__':
    with open('tree_map.txt') as f:
        shell_output_lines = f.read().splitlines()
        tree_array = np.array(list(map(list, shell_output_lines))).astype(int)
        seen_trees = np.zeros(tree_array.shape)
        num_trees = 0
        for i in range(4):
            tree_array = np.rot90(tree_array)
            seen_trees = np.rot90(seen_trees)
            num_trees_current_side, seen_trees = get_visible_trees_left(tree_array, seen_trees)
            num_trees += num_trees_current_side
        print(num_trees)
