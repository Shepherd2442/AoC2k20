from utils import FileUtils
import itertools

def get_first_invalid(numbers, preamble=25):
    for idx, number in enumerate(numbers[preamble:]):
        is_valid = [sum(num_pair) == number for num_pair in itertools.combinations(numbers[idx:preamble + idx], 2)]
        if sum(is_valid) == 0:
            return number

def get_encryption_weakness(numbers, invalid_num):
    sum_num, start_idx, last_idx = 0, -1, 0
    while sum_num != invalid_num:
        sum_num = 0
        start_idx += 1
        for idx, number in enumerate(numbers[start_idx:]):
            sum_num += number
            last_idx = start_idx + idx
            if sum_num >= invalid_num:
                break
    return sum([min(numbers[start_idx:last_idx]), max(numbers[start_idx:last_idx])])

if __name__ == "__main__":
    invalid_num =  get_first_invalid(FileUtils.int_input(), 25)
    print( invalid_num, get_encryption_weakness(FileUtils.int_input(), invalid_num) )