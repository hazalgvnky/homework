def flatten(tree, res = []):
    for i in tree:
        if type(i) == list :
            res += flatten(i, [])
        else:
            res += [i]
    return res

def maxi(lis, maximus = 0):
    liste = flatten(lis)
    for i in liste:
        if type(i) == int:
            if i > maximus:
                maximus = i
    return maximus

def all_trees(tree, all = []):
    all.append(tree)
    for i in tree:
        if type(i) == list:
            all_trees(i)
    return all

def flatten_all(tree):
    all1 = all_trees(tree)
    res2 = []
    for i in all1:
        a = flatten(i, res= [])
        if not a in res2:
            res2 += [a]
    return res2

def path(tree, final=[]):
    flatrees = flatten_all(tree)
    for i in range(1, maxi(flatrees)+1):
        res3 = []
        for elem in flatrees:
            if elem.count(i) >= 1:
                res3 += [elem[0]]
        final += [res3]
    return final

def chalchiuhtlicue(tree, n = 0):
    path1 = path(tree)
    maxim = maxi(tree)
    result = []
    while n < maxim:
        result_helper = []
        if len(path1) == 1:
            result += [[tree[0]]]
        elif path1[0] == []:
            result += [[]]
            path1 = path1[1:]
        else:
            for i in path1[0]:
                flat3 = flatten(path1, res=[])
                if flat3.count(i) == 1:
                    result_helper += i
            if len(result_helper) > 1:
                for num in range(len(result_helper)-1):
                    first = result_helper[num]
                    second = result_helper[num+1]
                    if first in path1[0] and second in path1[0]:
                        p1 = flatten(tree).index(first)
                        p2 = flatten(tree).index(second)
                        if not flatten(tree)[p1+1] == n+1 and flatten(tree)[p2+1] == n+1:
                            result_helper.remove(second)
            path1 = path1[1:]
            result.append(result_helper)
        n += 1
    return result



