class Solution:
    def armstrongNumber (self, n):
        og = n
		rev = 0
		while n>0:
		    digit = n%10
		    rev = rev +(digit * digit * digit)
		    n = n//10
		if rev==og:
		    return True
		else:
		    return False
