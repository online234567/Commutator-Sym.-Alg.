"""系数的sum"""
def sum(summ):
    if summ == []:
        return []
    else:
        mlensumm = len(summ)-1
        find = summ[0]
        copyfind = find.copy()
        count = 1
        """删除find多少次(目标是全部删掉)"""
        findminus = find.copy()
        sign = find[0]
        findminus[0] = - sign
        findcount = 1 #至少删除一次
        summary = sign #考虑初始符号
        """summary代表考虑正负find1的第一位的值"""
        while findcount <= mlensumm:
            if summ[findcount] == find:
                summary += sign
                count += 1
            elif summ[findcount] == findminus:
                summary -= sign
                count += 1
                summ[findcount][0] = sign
            findcount += 1
        delcount = 1
        copyfind[0] = summary
        while delcount <= count :
            summ.remove(find)
            delcount += 1
        s = sum(summ)
        """每次找一种并计数，从summ中删掉所有值，之后再在剩余的张量中找，返回的值已经是求过和了"""
        if summary != 0:
            s.append(copyfind)
        return s

#List = [[1,2,5,8],[-1,3,5,7],[1,2,5,8],[1,3,5,7]]
#Sum = sum(List)
#print(Sum)

