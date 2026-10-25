# Container With Most Water
# You are given an integer array heights where heights[i] represents the height of the 
# i^(th) bar.

# You may choose any two bars to form a container. Return the maximum amount of water a container can store.

# Example 1:

# Input: 
height = [1,7,2,5,4,7,3,6]

# Output: 36

def fill_water(heights):
    def calc_volume(start, end):
        return (end - start) * min(heights[start], heights[end])
    max_volume = 0
    l = 0
    r = len(heights) - 1
    while l < r:
        max_volume = max(max_volume, calc_volume(l, r))
        if heights[l] < heights[r]:
            l += 1
        else:
            r -= 1
    return max_volume







if __name__=='__main__':
    height = [2,2,2]
    print(fill_water(height))

