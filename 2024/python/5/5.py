## Reading the file into rules and updates

from os import name
from typing import List
from collections import Counter

input_file = 'test.txt'

rules = []
updates = []

reading_rules = True
with open(input_file,'r') as f:
    lines = [i.strip() for i in f.readlines()]
    for line in lines:

        if len(line) == 0:
            reading_rules = False
            continue
        if reading_rules:
            rules.append([int(i) for i in line.split('|')])
        else:
            updates.append([int(i) for i in line.split(',')])

# We loop on every update
# We check if every rule is ok
# If it is, we get the middle number


def part1():
    def check_update(update: list[int], rules: list[list[int]]):
        for rule in rules:
            if not check_rule(rule,update):
                return False
        return True

    def check_rule(rule: list[int],update: list[int]):

        first, second = rule[0], rule[1]

        # If first or second are not present, its ok
        if second not in update or first not in update:
            return True
        
        # If first is before second return true, else false
        if update.index(first) < update.index(second):
            return True
        else:
            return False

    def get_update_info(update: list[int], rules: list[list[int]]):
        if check_update(update, rules):
            return update[len(update)//2] #Every update it's an odd-numbered list apparently
        return 0

    sum = 0
    for update in updates:
        sum += get_update_info(update, rules)

    print(f"The sum is {sum}")



def part2():

    def rule_applies(rule: list[int], update: list[int]):
        first, second = rule[0], rule[1]

        # If first or second are not present, its ok
        if second not in update or first not in update:
            return False
        
        return True

    def check_update(update: list[int], rules: list[list[int]]):
        for rule in rules:
            if not check_rule(rule,update):
                return False
        return True 

    def check_rule(rule: list[int],update: list[int]):

        first, second = rule[0], rule[1]

        # If first or second are not present, its ok
        if second not in update or first not in update:
            return True
        
        # If first is before second return true, else false
        if update.index(first) < update.index(second):
            return True
        else:
            return False

    def order_update_and_get_info(update: list[int], rules: list[list[int]]):

        applied_rules = []
        for rule in rules:
            if rule_applies(rule,update):
                applied_rules.append(rule)

        ordered_update = order_update(applied_rules)
        return ordered_update[len(ordered_update)//2]

    def order_update(rules):
        
        rule_count = Counter()
        for rule in rules:
            first, second = rule[0], rule[1]

            # By updating of +1 for each time a number is second we get exactly its index in the update
            rule_count[first] += 0 
            rule_count[second] += 1

        return [i for i,c in rule_count.most_common()]

    # This is not efficient since we are going to check twice for every update but who cares
    def check_all_updates(updates: list[list[int]], rules):
        sum = 0
        for upd in updates:
            if not check_update(upd,rules):
                sum += order_update_and_get_info(upd,rules)

        print(f"the sum is {sum}")

    # Key assumption: every update only contains numbers that are ruled.
    # Thus each update is completely covered by a set of rules.

    # Algo
    # Check if the rule applies for a given update. If it does, store it.
    # Once you have all the rules, cycle through them.
    # If a number always appears at first in every rule, put it in first position.
    # If a number appears once as second, put it in second position
    # ...

    # input_file = 'test.txt'

    # rules = []
    # updates = []

    # reading_rules = True
    # with open(input_file,'r') as f:
    #     lines = [i.strip() for i in f.readlines()]
    #     for line in lines:

    #         if len(line) == 0:
    #             reading_rules = False
    #             continue
    #         if reading_rules:
    #             rules.append([int(i) for i in line.split('|')])
    #         else:
    #             updates.append([int(i) for i in line.split(',')])

    check_all_updates(updates,rules)

if __name__ == "__main__":
    part2() 