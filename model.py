# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle
df= pd.read_csv('DS.CSV')
print(df)
X=df.iloc[:,0:5]
y=df.iloc[:,5]
# Fitting Random Forest Regression to the dataset
# import the regressor



from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X,y)

pickle.dump(regressor, open('model.pkl','wb'))

model = pickle.load(open('model.pkl','rb'))
print(model.predict([[2, 9, 6, 6, 9]]))

