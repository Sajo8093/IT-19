from random import randint
open   = 0
closed = 1


def splash():
    print()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("           Biathlon")
    print()
    print("       a hit or miss game")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print()
    
def is_open(value):
    if value == open:
        return True
    elif value == closed:
        return False
    
def is_closed(value):
    if value == open:
        return False
    elif value == closed:
        return True
    
def new_targets():
    xs = []
    for x in range(5):
        xs.append(open)
    return xs

target = new_targets()

def close_target(target, position):
    target[position] = closed
    return target

    
def points(target):
    n = 0
    for x in target:
        if is_closed(x) == True:
            n = n + 1
    return n
    
def target_to_string(target):
    s = ""
    for x in target:
        if is_closed(x) == True:
            s = s + " * "
        elif is_open(x) == True:
            s = s + " O "
    return s
    
def view_targets(target):
    print()
    print(" 1  2  3  4  5")
    print()
    print(target_to_string(target))
    print()
    
def random_hit():
    randint(0,1)
    if randint(0,1) == 0:
        return False
    else:
        return True
    
def shoot(target, position):
    if random_hit() == True:
        if is_open(target [position]) == True:
            close_target(target, position)
            return "Hit on open target"
        elif is_closed(target [position]) == True:
            return "Hit on closed target"
    else:
        return "Miss"
    
def parse_target(string):
    
    