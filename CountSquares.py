def countSquares(N):
    count = 0
    for i in range(1, N):
        if i**2 < N:
            count+=1
        else:
            break
    return count
n = int(input())
ans = countSquares(n)
print(ans)
