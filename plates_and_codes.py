from itertools import permutations

def list_to_int(lst):
    return int(''.join(lst))

def answer(l):
    l = sorted([str(el) for el in l], reverse=True)
    for r in range(len(l), 1, -1):
        for p in permutations(l, r + 1):
            if (list_to_int(p) % 3 == 0):
                return list_to_int(p)
    return 0
