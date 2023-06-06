n = int(input())
nums = input().split()
negatives = 0
num_zeros = 0
nums_list = []
for x in nums:
    if int(x) < 0:
        negatives += 1
    if int(x) == 0:
        num_zeros += 1
    nums_list.append(int(x))


nums_list.sort()

coins = 0

if (negatives  + num_zeros) % 2 == 0:
    for index,num in enumerate(nums_list):
        if num < 0:
            coins += (-num) - 1
        elif num == 0:
            coins += 1
        else:
            coins += num - 1
else:
    for index,num in enumerate(nums_list):
            if num < 0 and negatives > 1:
                coins += (-num) - 1
                negatives -= 1
            elif num < 0  and num_zeros >= 1:
                coins += (-num) - 1
                num_zeros -= 1
            elif num < 0 :
                coins += 1 - num
            elif num == 0:
                coins += 1
            else:
                coins += num  -  1
print(coins)