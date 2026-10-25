preds = [0.95, 0.83, 0.76, 0.60, 0.55, 0.52, 0.48, 0.40, 0.30, 0.10]
true  = [1,    1,    1,    1,    0,    0,    0,    0,    0,    0]

total = len(preds)
total_pos = sum(true)
total_neg = total - total_pos
best_score = 0

sorted_preds_tr = sorted(zip(preds, true), key=lambda x: -x[0])
res = None
tp, fp = 0, 0
i = 0
while i < len(sorted_preds_tr):
    if sorted_preds_tr[i][1] == 1:
        tp += 1
    else:
        fp += 1
    tn = total_neg - fp
    acc = (tp+tn)/total
    if best_score < acc:
        res = sorted_preds_tr[i]  
        best_score = acc
    i += 1
print(res)
