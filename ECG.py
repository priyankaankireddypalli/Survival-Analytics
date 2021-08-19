# 2
import lifelines
import pandas as pd
# importing the dataset
ECG = pd.read_excel("C:\\Users\\WIN10\\Desktop\\LEARNING\\DS\\survival\\ECG_Surv.xlsx")
ECG.head()
ECG.describe()
ECG["survival_time_hr"].describe()
# Spell is referring to time 
T = ECG.survival_time_hr

# Importing the KaplanMeierFitter model to fit the survival analysis
from lifelines import KaplanMeierFitter
# Initiating the KaplanMeierFitter model
kmf = KaplanMeierFitter()
# Fitting KaplanMeierFitter model on Time and Events for death 
kmf.fit(T, event_observed=ECG.group)
# Time-line estimations plot 
kmf.plot()

# Over Multiple groups 
# For each group, here group is ui
ECG.group.value_counts()
# Applying KaplanMeierFitter model on Time and Events for the group "1"
kmf.fit(T[ECG.alive==1], ECG.alive[ECG.alive==1], label='1')
ax = kmf.plot()
# Applying KaplanMeierFitter model on Time and Events for the group "0"
kmf.fit(T[ECG.alive==0], ECG.alive[ECG.alive==0], label='0')
ax = kmf.plot()
