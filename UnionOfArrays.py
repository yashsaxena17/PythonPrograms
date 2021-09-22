def doUnion(self,a,n,b,m):
    l = []
    for i in range(n):
        if a[i] not in l:
            l.append(a[i])
        
    for i in range(m):
        if b[i] not in l:
            l.append(b[i])
                
    return len(l)
    
array1 = [1,2,3,4,5]
n = len(array1)
array2 = [1,2]
m = len(array2)

ans = doUnion(array1, n, array2, m)
print(ans)
