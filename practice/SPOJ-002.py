#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import math


def segment_sieve(a, b):
    N = int(math.ceil(math.sqrt(b)))
    is_prime_small = [True for x in range(N)]
    is_prime = range(a, b)

    for i in range(2, N):
        if is_prime_small[i]:
            for j in range(2*i, N, i):
                is_prime_small[j] = False
            for j in range(max(2, (a+i-1)/i)*i, b, i):
                is_prime[j-a] = 1
    
    return filter(lambda x: x > 1, is_prime)


def main():

    T = int(sys.stdin.readline())
    for t in range(T):
        if t > 0:
            print
        n, m = [int(x) for x in sys.stdin.readline().split(' ')]
        primes = segment_sieve(n, m+1)
        for i in primes:
            print i

if __name__ == '__main__':
    main()
