n = int(input())
result_sq = list([0] * (n + 1))
result_sq[0] = 0
result_sq[1] = 1

for i in range(2, n+1):
    result_sq[i] = result_sq[i - 1] + result_sq[i - 2]

print(result_sq[n])