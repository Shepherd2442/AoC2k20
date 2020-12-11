from utils import FileUtils

def parse_bag_rules(rules):
    bag_rules = {}
    for rule in rules:
        bag_name, contents = rule.split(" bags contain ")
        bag_rules[bag_name] = []
        if "no" in contents: continue
        inner_bags = contents.split(", ")
        for bag in inner_bags:
            num, attribute, color, *_ = bag.split(" ")
            bag_rules[bag_name] += (["%s %s" % (attribute, color)] * int(num))
    return bag_rules

def get_fittable_colors(bag_rules, my_bag="shiny gold"):
    color_list = set()
    for bag, contents in bag_rules.items():
        if my_bag in contents:
            color_list.add(bag)
            color_list.update(get_fittable_colors(bag_rules, my_bag=bag))
    return color_list

def get_bag_count_for(bag_rules, my_bag="shiny gold"):
    bag_count = 0
    for bag in bag_rules[my_bag]:
        bag_count += 1 + get_bag_count_for(bag_rules, bag)
    return bag_count

if __name__ == "__main__":
    bag_rules = parse_bag_rules(FileUtils.input())
    print( len(get_fittable_colors(bag_rules)) )
    print( get_bag_count_for(bag_rules) )