from sym import sym
from tens1 import nrc, rcn
from sum import sum
from index import find_all_index
from compare import indminusmain
from sort import sort

"""第一个ind长度为lenth，第二个ind长度为rank + 1"""
def lsymtenmult(ind,tens,rank):
    product = []
    lenth = len(ind)
    lenlist = []
    count = 1
    while count <= lenth:
        lenlist.append(count)
        count += 1
    Sym = sym(lenlist).copy()
    for grpele in Sym:
        permuind = []
        countass = 1
        while countass <= lenth:
            permuind.append(ind[grpele[countass-1]-1])
            countass += 1
        for addtens in tens:
            addprod = []
            tenind = 1
            #print(addprod[0])
            coeff = addtens[0]
            #addprod.append(coeff)
            while tenind <= lenth:
                coord = []
                t = tenind
                # print(t)
                #print("a")
                coord.append(ind[grpele[t - 1] - 1])
                coord.append(addtens[t])
                # print(coord)
                ij = nrc(coord[0], rank).copy()
                kl = nrc(coord[1], rank).copy()
                #print(coord)
                # print(kl)
                if ij[1] == kl[0]:
                    appd = rcn(ij[0], kl[1], rank)
                    addprod.append(appd)
                    # print(tens1)
                else:
                    addprod = []
                    break
                tenind += 1
            if addprod != []:
                sortedprod = sort(addprod)
                sortedprod.insert(0,coeff)
                product.append(addprod)
            #print(product)
    if product != []:
        prod = sum(product)#sum帮助我们合并同类项
    else:
        prod = []
    return prod

def rsymtenmult(tens,ind,rank):
    product = []
    lenth = len(ind)
    lenlist = []
    count = 1
    while count <= lenth:
        lenlist.append(count)
        count += 1
    Sym = sym(lenlist).copy()
    for grpele in Sym:
        permuind = []
        countass = 1
        while countass <= lenth:
            permuind.append(ind[grpele[countass-1]-1])
            countass += 1
        for addtens in tens:
            addprod = []
            tenind = 1
            #print(addprod[0])
            coeff = addtens[0]
            #addprod.append(coeff)
            while tenind <= lenth:
                coord = []
                t = tenind
                # print(t)
                #print("a")
                coord.append(addtens[t])
                coord.append(ind[grpele[t - 1] - 1])
                # print(coord)
                ij = nrc(coord[0], rank).copy()
                kl = nrc(coord[1], rank).copy()
                #print(coord)
                # print(kl)
                if ij[1] == kl[0]:
                    appd = rcn(ij[0], kl[1], rank)
                    addprod.append(appd)
                    # print(tens1)
                else:
                    addprod = []
                    break
                tenind += 1
            if addprod != []:
                sortedprod = sort(addprod)
                sortedprod.insert(0,coeff)
                product.append(addprod)
            #print(product)
    if product != []:
        prod = sum(product)#sum帮助我们合并同类项
    else:
        prod = []
    return prod
"""搜集所有的列表的乘积，包括左右乘积,输出为一个三重列表"""
def symtenmultlist(Ind, tenslist, rank):
    symtens = []
    for ind in Ind:
        for tens in tenslist:
            lproduct = lsymtenmult(ind, tens, rank)
            rproduct = rsymtenmult(tens, ind, rank)
            if lproduct != []:
                symtens.append(lproduct)
            if rproduct != []:
                symtens.append(rproduct)
    return symtens

STM = lsymtenmult([1,3],[[1,1,2]],2)
print(STM)
List = []
List.append(STM)
STML = indminusmain(symtenmultlist(find_all_index(2,2),List,2),find_all_index(2,2))
print(STML)