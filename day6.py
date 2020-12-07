from utils import FileUtils
from functools import reduce
from collections import Counter

def get_number_of_yes(groups, everyone=False):
    answers = ([reduce(lambda a1, a2: set(a1) & set(a2), group) for group in groups]) if everyone \
        else ([reduce(lambda a1, a2: a1 + a2, group) for group in groups])
    return [len(Counter(questions).keys()) for questions in answers]
    
def parse_answers(answers):
    groups, group = [], []
    for line in answers:
        if line == "":
            groups.append(group)
            group = []
            continue
        group.append(line)
    groups.append(group)
    return groups

def part_1(answer_groups):
    return sum( get_number_of_yes(answer_groups) )

def part_2(answer_groups):
    return sum( get_number_of_yes(answer_groups, everyone=True) )

if __name__ == "__main__":
    answer_groups = parse_answers(FileUtils.input())
    print( part_1(answer_groups) )
    print( part_2(answer_groups) )