# Trapping Rain Water
# You are given an array of non-negative integers height which represent an elevation map. Each value height[i] represents the height of a bar, which has a width of 1.

# Return the maximum area of water that can be trapped between the bars.

# Example 1:
# Input: 
height = [0,2,0,3,1,0,1,3,2,1]

# Output: 9

def water_count(height):
    prefix = [0] * len(height)
    suffix = [0] * len(height)
    prefix[0] = height[0]
    for i in range(1, len(height)):
        prefix[i] = max(prefix[i-1], height[i])
    suffix[-1] = height[-1]
    for i in range(1, len(height)):
        i = len(height) - i - 1
        suffix[i] = max(suffix[i + 1], height[i])
    water = 0
    for i in range(len(height)):
        water += min(suffix[i], prefix[i]) - height[i]
    return water

if __name__=='__main__':
    # height = [4,2,0,3,2,5]
    print(water_count(height))

