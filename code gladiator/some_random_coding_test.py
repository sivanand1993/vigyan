A = [[0,0,0,0],[0,0,1,0],[0,0,0,0]]
B = [[1,0,0,1],[1,0,1,1],[1,0,0,1]]

def flip(A, i, j, lr, lc):
    if (i+2 > lr) or (j+2 > lc):
        return -1
    for x in range(i, i+3):
        for y in range(j, j+3):
            A[x][y] = 1 - A[x][y]
            
def main():
    m, n = len(A), len(A[0])
    if m != len(B) or n != len(B[0]):
        return -1
        
    ans = 0
    for i in range(m):
        for j in range(n):
            if A[i][j] != B[i][j]:
                if flip(A,i,j,m,n) == -1:
                    return -1
                ans += 1
    return ans

if __name__ == "__main__":
    print(main())
            
            