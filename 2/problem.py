class Solution:
    def isValidSudoku(self, matrix):
        # Time complexity: 
        # Space complexity:
        
        from collections import defaultdict

        rows = defaultdict(set)
        cols = defaultdict(set)
     

        for i in range(9):  # row
            for j in range(9):  # column
                val = matrix[i][j]
                
                if val == '.':
                    continue
                if val in rows[i] or val in cols[j]:            
                    return False
                rows[i].add(val)                        
                cols[j].add(val)
                # Check 3x3 sub-box ?
        return True