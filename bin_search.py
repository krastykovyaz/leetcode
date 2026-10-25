# class Solution:

def peakIndexInMountainArray(arr) -> int:
        start_idx = 0
        def bst(arr_):
            global start_idx
            if len(arr_) == 1:
                return start_idx
            middle = len(arr_) // 2
            left = arr_[:middle]
            right = arr_[middle:]
            
            if len(right) > 0 and len(left) > 0 and left[-1] < right[0]:
                start_idx += len(arr_)
                print(right, start_idx)
                return peakIndexInMountainArray(right)
            if len(right) > 0 and len(left) > 0 and left[-1] > right[0]:
                start_idx += middle
                print(left, start_idx)
                return bst(left)

        return bst(arr)
        
if __name__ == "__main__":
    # s = Solution()
    sample = [0,1,2,3,1]
    print(peakIndexInMountainArray(sample))

        