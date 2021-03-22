#!/usr/bin/env python
# coding: utf-8

# In[8]:


import numpy as np
import pandas as pd


# In[9]:


Vac_Stats = pd.read_csv('country_vaccination_stats.csv')
Vac_Stats = pd.DataFrame(Vac_Stats)


# In[26]:


Vac_Stats['daily_vaccinations'] = Vac_Stats['daily_vaccinations'].fillna(Vac_Stats.groupby('country')['daily_vaccinations'].transform("min"))
Vac_Stats['daily_vaccinations'].fillna(0,inplace = True)
Vac_Stats.groupby('country')['daily_vaccinations'].median().nlargest(3)


# In[ ]:




