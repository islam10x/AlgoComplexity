def pascal(n,k):
    if k==0 or k==n :
        return 1
    else :
        return pascal(n-1,k-1)+pascal(n-1,k)

# O(2^n) Complexity

for i in range(0,5) :
    print("\n")
    for j in range(0,i+1) :
        print(pascal(i,j),end=" ")