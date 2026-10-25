# [1,4,5,2,3,9,8,11,0] => "0-5,8-9,11"
# [1,4,3,2] => "1-4"
# [1,4] => "1,4"

nums = [1,4]
snums = sorted(nums)
res = []
def form_answer(start, end):
    if start == end:
        return str(end)
    return f"{start}-{end}"

st=None
en=None
for n in snums:
    if en==None:
        st=n
        en=n
    elif en==1+n:
        en=n
    else:
        res.append(form_answer(st,en))
        st=n
        en=n
else:
    res.append(form_answer(st,en))

print(', '.join(res))