import numpy as np


class VisitedLocationCounter:
    def __init__(self):
        self.visited_locations = {}

    def visit_location(self, location: any):
        self.visited_locations[location] = 0

    def count_visited_locations(self) -> int:
        return len(self.visited_locations.keys())


class Rope:
    def __init__(self):
        self.head_pos_x = 0
        self.head_pos_y = 0
        self.tail_pos_x = 0
        self.tail_pos_y = 0

    def move_head(self, direction: str):
        if direction == 'R':
            self.head_pos_x += 1
        elif direction == 'L':
            self.head_pos_x -= 1
        elif direction == 'U':
            self.head_pos_y -= 1
        elif direction == 'D':
            self.head_pos_y += 1

    def tail_follow(self):
        diff_x = self.head_pos_x - self.tail_pos_x
        diff_y = self.head_pos_y - self.tail_pos_y

        # still close enough
        if abs(diff_x) <= 1 and abs(diff_y) <= 1:
            return

        # moving diagonally
        if diff_x != 0 and diff_y != 0:
            self.tail_pos_x += np.clip(diff_x, -1, 1)
            self.tail_pos_y += np.clip(diff_y, -1, 1)
            return

        # moving straight
        self.tail_pos_x += diff_x // 2
        self.tail_pos_y += diff_y // 2

    def get_tail_pos(self):
        return self.tail_pos_x, self.tail_pos_y

    def set_head_pos(self, tail_pos_x, tail_pos_y):
        self.head_pos_x = tail_pos_x
        self.head_pos_y = tail_pos_y


if __name__ == '__main__':
    rope = Rope()
    location_counter = VisitedLocationCounter()
    location_counter.visit_location(rope.get_tail_pos())
    with open('rope_movement.txt') as f:
        for line in f.read().splitlines():
            direction, amount = line.split()
            amount = int(amount)
            for i in range(amount):
                rope.move_head(direction)
                rope.tail_follow()
                location_counter.visit_location(rope.get_tail_pos())
    print(location_counter.count_visited_locations())




