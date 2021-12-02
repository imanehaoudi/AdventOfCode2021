import pandas as pd
import numpy as np 

#part 1
data = pd.read_csv('input1.txt', header = None)
sol1 = (data.diff()>0).sum()
print(sol1)

#part 2
new_data_1 = data.shift(-1)
new_data_2 = data.shift(-2)
sol2 = ((new_data_1+new_data_2+data).diff()>0).sum()
print(sol2)

