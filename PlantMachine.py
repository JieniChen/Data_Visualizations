#Author:Jieni Chen
#This is a code for histogram with Seaborn

import pandas as pd
import numpy as np

from scipy import stats, integrate
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("/Users/chenjenny/Documents/Tyson/Plant Machine IOT/result/groupEqMal.csv")
df = df[(df['n'] >= 10)]
df


# In[11]:

plt.figure(figsize=(144,60))
sns.set_style("whitegrid")
ax = sns.barplot(x='Equipment_Number', y='n', data=df)
plt.show()


# In[ ]:




# In[ ]:



