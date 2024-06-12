def split2(P, X):
    P[0].split(X, 2)
    P[1].add(P[1].pick(X))
    P[0].add(X.splitList[0])
    if X.parent is not None:
        X.parent.splitList.remove(X)

