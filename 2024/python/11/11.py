MAX_LIM = 75
def apply_rules(item: int, the_map: dict, depth = 0) -> int:
    if depth == MAX_LIM:
        return 1
    
    rule = the_map.get((item,depth),None)
    if rule:
        return rule
    else:
        if item == 0:
            val = apply_rules(1,the_map,depth+1)
            the_map[(item,depth)] = val
            return val
        if len(str(item))%2 == 0:
            str_item = str(item)
            el1, el2 = int(str_item[:len(str_item)//2]), int(str_item[len(str_item)//2:])
            val = apply_rules(el1, the_map, depth+1) + apply_rules(el2,the_map, depth+1)
            the_map[(item,depth)] = val
            return val
        else:
            val = apply_rules(item*2024, the_map, depth+1)
            the_map[(item,depth)] = val
            return val

if __name__ == '__main__':
    with open("input.txt", "r") as f:
        exp = [int(i) for i in f.read().split(' ')]
    
    the_map = {}
    sum = 0
    for item in exp:
        sum += apply_rules(item,the_map,0)

    print(f"The sum is {sum}")