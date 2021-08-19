# 1
pip install lifelines
import lifelines
import pandas as pd
# importing the dataset
patient= pd.read_csv("C:\\Users\\WIN10\\Desktop\\LEARNING\\DS\\survival\\Patient.csv")
# Performing EDA
patient.head()
patient.describe()
patient.drop(['PatientID'], axis =1, inplace =True) # Dropping ID column
# Creating the dummy variables
patient = pd.get_dummies(patient)
patient["Followup"].describe()
# Spell is referring to time 
T = patient.Followup

# Importing the KaplanMeierFitter model to fit the survival analysis
from lifelines import KaplanMeierFitter
# Initiating the KaplanMeierFitter model
kmf = KaplanMeierFitter()
# Fitting KaplanMeierFitter model on Time and Events for death 
kmf.fit(T, event_observed=patient.Scenario_A)
# Time-line estimations plot 
kmf.plot()

# Over Multiple groups 
# For each group, here group is ui
patient.Scenario_A.value_counts()
# Applying KaplanMeierFitter model on Time and Events for the group "1"
kmf.fit(T[patient.Eventtype==1], patient.Eventtype[patient.Eventtype==1], label='1')
ax = kmf.plot()
# Applying KaplanMeierFitter model on Time and Events for the group "0"
kmf.fit(T[patient.Eventtype==0], patient.Eventtype[patient.Eventtype==0], label='0')
ax = kmf.plot()


