import copy

def mainmiusind(mainlist,indexlist):
    goallist = []
    for tens in mainlist:
        if len(tens) == 1:
            comp = copy.deepcopy(tens[0])
            del comp[0]
            add = True
            for ind in indexlist:
                if comp == ind:
                    add = False
                    break
            if add:
                goallist.append(tens)
        else:
            goallist.append(tens)
    return goallist

"""mainlist为三重序列，而输出为一个二重序列"""
def indminusmain(mainlist,indexlist):
    goallist = []
    for ind in indexlist:
        add = True
        for tens in mainlist:
            if len(tens) == 1:
                comp = copy.deepcopy(tens[0])
                del comp[0]
                if ind == comp:
                    add = False
                    break
        if add:
            goallist.append(ind)
    return goallist

"""输入为两个二重序列，输出为一个二重序列"""
def indandmain(indminusmainlist,indexlist):
    goallist = []
    for ind in indexlist:
        add = True
        for minusind in indminusmainlist:
            #if len(tens) == 1:
            #comp = copy.deepcopy(tens[0])
                #del comp[0]
            if ind == minusind:
                add = False
                break
        if add:
            goallist.append(ind)
    return goallist

"""这里的indandmain为二重序列，symtenmultlist为一个三重序列（每一个张量的每一个加法项都被排过序）"""
def stmlminusiam(indandmain, symtenmultlist):
    goallist = []
    for tens in symtenmultlist:
        linearcal = []
        if len(tens) > 1:
            countlc = 1
            #确保tens中的每一个分量（加法和项）都得到比较
            while countlc <= len(tens):
                comp = copy.deepcopy(tens[countlc - 1])
                del comp[0]
                remain = True
                for ind in indandmain:
                    if comp == ind:
                        remain = False
                        break
                if remain:
                    linearcal.append(tens[countlc - 1])
                countlc += 1
        if linearcal != []:
            goallist.append(linearcal)
    return goallist
#Mainminusind = mainmiusind([[[-1,1,2,3],[1,2,3,4]],[[1,2,2,3]],[[2,2,3,4]]], [[2,3,4]])
#print(Mainminusind)

"""stmlminusiam之中基本为"""

Indandmain = indandmain([[1,2],[1,3]], [[1,2],[1,3],[2,3]])
print(Indandmain)

Stmlminusiam = stmlminusiam([[1,2],[1,3]],[[[3,1,2]],[[2,1,4],[1,1,2]],[[-1,1,3],[2,1,1]]])
print(Stmlminusiam)