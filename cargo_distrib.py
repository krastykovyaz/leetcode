weights = [1,2,3,4,5,6,7,8,9,10]
days = 5
# Output: 15

def form_cargo(weights, days):
    def count_days(capacity):
        req_days = 1
        cargo = 0
        for w in weights:
            if w + cargo > capacity:
                req_days += 1
                cargo = 0
            cargo += w
        return req_days <= days

    left = max(weights)
    right = sum(weights)
    while left < right:
        mid = (left + right) // 2
        if count_days(mid):
            right = mid
        else:
            left = mid + 1
    return left

if __name__=='__main__':
    print(form_cargo(weights, days))

    
            

