def nrc(n, rank):
    rc = []
    coord0 = n % rank
    if coord0 == 0:
        r = int(n / rank)
    else:
        r = int((n - (n % rank)) / rank) + 1
    c = n % rank
    if c == 0:
        c += rank
    rc.append(r)
    rc.append(c)
    return rc


def rcn(r, c, rank):
    n = (r - 1) * rank + c
    return n


def tensor1(ind1, ind2, grpele, position, rank):
    dd = rank * rank
    tens1 = []
    tens1.append(1)
    lentens = len(ind1)
    # print(tens1)
    tenind = 1
    while tenind <= lentens:
        coord = []
        if tenind < position:
            t = tenind - 1
            # coord 是矩阵乘法的两个乘积项
            coord.append(ind2[grpele[t] - 1])
            coord.append(ind1[t])
        elif tenind >= position:
            t = tenind - 1
            # print(t)
            coord.append(ind1[t])
            coord.append(ind2[grpele[t] - 1])
        # print(coord)
        ij = nrc(coord[0], rank).copy()
        kl = nrc(coord[1], rank).copy()
        # print(kl)
        if ij[1] == kl[0]:
            appd = rcn(ij[0], kl[1], rank)
            tens1.append(appd)
            # print(tens1)
        else:
            tens1 = []
            return tens1
            break
        tenind += 1
    return tens1

# Tens1 = tensor1([1,2,3],[5,4,7],[2,1,3],2,3)
# print(Tens1)