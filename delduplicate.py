"""Except for coefficients"""
import copy
from mini import sortdoublelist

def delduplicate(list0):
    if list0 == []:
        return []
    elif len(list0) == 1:
        return list0
    else:
        #lenlist = len(list1)
        list1 = sortdoublelist(list0)
        findcoff = copy.deepcopy(list1[0])
        #delete = False
        #print(findcoff)
        find = copy.deepcopy(findcoff)
        #print(find)
        if len(find) > 1:
            countcl = 1
            cofflistf = []
            while countcl <= len(find):
                cofflistf.append(find[countcl - 1][0])
                #print(countcl)
                #print(find[countcl - 1][0])
                #print(cofflistf)
                countcl += 1
            #print(cofflistf)
        for tens in find:
            #print(find)
            del tens[0]
            #print(find)
            #print(find)
            #print(findcoff)
            #print(list1)
        count = 2
        """删除find多少次(目标是留下第一个)"""
        findcount = 1 #至少删除一次
        #summary = sign #考虑初始符号
        """summary代表考虑正负find1的第一位的值"""
        while findcount <= len(list1):
            #print(findcount)
            check = copy.deepcopy(list1[findcount - 1])
            if len(check) == len(findcoff) and len(check) > 1:
                countclc = 1
                #print(len(check))
                #print(len(find))
                cofflistc = []
                while countclc <= len(check):
                    cofflistc.append(check[countclc - 1][0])
                    countclc += 1
                countrat = 1
                coffratio = []
                while countrat <= len(check):
                    coffratio.append(cofflistf[countrat - 1] / cofflistc[countrat - 1])
                    countrat += 1
                judgerat = True
                countratio = 1
                while countratio < len(check):
                    judgerat = judgerat and coffratio[countratio - 1] == coffratio[countratio]
                    countratio += 1
                #print(cofflistf)
                #print(cofflistc)
                #print(coffratio)
                #print(judgerat)
            for tens in check:
                del tens[0]
                #print(find)
            if find == check:
                if len(find) == 1:
                    #print(list1)
                    del list1[findcount - 1]
                    #print(list1)
                    #delete = True
                elif len(find) > 1 and len(find) == len(check) and judgerat:
                    #print(judgerat)
                    #print(list1)
                    del list1[findcount - 1]
                    #print(list1)
                    #delete = True
                else:
                    findcount += 1
            else:
                findcount += 1
            #print(findcount)
            #print(findcount)
            #print(list1)
        slist = delduplicate(list1)
        """每次找一种并计数，从summ中删掉所有值，之后再在剩余的张量中找，返回的值已经是求过和了"""
        #print(findcoff)
        slist.insert(0, findcoff)
        slist = sortdoublelist(slist)
        return slist

#list1 = [[[6,1,3,7]],[[5,1,3,7]],[[2,1,3,8],[-2,1,3,6]],[[2,1,3,8],[-1,1,3,6]]]
list1 = [[[-2, 2, 3], [-2, 1, 4]], [[-1, 1, 4], [-1, 2, 3]]]
List = delduplicate(list1)
print(List)