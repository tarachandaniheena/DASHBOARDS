
# coding: utf-8

# Importing and reading Excel file

# In[2]:

import pandas as pd  
df=pd.read_excel('SECTOR(1).xlsx')
df.head();
df


# In[ ]:

Renaming Columns


# In[18]:

df1=df.rename(columns = {'CH4.1':'CH4','CH4.2':'CH4','CH4.3':'CH4','CH4.5':'CH4','CH4.6':'CH4','CH4.7':'CH4',
                        'CO2.1':'CO2','CO2.2':'CO2','CO2.3':'CO2','CO2.4':'CO2','CO2.5':'CO2','CO2.6':'CO2','CO2.7':'CO2',
                        'HFCs.1':'HFCs','HFCs.2':'HFCs','HFCs.3':'HFCs','HFCs.4':'HFCs','HFCs.5':'HFCs','HFCs.6':'HFCs',
                        'N20.1':'N20','N20.2':'N20','N20.3':'N20','N20.4':'N20','N20.5':'N20','N20.6':'N20','N20.7':'N20',
                        'PFCs.1':'PFCs','PFCs.2':'PFCs','PFCs.3':'PFCs','PFCs.4':'PFCs','PFCs.5':'PFCs','PFCs.6':'PFCs',
                        'SF6.1':'SF6','SF6.2':'SF6','SF6.3':'SF6','SF6.4':'SF6','SF6.5':'SF6','SF6.6':'SF6'
                       })
df1
    


# Deleting column Gas as it contains Nan Values

# In[22]:

del df1['Gas']
df1


# In[29]:

df2=df1{'CH4','CO2','HFCs','N20','PFCs','SF6'}.replace('-',0)


# In[27]:

df2


# In[ ]:



