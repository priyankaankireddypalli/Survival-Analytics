# 2
library(readxl)
library(survminer)
library(survival)
# Importing the dataset
ECG <- read_excel('C:\\Users\\WIN10\\Desktop\\LEARNING\\DS\\survival\\ECG_Surv.xlsx')
attach(ECG)
str(ECG)
# Define variables 
time <- survival_time_hr
event <- alive
group <- group
# Unemployment insurance can take 2 values 0 or 1 
# Descriptive statistics
summary(time)
table(event)
table(group)

# Kaplan-Meier non-parametric analysis
kmsurvival <- survfit(Surv(time, event) ~ 1)
summary(kmsurvival)
plot(kmsurvival, xlab="Time", ylab="Survival Probability")
ggsurvplot(kmsurvival, data=ECG, risk.table = TRUE)

# Kaplan-Meier non-parametric analysis by group
kmsurvival1 <- survfit(Surv(time, event) ~ group)
summary(kmsurvival1)
plot(kmsurvival1, xlab="Time", ylab="Survival Probability")
ggsurvplot(kmsurvival1, data=ECG, risk.table = TRUE)

