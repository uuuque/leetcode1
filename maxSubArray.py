class Solution:
    def maxsubarray(self, nums):
        for i in range(1, len(nums)):
            nums[i] = max(nums[i], nums[i-1] + nums[i])
        return max(nums)


if __name__ == '__main__':
    a = Solution()
    num = [int(n) for n in input().split()]
    print(a.maxsubarray(num))
