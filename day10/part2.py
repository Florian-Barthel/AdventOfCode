from part1 import CPU
from aoc_utils.parse import parse_multi_element


class Renderer:
    def __init__(self):
        self.pixel_pos_x = 0
        self.width = 40

    def draw_pixel(self, x_position):
        if self.pixel_pos_x >= self.width:
            self.pixel_pos_x -= self.width
            print()
        if x_position - 1 <= self.pixel_pos_x <= x_position + 1:
            print('█', end='')
        else:
            print(' ', end='')

        self.pixel_pos_x += 1


if __name__ == '__main__':
    cpu = CPU()
    renderer = Renderer()
    for instruction_line in parse_multi_element('instructions.txt'):
        cpu.process_instruction(instruction_line)
    for x in cpu.cycle_history:
        renderer.draw_pixel(x)
