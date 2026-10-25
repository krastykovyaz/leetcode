arr = [12, 16, 22, 30, 35, 39, 42, 45, 48, 50, 53, 55, 56]
k = 4
x = 4

def find_k(arr, k, x):
    if len(arr) < k or len(arr) == 0:
        return arr
    center = arr[x]
    left = x - 1
    right = x + 1
    res = []
    while right < len(arr) or left > 0:
        if right > len(arr):
            res.append(arr[left])
            left -= 1
        elif left <= 0:
            res.append(arr[right])
            right += 1
        else:
            if abs(arr[right] - arr[x]) > abs(arr[left] - arr[x]):
                res.append(arr[left])
                left -= 1
            else:
                res.append(arr[right])
                right += 1
        if k == 0:
            return res
        k -= 1

print(find_k(arr, k, x))
