# 1
install.packages('survminer')
install.packages("survival")
library(survminer)
library(survival)
# Importing the dataset
Patient <- read.csv('C:\\Users\\WIN10\\Desktop\\LEARNING\\DS\\survival\\Patient.csv')
attach(Patient)
str(Patient)
# Define variables 
time <- Followup
event <- Eventtype
group <-Scenario  # unemployment insurance can take 2 values 0 or 1 
# Descriptive statistics
summary(time)
table(event)
table(group)
# Kaplan-Meier non-parametric analysis
kmsurvival <- survfit(Surv(time, event) ~ 1)
summary(kmsurvival)
plot(kmsurvival, xlab="Time", ylab="Survival Probability")
ggsurvplot(kmsurvival, data=Patient, risk.table = TRUE)

# Kaplan-Meier non-parametric analysis by group
kmsurvival1 <- survfit(Surv(time, event) ~ group)
summary(kmsurvival1)
plot(kmsurvival1, xlab="Time", ylab="Survival Probability")
ggsurvplot(kmsurvival1, data=Patient, risk.table = TRUE)

