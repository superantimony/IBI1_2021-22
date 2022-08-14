import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir("c:/users/HP/IBI_2021-22/practical 7")
covid_data = pd.read_csv("full_data.csv")
#show columns one and three for every row between (and including) 0 and 10
covid_data.iloc[0:11, 0:3:2]
#compute the mean number of new cases in the United Kingdom and China.
L = []
i = 0
for i in range(0, 7996):
    if covid_data.iloc[i,1]=="China":
        L.append(True)
        i+=i+1
    else:
        L.append(False)
        i+=i+1
China_data = covid_data.iloc[China]
China_new_cases = China_new_data.iloc[:,2:3]
x = 0
for x in range(0,7996):
    if covid_data.iloc[x,1]=="United Kingdom":
        L.append(True)
        x+=x+1
    else:
        L.append(False)
        x+=x+1
Kingdom_data= = covid_data.iloc[United Kingdom]
Kingdom_new_cases = Kingom_new_data.iloc[:,2:3]
#creata boxplot of new cases in Kindom and China
labels ='new cases in China', 'new cases in Kingdom'
China_new_cases = China_new_data.iloc[:,1]
Kingdom_new_cases = Kingom_new_data.iloc[:,1]
plt.boxplot(China_new_cases)
plt.title("New cases in China")
plt.ylabel("China")
plt.show()
plt.boxplot(Kingdom_new_cases)
plt.title("New cases in Kingdom")
plt.ylabel("Kingdom")
plt.show()
#plot both new cases in China and Kingdom
plt.plot(new_cases, China_datas,'ro')
plt.plot(new_cases, Kingdom_data, 'b+')
plt.title("new cases in China and Kingdom")
plt.xlabel("time")
plt.ylabel("cases")
plt.show()
#answer for question
Spain = []
for i in range(7996):
    if covid_data.iloc[i,1]=="Spain":
        Spain.append(True)
    else:
        Spain.append(False)
Spain_data = covid_data.iloc[Spain]
Spain_datas=Spain_data.iloc[:,0]
Spain_total_cases=Spain_data.iloc[:,4]
plt.plot(Spain_datas, Spain_tatol_cases,'b+')
plt.xlabel('date')
plt.ylabel('total cases in Spain')
plt.show()