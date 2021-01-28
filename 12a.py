import pandas as pd

ds1 = pd.Series([2, 4, 6, 8])
ds2 = pd.Series([1, 3, 5, 7])
dsum = ds1 + ds2
dsub = ds1 - ds2
dmul = ds1 * ds2
ddiv = ds1 / ds2

print(ds1)
print(ds2)
print(dsum)
print(dsub)
print(dmul)
print(ddiv)
