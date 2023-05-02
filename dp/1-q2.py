
n = int(input())

time_list = [a_i for a_i in map(int, input().split(' '))]
sum_list = [0 for _ in range(n)]

result = 0
i = 1
while i < n:
    if i == 1:
        sum_list[i] += time_list[1]
        i += 1
        continue
    
    sum_list[i] = min(
        sum_list[i - 1] + time_list[i],
        sum_list[i - 2] + time_list[i] * 2
    )

    i += 1

print(sum_list[-1])