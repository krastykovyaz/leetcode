# You are given an array of integers heights where heights[i] represents the height of a bar. The width of each bar is 1.

# Return the area of the largest rectangle that can be formed among the bars.

# Note: This chart is known as a histogram.

# Example 1:

# Input: 
# heights = [7,1,7,2,2,4]
 
# Output: 8
# Example 2:

# Input: 
heights = [1,3,7]

# Output: 7

def lagest_hist(heights):
    stack = []
    max_vol = 0
    heights.append(0)
    for i, h in enumerate(heights):
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            width = i - stack[-1] - 1 if stack else i
            max_vol = max(max_vol, height * width)
        stack.append(i)
    return max_vol
        

if __name__=='__main__':
    print(lagest_hist(heights))
