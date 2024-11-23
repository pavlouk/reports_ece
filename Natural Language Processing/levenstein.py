def levenstein(S, T):
    
    if S == " ":
        return len(T)
    if T == " ":
        return len(S)
    p1 = levenstein(S, T[:-1]) + 1
    p2 = levenstein(S[:-1], T) + 1
    p3 = levenstein(S[:-1], T[:-1])
    if S[-1] != T[-1]:
        p3 += 1
    
    return min(p1, p2, p3)
