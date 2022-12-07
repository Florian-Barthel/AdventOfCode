import re


class FileSystem:
    def __init__(self, total_space):
        self.files = {'~': {'size': 0}}
        self.current_dir = ['~']
        self.total_size_small_dirs = 0
        self.total_sizes = []
        self.total_space = total_space
        self.used_space = 0

    def execute_command(self, command: str):
        change_home = re.search(r'\$ cd /', command)
        change_dir = re.search(r'\$ cd \w+', command)
        change_up = re.search(r'\$ cd \.\.', command)

        if change_home is not None:
            self.current_dir = ['~']
            return

        if change_dir is not None:
            self.current_dir.append(change_dir.group(0).split()[-1])
            return

        if change_up is not None:
            self.current_dir.pop()
            return

    def add_files_and_dirs(self, console_output: str):
        directory = re.search(r'dir \w+', console_output)
        file = re.search(r'\d+ \w+', console_output)

        if directory is not None:
            directory_name = directory.group(0).split()[-1]
            current_directory_dict = self.get_current_dir()
            if directory_name not in current_directory_dict.keys():
                current_directory_dict[directory_name] = {'size': 0}
            return

        if file is not None:
            file_size = int(file.group(0).split()[0])
            current_directory_dict = self.get_current_dir()
            current_directory_dict['size'] += file_size
            return

    def get_current_dir(self):
        current_directory_dict = self.files
        for key in self.current_dir:
            current_directory_dict = current_directory_dict[key]
        return current_directory_dict

    def get_sum_small_dir(self, max_size: int) -> int:
        self.total_size_small_dirs = 0
        self._rec_get_sum_small_dir(self.files['~'], max_size)
        return self.total_size_small_dirs

    def _rec_get_sum_small_dir(self, directory: dict, max_size: int):
        if len(directory.keys()) == 1:
            self.total_sizes.append(directory['size'])
            self.used_space += directory['size']

            if directory['size'] <= max_size:
                self.total_size_small_dirs += directory['size']
            return directory['size']
        else:
            total_size = directory['size']
            self.used_space += total_size

            for key in directory.keys():
                if key != 'size':
                    total_size += self._rec_get_sum_small_dir(directory[key], max_size)
            if total_size <= max_size:
                self.total_size_small_dirs += total_size
            self.total_sizes.append(total_size)
            return total_size

    def get_unused_space(self):
        return self.total_space - self.used_space

    def free_space_size(self, max_size: int) -> int:
        size_to_free = max_size - self.get_unused_space()
        self.total_sizes.sort()
        for i, current_size in enumerate(self.total_sizes):
            if current_size > size_to_free:
                return current_size
        return self.total_sizes[-1]


if __name__ == '__main__':
    file_system = FileSystem(total_space=70000000)
    with open('shell_output.txt') as f:
        shell_output_lines = f.read().splitlines()
        for line in shell_output_lines:
            if line.startswith('$'):
                file_system.execute_command(line)
            else:
                file_system.add_files_and_dirs(line)

    print('Part 1')
    print(file_system.get_sum_small_dir(100000))

    print('Part 2')
    print(file_system.free_space_size(30000000))
