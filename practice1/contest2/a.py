def solve():
    n = int(input())
    nums = [int(item) for item in input().split()]
    for i in range(1, len(nums) - 1):
        if nums[i - 1] + nums[i + 1] == nums[i]:
            print(nums[i])

solve()