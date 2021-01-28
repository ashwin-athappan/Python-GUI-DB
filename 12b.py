import pandas as pd

d1 = {'a': 100, 'b': 200, 'c': 300, 'd': 400}

print('Dictionary', d1)

nd = pd.Series(d1)
print(f'Pandas Series\n{nd}')
