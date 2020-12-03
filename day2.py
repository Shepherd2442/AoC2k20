from utils import FileUtils

def is_valid(policy, password):
    character_count = password.count(policy['character'])
    return character_count <= policy['u_bound'] and character_count >= policy['l_bound']

def is_valid_index(policy, password):
    return (password[policy['l_bound'] - 1] == policy['character']) != (password[policy['u_bound'] - 1] == policy['character'])

def parse_policy(policy):
    bounds, character = policy.split(" ")
    l_bound, u_bound = bounds.split("-")
    return dict(character = character, l_bound = int(l_bound), u_bound = int(u_bound))

def get_number_of_valid(input, validity_function):
    valid = 0
    for line in input:
        policy, password = line.split(": ")
        if ( validity_function( parse_policy( policy ), password)):
            valid += 1
    return valid

def part_1():
    return get_number_of_valid(FileUtils.input(), is_valid)

def part_2():
    return get_number_of_valid(FileUtils.input(), is_valid_index)

if __name__ == "__main__":
    print(part_1())
    print(part_2())