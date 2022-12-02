#!/usr/bin/env python3

def print_elf_data(elf_number, total_calories):
    print(f"Elf {elf_number} has {total_calories} total calories.")


def update_maxes(elf_counter, calories, max_elves, max_calories):
    if calories > max_calories[0]:
        max_calories[2] = max_calories[1]
        max_calories[1] = max_calories[0]
        max_calories[0] = calories
        max_elves[2] = max_elves[1]
        max_elves[1] = max_elves[0]
        max_elves[0] = elf_counter
    elif calories > max_calories[1]:
        max_calories[2] = max_calories[1]
        max_calories[1] = calories
        max_elves[2] = max_elves[1]
        max_elves[1] = elf_counter
    elif calories > max_calories[2]:
        max_calories[2] = calories
        max_elves[2] = elf_counter
    return max_elves, max_calories


def print_maxes(max_elves, max_calories):
    print(f"Elf {max_elves[0]} has {max_calories[0]} calories (the most).")
    print(f"Elf {max_elves[1]} has {max_calories[1]} calories (the second most).")
    print(f"Elf {max_elves[2]} has {max_calories[2]} calories (the third most).")


def main():
    elf_counter = 1
    calories = 0
    max_calories = [0, 0, 0]
    max_elves = [0, 0, 0]

    for line in open('input','r'):
        #print(f"new iteration.  line = '{line}'")
        if line.strip() == "":
            #print(f"calories = {calories}")
            max_elves, max_calories = update_maxes(elf_counter, \
                    calories, max_elves, max_calories)
            print_elf_data(elf_counter, calories)
            elf_counter += 1
            calories = 0
        else:
            calories += int(line)
            #print(calories)
    max_elves, max_calories = update_maxes(elf_counter, \
                    calories, max_elves, max_calories)
    print_elf_data(elf_counter, calories)
    print_maxes(max_elves, max_calories)
    print(f"The top three elves are carrying {sum(max_calories)} total calories")


if __name__ == '__main__':
    main()
