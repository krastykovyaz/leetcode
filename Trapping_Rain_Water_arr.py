# You are given an array of non-negative integers height which represent an elevation map. Each value height[i] represents the height of a bar, which has a width of 1.

# Return the maximum area of water that can be trapped between the bars.

# Example 1:



# Input: 
height = [0,2,0,3,1,0,1,3,2,1]

# Output: 9
def account_water(height):
    def account(left, right, i):
        return min(left, right) - height[i]
    if not len(height):
        return None
    prefix = [0] * len(height)
    prefix[0] = height[0]
    for i in range(1, len(height)):
        prefix[i] = max(height[i], prefix[i - 1])
    suffix = [0] * len(height)
    suffix[-1] = height[-1]
    for i in range(len(height) - 2, -1, -1):
        suffix[i] = max(height[i], suffix[i + 1])
    out = 0
    for i, heigh in enumerate(height):
        out += account(prefix[i], suffix[i], i)
    return out
    
    

if __name__=='__main__':
    print(account_water(height))
