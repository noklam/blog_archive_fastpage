# Match Pattern
(y.+_ls)\s=\sflatten\((y1_ls)\)
# replace pattern
$1 = flatten($1)

# Source
```
y1_ls = flatten(y1_ls)
y2_ls = flatten(y1_ls)
y3_ls = flatten(y1_ls)
y1_pred_ls = flatten(y1_ls)
y2_pred_ls = flatten(y1_ls)
y3_pred_ls = flatten(y1_ls)
```
# Target
```
y1_ls = flatten(y1_ls)
y2_ls = flatten(y2_ls)
y3_ls = flatten(y3_ls)
y1_pred_ls = flatten(y1_pred_ls)
y2_pred_ls = flatten(y2_pred_ls)
y3_pred_ls = flatten(y3_pred_ls)
```