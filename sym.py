def sym(someofonetolenth):
    if len(someofonetolenth) == 1:
        firstnum = someofonetolenth[0]
        Sym = [[firstnum]]
        return Sym
    else:
        Sym = []#"""之后使用递归，我们需要长度为lenth的表，且所有的words不重复，所以假设我们已经对于长度lenth-1的串做到这一点""" #"""someofonetolenth中被假设不带有相同的数字"""
        for firstnum in someofonetolenth:
            missitems = someofonetolenth.copy()
            missitems.remove(firstnum)
            #print(missitems)
            Symmid = sym(missitems)
            for grpele1 in Symmid:
                grpele = grpele1.copy()
                grpele.insert(0,firstnum)
                Sym.append(grpele)
            firstnum += 1
        #for grpele in Sym:
            #if len(grpele) < len(someofonetolenth):
                #Sym.remove(grpele)
        return Sym

#List = [1, 2, 3]
#Sym = sym(List).copy()
#matrixSym = [ Sym[i:i+4] for i in range(0,len(Sym),4) ]
#for l in matrixSym:
    print(l)