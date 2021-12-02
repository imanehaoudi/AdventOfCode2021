import pandas as pd
import numpy as np 

data = pd.read_csv('input2.txt', header = None)
print(data)

data[['direction','X']] = data[0].str.split(' ',expand=True)
print(data)

forward = data.loc[data['direction']=='forward','X'].apply(int)
down = data.loc[data['direction']=='down','X'].apply(int)
up = data.loc[data['direction']=='up','X'].apply(int)

#part 1
print(forward.sum()*(down.sum()-up.sum()))

#part 2
aim = 0
depth = 0
horizontal = 0
for i in range(data.shape[0]):
  aim += (data['direction'][i]=='down')*int(data['X'][i]) - (data['direction'][i]=='up')*int(data['X'][i])
  horizontal += (data['direction'][i]=='forward')*int(data['X'][i])
  depth +=(data['direction'][i]=='forward')*int(data['X'][i])*aim

print(depth*horizontal)