

with open('calories.txt') as f:
    elf_list = ''.join(f.readlines()).split('\n\n')
    calorie_list = [elf.split('\n') for elf in elf_list]
    calorie_sum_list = [sum(list(map(int, calories))) for calories in calorie_list]
    calorie_sum_list.sort()
    print(sum(calorie_sum_list[-3:]))