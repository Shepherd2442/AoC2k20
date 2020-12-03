from utils import FileUtils
import numpy as np
marked_map = ""

def add_to_marked_map(row, index, tree):
    global marked_map
    s_list = list(row)
    s_list[index] = "X" if tree else "O"
    marked_map += ("".join(s_list)) + "\n"

def get_number_of_trees(toboggan_map, slope):
    h_index, trees = 0, 0
    for v_index, row in enumerate(toboggan_map):
        if v_index % slope['down'] != 0:
            continue
        if h_index >= len(row):
            h_index = h_index - len(row)
        if row[h_index] == "#":
            trees += 1
        add_to_marked_map(row, h_index, row[h_index] == "#")
        h_index += slope['right']
    return trees 

def part_1():
    return get_number_of_trees(FileUtils.input(), { "right": 3, "down": 1 }) 

def part_2():
    slopes = [
        { "right": 1, "down": 1 },
        { "right": 3, "down": 1 },
        { "right": 5, "down": 1 },
        { "right": 7, "down": 1 },
        { "right": 1, "down": 2 }
    ]
    return np.prod([get_number_of_trees(FileUtils.input(), slope) for slope in slopes])

if __name__ == "__main__":
    print(part_1())
    print(part_2())

    text_file = open("MarkedMap.txt", "w")
    text_file.write(marked_map)
    text_file.close()