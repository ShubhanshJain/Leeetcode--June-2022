class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        M, N = len(matrix), len(matrix[0])
        
        self.dp = [[0 for _ in range(N+1)] for _ in range(M+1)]
        
        for r in range(1, M+1):
            for c in range(1, N+1):
                self.dp[r][c] = matrix[r-1][c-1] + self.dp[r][c-1]
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        output = 0
        for r in range(row1+1, row2+2):
            output += self.dp[r][col2+1] - self.dp[r][col1]
            
        return output    
