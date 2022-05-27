import os
os.chdir full_data.csv("/home/hp/Practical7")
os.getcwd()
import pandas as pd
covid_data = pd.read_csv("ful_data.csv")
import matplotlib.pyplot as plt
import numpy as np
print(os.chdir("home/hp/IBI_2021_22/Practical7"))
print(os.getcwd())
print(os.listdir("home/hp/IBI_2021_22/Practical7"))
f = open("full_data.csv", encoding='UTF-8')
print(covid_data)
print(covid_data.head(5))
covid_data.info()
print(covid_data.describe())
print(covid_data.iloc[0, 1])
print(covid_data.iloc[2,0:5])
print(covid_data.iloc[0:2,:])
print(covid_data.iloc[0:10:2,0:5])
print(covid_data.iloc[0:3,[0,1,3]])
my_columns = [True, True, False, True, False, False]
print(covid_data.iloc[0:3,my_columns])
print(covid_data.loc[2:4,"date"])
print(covid_data.loc[0:81,"total_cases"])
x = [False, True, False, False, False, False]
print(covid_data.iloc[:, x])
x1 = [False, True, False, False, False, True]
y = []
def select(location):
    for i in range(len(covid_data)):
        if covid_data.iloc[i,1] == location:
            y.append(True)
        else:
            y.append(False)
select("Afghanistan")
print(covid_data.iloc[y,x1])
y2 = []
for i in range(len(covid_data)):
    if covid_data.iloc[i, 1] == "China":
        y2.append(True)
    else:
        y2.append(False)
print(covid_data.iloc[y2, :])
china = covid_data.iloc[y2, : ]
china_dates = covid_data.iloc[y2, 0]
china_cases = covid_data.iloc[y2, 2]
china_death = covid_data.iloc[y2, 3]
print(np.average(china_cases))
print(np.average(china_death))
plt.boxplot((china_death, china_cases), vert = False)
plt.title('china death and china cases')
plt.show()
plt.boxplot(china_cases, vert = False)
plt.title('china cases only')
plt.show()
plt.boxplot(china_death, vert = False)
plt.title('china death only')
plt.show()
plt.plot(china_dates, china_death, "ro", china_dates, china_cases, 'b+')
plt.xticks(china_dates.iloc[0:len(china_dates):4],rotation=-90)
plt.title('Total cases and death in China')
plt.ylabel('number')
plt.show()
y3 = []
for i in range(len(covid_data)):
    if covid_data.iloc[i, 1] == "United States":
        y3.append(True)
    else:
        y3.append(False)
print(covid_data.iloc[y3, :])
US_dates = covid_data.iloc[y3, 0]
US_cases = covid_data.iloc[y3, 2]
US_death = covid_data.iloc[y3, 3]
plt.boxplot((US_death, US_cases), vert = False)
plt.title('Total cases and deaths in the United States')
plt.show()
plt.plot(US_dates, US_death, "ro", US_dates, US_cases, 'b+')
plt.xticks(US_dates.iloc[0:len(US_dates):4],rotation=-90)
plt.title('Total cases and death in the United States')
plt.ylabel('number')
plt.show()