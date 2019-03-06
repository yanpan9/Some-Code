def permutations(elements, num):
    if not isinstance(elements, list):
        elements=list(elements)
    length = len(elements)
    if not num:
        num = length
    for i in range(length):
        elem = elements[i:i+1]
        if num==1:
            yield elem
        else:
            rest = elements[:i]+elements[i+1:]
            for res in permutations(rest, num-1):
                yield elem+res

def combinations(elements, num):
    if not isinstance(elements, list):
        elements=list(elements)
    length = len(elements)
    if not num:
        num = length
    for i in range(length+1-num):
        elem = elements[i:i+1]
        if num==1:
            yield elem
        else:
            rest = elements[i+1:]
            for res in combinations(rest, num-1):
                yield elem+res
