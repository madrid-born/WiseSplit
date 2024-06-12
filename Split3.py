from Split2 import split2


def split3(P, X):
    P[0].split(X, 3)
    mp1 = P[1].pick(X)
    mp2 = P[2].pick(X)
    if mp1 != mp2:
        P[1].add(mp1)
        P[2].add(mp2)
        P[0].add(X.splitList[0])
        return
    split2([P[1], P[2]], mp1)
    mp1 = P[1].pick(X)
    mp2 = P[2].pick(X)
    if mp1 != mp2:
        split2([P[1], P[0]], mp1)
        split2([P[2], P[0]], mp2)
        return
    split2([P[1], P[2]], mp1)
    P[0].add(X.splitList[0])