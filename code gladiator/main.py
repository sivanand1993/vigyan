import numpy as np
A=np.array([[0,0,0,0],[0,0,1,0],[0,0,0,0]])
B=np.array([[1,0,0,1],[1,0,1,1],[1,0,0,1]])
# A=np.array([[0,0,0],[1,0,1]])
# B=np.array([[1,1,1],[0,1,0]])
m,n=A.shape
def flip(x):
    return 1-x
ans=0
if m<3 or n<3:
    A=flip(A)
    if np.all(A == B) == False:
        ans = -1
    else:
        ans=0
else:
    for i in range(m - 3 + 1):
        for j in range(0, n - 3+1):
            ans += 1
            # print(i,j)
            A[i:i+3,j:j+3]=flip(A[i:i+3,j:j+3])
            print(A)
            if np.all(A==B):
                break
    if np.all(A == B)==False:
        ans=-1''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():
    import numpy as np
    A=[]
    B=[]
    m,n=[int(i) for i in input().split()]
    for a in range(m):
        z=[int(i) for i in input().split()]
        A.append(z)
    for a in range(m):
        z=[int(i) for i in input().split()]
        B.append(z)
    def flip(x):
        return 1-x
    ans=0
    A=np.array(A)
    B=np.array(B)
    if m<3 or n<3:
        ans=-1
        print(ans)
    else:
        if np.all(np.all(A == B)):
            ans=0
        else:
            for i in range(m - 3 + 1):
                for j in range(0, n - 3+1):
                    ans += 1
                    A[i:i+3,j:j+3]=flip(A[i:i+3,j:j+3])
                    if np.all(A==B):
                        break
            if np.all(A == B)==False:
                ans= -1
        print(ans)
main()



print(ans)
