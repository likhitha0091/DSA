import math
class Solution:
    def print_divisors(self, N):
        res = []
		for i in range(1, int(math.sqrt(N))+1):
		    if N%i == 0:
		        res.append(i)
		        if (N//i)!=i:
		            res.append(N//i)
		res.sort()
		for x in res:
		    print(x, end = " ")
