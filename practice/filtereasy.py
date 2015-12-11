def prime(n):
    if n == 1 or n == 2:
        return n
    else:
        for i in range(2, n+1):
            if n%i == 0 and i != n:
                break
            elif i == n:
                return n
l = range(1,101)
print l
lf = filter(prime, l)
print lf
