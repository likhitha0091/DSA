class Solution:
    def minAnd2ndMin(self, arr):
        # code here
        if len(arr)<2:
            return [-1]
        smallest = arr[0]
        for i in range(len(arr)):
            if arr[i]<smallest:
                smallest = arr[i]
        secsmall = float('inf')
        for i in range(len(arr)):
            if arr[i]>smallest and arr[i] < secsmall:
                secsmall = arr[i]
        if secsmall == float('inf'):
            return [-1]
                
        return [smallest, secsmall]
        
        
