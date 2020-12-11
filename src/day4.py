from utils import FileUtils
import re

ecl = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

def check_passport_fields(passport):
    global required_fields
    return False not in [(key in passport) for key in required_fields]

def check_passport_values(passport):
    if not check_passport_fields(passport):
        return False
    global ecl
    numerical_valid = (
        1920 <= int(passport['byr']) <= 2002 and len(passport['byr']) == 4 and
        2010 <= int(passport['iyr']) <= 2020 and len(passport['iyr']) == 4 and
        2020 <= int(passport['eyr']) <= 2030 and len(passport['eyr']) == 4 and
        len(passport['pid']) == 9 )
    unit = passport['hgt'][-2:]
    if (unit == 'cm' or unit == 'in'):
        height = int(passport['hgt'][:-2])
        height_valid = (150 <= height <= 193) if unit == 'cm' else (59 <= height <= 76)
    else:
        height_valid = False
    hair_color_valid = re.match("^#(?:[0-9a-f]{3}){1,2}$", passport['hcl']) is not None
    eye_color_valid = passport['ecl'] in ecl
    return numerical_valid and height_valid and hair_color_valid and eye_color_valid

def check_passport_validity(passport, check_values=False):
    if not check_values:
        return check_passport_fields(passport)
    return check_passport_values(passport)

def parse_passports(input):
    documents, document = [], {}
    for line in input:
        if line == "":
            documents.append(document)
            document = {}
            continue
        data_pairs = line.split(" ")
        for data_pair in data_pairs:
            field, value = data_pair.split(":")
            document[field] = value
    documents.append(document)
    return documents

def part_1(passports):
    return sum([check_passport_validity(passport) for passport in passports])

def part_2(passports):
    return sum([check_passport_validity(passport, True) for passport in passports])

if __name__ == "__main__":
    passports = parse_passports(FileUtils.input())
    print( part_1(passports) )
    print( part_2(passports) )