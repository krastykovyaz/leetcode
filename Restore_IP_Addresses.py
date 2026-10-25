# A valid IP address consists of exactly four integers separated by single dots. Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.
# For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.
# Given a string s containing only digits, return all possible valid IP addresses that can be formed by inserting dots into s. You are not allowed to reorder or remove any digits in s. You may return the valid IP addresses in any order.

 

# Example 1:
s = "25525511135"
# Output: ["255.255.11.135","255.255.111.35"]

def restore_ip_address(s):
    res = []
    def backtrack(start, path):
        if start == len(s):
            if len(path) == 4:
                res.append('.'.join(path))
        for l in range(1,4):
            if start + l > len(s):
                break
            subs = s[start:start+l]
            if (subs.startswith('0') and len(subs) > 1) or int(subs) > 255:
                continue
            backtrack(start + l, path + [subs])
    backtrack(0,[])
    return res



    

if __name__=='__main__':
    print(restore_ip_address(s))

