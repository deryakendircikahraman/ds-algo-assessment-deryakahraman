class Solution:
    def planVacation(self, miles, target):
        # Time complexity: O(n)
        # Space complexity:O(1)
        
        total=0
        left=0
        shoertest=float('inf')
        for right in range(len(miles)):
            total+=miles[right]
            while total>=target:
                shoertest=min(shoertest,right-left+1)
                total-=miles[left]
                left+=1
        return shoertest if shoertest!=float('inf') else 0  
