class Solution:
    def largest(self, arr):
        # code here
      # Method1(Optimal-TC->O(N))
        largest = arr[0]
        for i in range(len(arr)):
           if arr[i]>largest:
                largest = arr[i]
        return largest


       # Method2(BruteForce-TC->O(NlogN))
        arr.sort()
        return arr[len(arr)-1]
        
        
        
