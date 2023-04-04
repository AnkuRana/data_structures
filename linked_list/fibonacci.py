import time


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-2) + fibonacci(n-1)


def fibo_iter(n):
    first = 0
    second = 1
    for i in range(n):
        if i <= 1:
            print(i)
        else:
            next_term = first + second
            print(next_term)
            first = second
            second = next_term


def fibo_iter_bottom_up(n):
    dic = []
    for i in range(n):
        if i <= 1:
            dic.append(i)
        else:
            dic.append(dic[i-1] + dic[i-2])
    print(dic[n-1])


memo = {}


def fibo_memo(k):
    if k in memo:
        return memo[k]
    else:
        if k <= 1:
            return k
        else:
            memo[k] = fibo_memo(k - 2) + fibo_memo(k - 1)
            return memo[k]


# start = time.time()
# for n in range(30):
#     fibonacci(n)
# end = time.time()
# print(f"fibonacci: {end-start} seconds")
temp = 0
start = time.time()
for n in range(30):
    temp = fibo_memo(n)
print(temp)
end = time.time()
print(f"fibo_memo: {end-start} seconds")
# start = time.time()
# fibo_iter(30)
# end = time.time()
# print(f"fibo_iter: {end-start} seconds")
start = time.time()
fibo_iter_bottom_up(30)
end = time.time()
print(f"fibo_iter_bottom_up: {end-start} seconds")
