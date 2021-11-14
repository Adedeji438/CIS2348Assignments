numbers = input().split()
sorted_list = []

for num in numbers:
    num = int(num)
    if num >= 0:
        sorted_list.append(num)

sorted_list.sort()
for num in sorted_list:
    print(num, end=' ')