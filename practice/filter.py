# def is_odd(n):
    # return n % 2 == 1

# filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])
# # [1, 5, 9, 15]

# def not_empty(s):
    # return s and s.strip()

# filter(not_empty, ['A', '', 'B', None, 'C', '  '])
# ['A', 'B', 'C']

import math
# try to use filter() to pick out the prime number in 1~100
def is_prime(m):
	
	for i in range(0, m+1):
		p[i] = True
	for i in range(3,m+1):
		if i%2 == 0:
			p[i] = False
		# else: p[i] = True
	for i in p:
		if p[i]:
			for i in range(i,math.sqrt(m+1),i):
				p[i] = False
				# print i
	for i in p:
		if p[i]:
			print i
# n = raw_input("input n = ")
# print int(n)
p = is_prime(10)
p
			