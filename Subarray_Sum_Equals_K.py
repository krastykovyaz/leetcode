class Solution(object):
    def subarraySum(self, nums, k):
        count = 0
        sum = 0
        dic = {}
        dic[0] = 1
        for num in nums:
            sum += num
            count += dic.get(sum - k, 0)
            dic[sum] = dic.get(sum, 0) + 1
        return count



if __name__ == '__main__':
    s = Solution()
    nums = [-1, -1, 1]
    k = 0
    print(s.subarraySum(nums, k))
