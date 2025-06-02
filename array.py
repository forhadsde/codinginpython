n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
reversed_array = []
for i in range(n):
    reversed_array.append(arr[n-i-1])
print(' '.join(str(i) for i in reversed_array))
