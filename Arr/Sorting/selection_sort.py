from random import randint

nums=[]
for _ in range(32):
    nums.append(randint(1, 50))

for i in range(len(nums)):
    min_index = i
    for j in range(i, len(nums)):
        if nums[j] < nums[min_index]:
            min_index = j
    nums[i], nums[min_index] = nums[min_index], nums[i]
    print(nums)