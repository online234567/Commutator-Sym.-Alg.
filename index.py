
# d = int(input("Input the rank of matrix"))
# lenth = int(input("Input the lenth of series"))


def find_all_index(lenth ,rank):
    # """首先需要判定是否lenth为1，为1的时候，我们直接得到想要的字符串"""
    d = rank
    dd = d * d
    if lenth == 1:
        Ind = []
        nlenth = 1
        while nlenth <= dd:
            index1 = []
            index1.insert(0 ,nlenth)
            Ind.append(index1)
            nlenth += 1
        return Ind
    elif lenth > 1:
        """之后进行递归，先假设我们已经找到了所有的lenth-1的字符串(这一步假设会通过调用实现)"""
        nlenth = 1
        Index = find_all_index(lenth -1 ,rank)
        Ind = []
        """不能用Ind是因为我们在Ind中添加有lenth长度的字符串，但是那些不是我想要的"""
        while nlenth <= dd:
            for index1 in Index:
                # print(Index)
                # 上一步定义index1
                if nlenth <= index1[0]:
                    index2 = index1.copy()
                    index2.insert(0 ,nlenth)
                    # print(index1)
                    index = index2.copy()
                    Ind.append(index)
            nlenth += 1
        for index in Ind:
            # print(index)
            if len(index) < lenth:
                # print(index)
                Ind.remove(index)
        """这两步做的实际上是“替换”，这里的做法更加简单粗暴"""
        return Ind


step = 0
Ind = find_all_index(2 ,2)
lenlonglist = len(Ind)
students = [1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,10] # assume numbers are students
matrixInd = [ Ind[i: i +4] for i in range(0 ,len(Ind) ,4) ]
for l in matrixInd:
    print(l)