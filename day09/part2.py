from part1 import Rope as RopeSegment
from part1 import VisitedLocationCounter


if __name__ == '__main__':
    num_segments = 9
    rope = [RopeSegment() for _ in range(num_segments)]
    location_counter = VisitedLocationCounter()
    location_counter.visit_location(rope[-1].get_tail_pos())
    with open('rope_movement.txt') as f:
        for line in f.read().splitlines():
            direction, amount = line.split()
            amount = int(amount)
            for _ in range(amount):
                rope[0].move_head(direction)
                rope[0].tail_follow()
                for i in range(1, num_segments):
                    rope[i].set_head_pos(*rope[i - 1].get_tail_pos())
                    rope[i].tail_follow()
                location_counter.visit_location(rope[-1].get_tail_pos())
    print(location_counter.count_visited_locations())
