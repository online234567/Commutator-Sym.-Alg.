"""index.py没有用到"""
"""main代表commutator"""
from sym import sym
from tens1 import tensor1
from tens2 import tensor2
from sort import sort
from sum import sum
from index import find_all_index
from delduplicate import delduplicate
from compare import mainmiusind, indminusmain, stmlminusiam, indandmain
from symtenmult import symtenmultlist

def mainindividual(ind1, ind2, rank):
    lenth = len(ind1)
    ranklist = []
    count = 1
    while count <= lenth:
        ranklist.append(count)
        count += 1
    Sym = sym(ranklist).copy()
    #print(Sym)
    position = 1
    summ = []
    while position <= lenth:
        for grpele in Sym:
            stens1 = sort(tensor1(ind1,ind2,grpele,position,rank))
            stens2 = sort(tensor2(ind1,ind2,grpele,position,rank))
            if stens1 != []:
                summ.append(stens1)
            if stens2 != []:
                summ.append(stens2)
            #print(stens1)
            #print(stens2)
        position += 1
    #print(summ)
    tures = sum(summ)
    return tures

#Comm = mainindividual([1,2,3],[5,3,8],3)
#print(Comm)

def main(lenth,rank):
    mainlist = []
    Ind = find_all_index(lenth,rank)
    for ind1 in Ind:
        for ind2 in Ind:
            appd = mainindividual(ind1,ind2,rank)
            #这一步除掉空列表
            if appd != []:
                mainlist.append(appd)
    return mainlist

lenth = 3
rank = 3

mainlist = main(lenth,rank)
Mainlist = delduplicate(mainlist)#这一步重排以及除掉重复的部分
print(mainlist)
countprint = 1
while countprint <= len(Mainlist):
    print(Mainlist[countprint - 1])
    countprint += 1
Matrixlist = [ Mainlist[i:i+4] for i in range(0,len(Mainlist),4) ]
for l in Matrixlist:
    print(l)

#countprint2 = 1
#Mainlistminusind = mainmiusind(Mainlist,find_all_index(3,3))
#while countprint2 <= len(Mainlistminusind):
#    print(Mainlistminusind[countprint2 - 1])
#    countprint2 += 1

countprint3 = 1
IndminusMainlist = indminusmain(Mainlist,find_all_index(lenth,rank))
while countprint3 <= len(IndminusMainlist):
    print(IndminusMainlist[countprint3 - 1])
    countprint3 += 1

print("split")

countprint4 = 1
Indminusprodlist = indminusmain(symtenmultlist(find_all_index(lenth,rank),Mainlist,rank),find_all_index(lenth,rank))
while countprint4 <= len(Indminusprodlist):
    print(Indminusprodlist[countprint4 - 1])
    countprint4 += 1

print("split")

#countprint5 = 1
#stmlminusiam0 = delduplicate(stmlminusiam(indandmain(Indminusprodlist,find_all_index(lenth,rank)),(symtenmultlist(find_all_index(lenth,rank),Mainlist,rank))))
#while countprint5 <= len(stmlminusiam0):
    #print(stmlminusiam0[countprint5 - 1])
    #countprint5 += 1

Stmlminusiam = delduplicate(stmlminusiam(indandmain(Indminusprodlist,find_all_index(lenth,rank)),(symtenmultlist(find_all_index(lenth,rank),Mainlist,rank))))

MatrixSMS = [ Stmlminusiam[i:i+4] for i in range(0,len(Stmlminusiam),4) ]
for l in MatrixSMS:
    print(l)