def fiban(n):
    if n==1:
        return 0
    if n==2:
        return 1
    return fiban(n-1) + fiban(n-2)
print(fiban(5))