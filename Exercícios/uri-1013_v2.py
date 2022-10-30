nums = input().split()

for i in range(3):
    nums[i] = int(nums[i])

maior = maior01 = (nums[0] + nums[1] + abs(nums[0] - nums[1])) / 2
maior = int((maior + nums[2] + abs(maior - nums[2])) / 2)

print(f"{maior} eh o maior")
