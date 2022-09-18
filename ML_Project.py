#!/usr/bin/env python
# coding: utf-8

# # Petrol Consumption problem

# # 1) Decision Tree Regressor

# In[72]:


pwd


# In[73]:


import numpy as np
import pandas as pd


# In[74]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[75]:


# Loading the dataset

Csv_dataset=pd.read_csv("petrol_consumption.csv")


# In[76]:


Csv_dataset.head()


# In[77]:


X = Csv_dataset.drop('Petrol_Consumption', axis=1)
y = Csv_dataset['Petrol_Consumption']


# In[78]:


X.head()


# In[79]:


y.head()


# In[80]:


Csv_dataset.describe()


# In[81]:


from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.10,random_state=0)


# In[82]:


# Training the model

from sklearn.tree import DecisionTreeRegressor
Reg = DecisionTreeRegressor()
Reg.fit(X_train,y_train)
y_pred = Reg.predict(X_test)
y_pred


# In[83]:


# Creating a dataframe

Data_frame = pd.DataFrame({"Actual":y_test, "predicted":y_pred})
Data_frame


# In[84]:


# Finding the Errors

from sklearn import metrics
print('Mean Absolute Error:',metrics.mean_absolute_error(y_test,y_pred))
print('Mean Square Error:',metrics.mean_squared_error(y_test,y_pred))
print('Root Mean Square Error:',np.sqrt(metrics.mean_squared_error(y_test,y_pred)))

***
Mean of the Target variable which is Petrol_Consumption is 576.770833
10% of Mean = 57.677

Decision Tree Regressor is a Good Model because it's Root Mean Square Error value is less than the 10% Mean of the Target variable

***
# # 2) Random Forest Regressor

# In[85]:


# Loading the dataset

dataset_Forest=pd.read_csv("petrol_consumption.csv")


# In[86]:


dataset_Forest.head()


# In[87]:


X = dataset_Forest.drop('Petrol_Consumption', axis=1)
y = dataset_Forest['Petrol_Consumption']


# In[88]:


X.head()


# In[89]:


y.head()


# In[90]:


dataset_Forest.describe()


# In[91]:


from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.10,random_state=0)


# In[92]:


# Training the model

from sklearn.ensemble import RandomForestRegressor
For_Reg = RandomForestRegressor(n_estimators=40, random_state=0)
For_Reg.fit(X_train,y_train)
y_pred = For_Reg.predict(X_test)
y_pred


# In[93]:


# Creating a dataframe

Data_frame01 = pd.DataFrame({"Actual":y_test, "predicted":y_pred})
Data_frame01


# In[94]:


# Finding the Errors

from sklearn import metrics
print('Mean Absolute Error:',metrics.mean_absolute_error(y_test,y_pred))
print('Mean Square Error:',metrics.mean_squared_error(y_test,y_pred))
print('Root Mean Square Error:',np.sqrt(metrics.mean_squared_error(y_test,y_pred)))

*** 
Mean of the Target variable which is Petrol_Consumption is 576.770833
10% of Mean = 57.677

Random Forest Regressor is also a Good Model because it's Root Mean Square Error value is less than the 10% Mean of the Target variable

***
# # 3) Linear Regression

# In[95]:


# Loading the dataset

dataset_linear=pd.read_csv("petrol_consumption.csv")


# In[96]:


dataset_linear.head()


# In[97]:


X = dataset_linear.drop('Petrol_Consumption', axis=1)
y = dataset_linear['Petrol_Consumption']


# In[98]:


X.head()


# In[99]:


y.head()


# In[100]:


dataset_linear.describe()


# In[101]:


from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.10,random_state=0)


# In[102]:


# Training the model

from sklearn.linear_model import LinearRegression
lin_Reg = LinearRegression()
lin_Reg.fit(X_train,y_train)
y_pred = lin_Reg.predict(X_test)
y_pred


# In[103]:


# Creating a dataframe

Data_frame02 = pd.DataFrame({"Actual":y_test, "predicted":y_pred})
Data_frame02


# In[104]:


# Finding the Errors

from sklearn import metrics
print('Mean Absolute Error:',metrics.mean_absolute_error(y_test,y_pred))
print('Mean Square Error:',metrics.mean_squared_error(y_test,y_pred))
print('Root Mean Square Error:',np.sqrt(metrics.mean_squared_error(y_test,y_pred)))

***
Mean of the Target variable which is Petrol_Consumption is 576.770833
10% of Mean = 57.677

Linear Regresion is not a Good Model because it's Root Mean Square Error value is greater than the 10% Mean of the Target variable.

***