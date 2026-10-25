

def is_same(s1, s2):
    if abs(len(s1) - len(s2)) > 1:
        return False
    
    if len(s1) == len(s2):
        i = 0
        count = 0
        while i < len(s1) and i < len(s2):
            if s1[i] != s2[i]:
                # print(s1[i], s2[i])
                count += 1
            if count > 1:
                return False
            i += 1
        return True
    elif len(s1) > len(s2) or len(s2) > len(s1):
        if len(s1) > len(s2):
            s1, s2 = s2, s1
        i = 0
        f = False
        count = 0
        while i < len(s2) and i < len(s1):
            if s2[i] != s1[i] and f == False:
                count += 1
                f = True
            if f == True:
                if i + 1 < len(s2) and s2[i + 1] != s1[i]:
                    count += 1
                if count > 1:     
                    return False
            i += 1
        return True

# s1, s2 = "pale", "ple"

# s1, s2 = "pales", "pale"


# s1, s2 = "pale", "bale"

# s1, s2 = "pale", "bake"

# print(is_same(s1, s2))
print(is_same("pale", "ple"))    # True
print(is_same("pales", "pale"))  # True
print(is_same("pale", "bale"))   # True
print(is_same("pale", "bake"))   # False
print(is_same("abc", "ab"))      # True
print(is_same("ab", "cab"))      # True
print(is_same("abc", "abcd"))    # True
print(is_same("ab", "abcd"))     # False