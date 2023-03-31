def nsort(n):
    nlen = len(n)
    count = 0
    for i in range(0, nlen):
        flag = False
        for j in range(0, nlen-1):
            if n[j+1] < n[j]:
                temp = n[j+1]
                n[j+1] = n[j]
                n[j] = temp
                flag = True
            count+=1
        if not flag:
            break
        nlen-=1
    print(count)
    return n

xint = [2,4,1,5,7,6,3,8]
sortedarr = [1,2,3,4,5,6,7,8]
print(nsort(sortedarr))
print(nsort(xint))
