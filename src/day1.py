from utils import FileUtils
import itertools
import numpy as np

def get_multi(input, quantity):
    for item in itertools.combinations(input, quantity):
        if sum(item) == 2020:
            return np.prod(item)

def part_1():
    return get_multi(FileUtils.int_input(), 2)

def part_2():
    return get_multi(FileUtils.int_input(), 3)

if __name__ == "__main__":
    print( part_1() )
    print( part_2() )