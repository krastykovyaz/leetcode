nums = [6,7,2,3,4,5]

# Output: 1

def min_search(nums):
    left = 0
    right = len(nums) - 1
    mid = 0
    while left < right:
        mid = (left + right) // 2
        if nums[mid] >= nums[right]:
            left = mid + 1
        else:
            right = mid
    return nums[left]

if __name__=="__main__":
    print(min_search(nums))

