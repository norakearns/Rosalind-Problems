import math
n = 95
k = 9

answer = 1
for i in range(k):
    answer *= (n-i)
print(answer%1000000)

# x=(n*(n-1)*(n-2)*(n-3)*(n-4)*(n-5)*(n-6)*(n-7)*(n-8))
# print(x%1000000)