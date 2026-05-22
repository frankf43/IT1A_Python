from random import randint

nums=[]
for _ in range(32):
    nums.append(randint(1, 50))

for i in range(1,len(nums)):
    item = nums[i]
    j = i - 1
    while j >= 0 and (nums[j] > item):
        nums[j+1] = nums[j]
        j -= 1
    nums[j+1] = item
    print(nums)