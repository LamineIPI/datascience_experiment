# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import sklearn
import pandas as pd
from sklearn.model_selection import train_test_split
import supervised
#pour l'entraînement automatique:
from supervised.automl import AutoML

df_co2 =  pd.read_csv(r"C:\Users\uc\Desktop\M2 Data Mining\Ateliers\datascience_experiment\data\raw\mars-2014-complete.csv", sep  = ";")

df_co2 = df_co2.drop(columns = ['Unnamed: 26', 'Unnamed: 27', 'Unnamed: 28', 'Unnamed: 29'])

df_co2 = df_co2[df_co2['co2'].isna() == False]

## Train & test

y = df_co2['co2'].values
X = df_co2.drop(columns = ['co2'])

x_train,x_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)


# 4. AutoML
automl = AutoML(total_time_limit=5*60,mode='Explain',random_state=42,ml_task='regression')
#fit models
automl.fit(X_train,y_train)
#predictions
predictions = automl.predict(X_test)
#generate html report
automl.report()



