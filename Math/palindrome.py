class Solution:
    def isPalindrome(self, n):
		# code here
		og = n
		rev = 0
		while n>0:
		    digit = n%10
		    rev = (rev *10)+ digit 
		    n = n//10
		if rev==og:
		    return True
		else:
		    return False
