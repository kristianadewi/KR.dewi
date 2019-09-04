#!/usr/bin/env python
# coding: utf-8

# In[126]:


import pandas as pd
from scipy import stats
import numpy as np
import seaborn as sns 
dewi = pd.read_csv("DEWI.csv")
dewi


# In[ ]:





# In[132]:


kolom = data.columns.tolist()
for u in kolom:
    dw=[x for x in dewi[u]]
    desc= data[x].describe()
    array= [x for x in desc]
    print("Spesifikasi ",u)
    print("Mean: ",array[1])
    print("Median: ",np.median(np.array(ds)))
    print("Modus: ", stats.mode(ds))
    print("SD: ",np.std(ds))
    print("varian: ", stats.variation(ds))
    print("Skewness: ",stats.skew(ds))
    print("Q1: ",array[4])
    print("Q2: ",array[5])
    print("Q3: ",array[6])
    
    print("\n")
    


# In[ ]:




