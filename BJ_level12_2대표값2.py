nums = list(int(input()) for _ in range(5))
nums.sort()
sum = 0

for i in range(5):
    sum += nums[i]

print(int(sum/5))
print(nums[2])

# 다른 풀이
nums = list(int(input()) for _ in range(5))
nums.sort()
print(int(sum(nums)/5))
print(nums[2])

# 다른 풀이2
nums = [int(input()) for i in range(5)]
print(sum(nums)//5)
print(sorted(nums)[2])