import copy

def mini(doublelist):
    step = 1
    copydoublelist = copy.deepcopy(doublelist)
    minimal = copy.deepcopy(copydoublelist[0])
    while step < len(doublelist):
        compare = 2
        while compare <= len(copydoublelist):
            comp = copy.deepcopy(doublelist[compare - 1])
            counttens = 2
            while counttens <= len(minimal):
                if minimal[counttens - 1] > comp[counttens - 1]:
                    #print(minimal[counttens - 1])
                    #print(comp[counttens - 1])
                    minimal = copy.deepcopy(comp)
                    del copydoublelist[0]
                    break
                elif minimal[counttens - 1] < comp[counttens - 1]:
                    break
                else:
                    counttens += 1
            compare += 1
        step += 1
    return minimal

"""该叫sortdoublelist in a triplelist"""
def sortdoublelist(list1):
    list2 = []
    for tens in list1:
        changetens = []
        if  len(tens) > 1:
            tochangetens = copy.deepcopy(tens)
            countchange = 1
            while countchange <= len(tens):
                #print(tochangetens)
                minimal = mini(tochangetens)
                tochangetens.remove(minimal)
                changetens.append(minimal)
                countchange += 1
                #print(changetens)
        else:
            changetens = copy.deepcopy(tens)
        list2.append(changetens)
    return list2

#Mini = mini([[-1,1,3,2],[1,1,2,3],[2,3,4,5]])
Mini = mini([[-1, 1, 4], [-1, 2, 3]])
print(Mini)
minilist = sortdoublelist([[[-2, 2, 3], [-2, 1, 4]], [[-1, 1, 4], [-1, 2, 3]]])
print(minilist)