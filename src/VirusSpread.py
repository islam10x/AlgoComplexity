def virusSpread(n,p):
    if n==0 :
        return p
    else :
        return p+virusSpread(n-1,p*2)
print(virusSpread(3,2))

def virusSpreaditerative(n,p):
    result = 0
    for i in range(n+1):
        result += p
        p *= 2
    return result
print(virusSpreaditerative(3,2))

# O(n) Complexity

