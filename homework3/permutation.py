def permutation(n):
    p = []
    return permNext(n, p)

def permNext(n, p):
    if len(p) == n:
        print(p)
        return
    else:
        for x in range(n):
            if x not in p:
                p.append(x)
                permNext(n, p)
                p.pop()
             
        
permutation(3)

