# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Cody Wu
# Section:      520
# Assignment:   12.15 : Lab: Plotting Data
# Date:         18 November 2023

import numpy as np
import matplotlib.pyplot as plt

#open files and read
weather = open("/Users/codywu/FALL 2023/ENGR_102/Lab_12/WeatherDataCLL.csv", "r")
weather_data = weather.readline()
weather_data = weather.read().split('\n')
workingset = []

for data in weather_data:
    split = data.split(",")
    workingset.append(split)

minimumtemp = 1000.0
maximumtemp = 0.0

#plot 1
fig, ax1 = plt.subplots()
color = 'tab:red'
ax1.set_xlabel('date')
ax1.set_ylabel('Maximum Temperature, F')
ax1.set_title('Maximum Temperature and Average Wind Speed')
maxtemps = []
for data in workingset:
    if data[6] != '' :
        if int(data[6]) < minimumtemp:
            minimumtemp = int(data[6])
    if data[5] != '':
        maximumtemp = int(data[5])
        maxtemps.append(maximumtemp)

p1 = ax1.plot(maxtemps, color=color, label='Max temp')
ax2 = ax1.twinx()

color = 'tab:blue'
ax2.set_ylabel('Average Wind Speed, mph')
windspeeds = []


months = {'January' : 1, 'February' : 2, 'March' : 3, 'April' : 4, 'May' : 5, 'June' : 6, 'July' : 7, 'August' : 8, 
          'September' : 9, 'October' : 10, 'November' : 11, 'December' : 12}

avgTemp = 0.0
avgTempdays = 0.0

humidity = 0.0
humiditydays = 0.0

windspeed = 0.0
windspeeddays = 0.0

prepdays = 0.0
days = 0.0

for data in workingset:
    if data[1] != '' :
        windspeed = float(data[1])
        windspeeds.append(windspeed)

p2 = ax2.plot(windspeeds, color=color, label='Avg wind')
fig.tight_layout()
ax = p1 + p2
labels = [l.get_label() for l in ax]
plt.legend(ax, labels, loc='lower left')
plt.show()

#plot 2
fig, ax3 = plt.subplots()
bins = np.linspace(0, 20, 30)
ax3.hist(windspeeds, bins, edgecolor='black')
ax3.set_xlabel('Average Wind Speed, mph')
ax3.set_ylabel('Number of days')
ax3.set_title('Histogram of Average Wind Speed')
plt.show()

#plot 3
fig, ax4 = plt.subplots()
ax4.set_xlabel('Average Relative Humidity (%)')
ax4.set_ylabel('Precipitation (in)')
ax4.set_title('Precipitaiton vs Average Relative Humidity')

humidities = []
for data in workingset:
    if data[3] != '' :
        humidity = float(data[3])
        humidities.append(humidity)

precipitation = []
for data in workingset:
    monthnum = data[0][0]
    if data[0][1] != '/':
        monthnum += data[0][1]
    monthnum = int(monthnum)
    if (monthnum == 10 and data[0][-4:] == '2013') or (monthnum == 2 and data[0][-4:] == '2015') or (data[0] == '11/30/2016') or (data[0] == '2/28/2017') or (data[0] == '4/16/2018') or (data[0] == '12/12/2019') or (data[0] == '5/31/2022'):
        continue
    if data[2] != '':
        rainlevel = float(data[2])
        precipitation.append(rainlevel)

ax4.scatter(humidities, precipitation)
plt.show()

#plot 4
fig, ax5 = plt.subplots()
ax5.set_xlabel('Month')
ax5.set_ylabel('Average Temperature, F')
ax5.set_title('Temperature by Month')

avg1 = []
avg2 = []
avg3 = []
avg4 = []
avg5 = []
avg6 = []
avg7 = []
avg8 = []
avg9 = []
avg10 = []
avg11 = []
avg12 = []

low1 = []
low2 = []
low3 = []
low4 = []
low5 = []
low6 = []
low7 = []
low8 = []
low9 = []
low10 = []
low11 = []
low12 = []

high1 = []
high2 = []
high3 = []
high4 = []
high5 = []
high6 = []
high7 = []
high8 = []
high9 = []
high10 = []
high11 = []
high12 = []

for data in workingset:
    monthnum = data[0][0]
    if data[0][1] != '/':
        monthnum += data[0][1]
    monthnum = int(monthnum)
    if monthnum == 1:
        if data[4] != '' :
            avgTemp = float(data[4])
            avg1.append(avgTemp)
        if data[6] != '' :
            minimumtemp = int(data[6])
            low1.append(minimumtemp)
        if data[5] != '':
            maximumtemp = int(data[5])
            high1.append(maximumtemp)
    elif monthnum == 2:
        if data[4] != '' :
            avgTemp = float(data[4])
            avg2.append(avgTemp)
        if data[6] != '' :
            minimumtemp = int(data[6])
            low2.append(minimumtemp)
        if data[5] != '':
            maximumtemp = int(data[5])
            high2.append(maximumtemp)
    elif monthnum == 3:
        if data[4] != '' :
            avgTemp = float(data[4])
            avg3.append(avgTemp)
        if data[6] != '' :
            minimumtemp = int(data[6])
            low3.append(minimumtemp)
        if data[5] != '':
            maximumtemp = int(data[5])
            high3.append(maximumtemp)
    elif monthnum == 4:
        if data[4] != '' :
            avgTemp = float(data[4])
            avg4.append(avgTemp)
        if data[6] != '' :
            minimumtemp = int(data[6])
            low4.append(minimumtemp)
        if data[5] != '':
            maximumtemp = int(data[5])
            high4.append(maximumtemp)
    elif monthnum == 5:
        if data[4] != '' :
            avgTemp = float(data[4])
            avg5.append(avgTemp)
        if data[6] != '' :
            minimumtemp = int(data[6])
            low5.append(minimumtemp)
        if data[5] != '':
            maximumtemp = int(data[5])
            high5.append(maximumtemp)
    elif monthnum == 6:
        if data[4] != '' :
            avgTemp = float(data[4])
            avg6.append(avgTemp)
        if data[6] != '' :
            minimumtemp = int(data[6])
            low6.append(minimumtemp)
        if data[5] != '':
            maximumtemp = int(data[5])
            high6.append(maximumtemp)
    elif monthnum == 7:
        if data[4] != '' :
            avgTemp = float(data[4])
            avg7.append(avgTemp)
        if data[6] != '' :
            minimumtemp = int(data[6])
            low7.append(minimumtemp)
        if data[5] != '':
            maximumtemp = int(data[5])
            high7.append(maximumtemp)
    elif monthnum == 8:
        if data[4] != '' :
            avgTemp = float(data[4])
            avg8.append(avgTemp)
        if data[6] != '' :
            minimumtemp = int(data[6])
            low8.append(minimumtemp)
        if data[5] != '':
            maximumtemp = int(data[5])
            high8.append(maximumtemp)
    elif monthnum == 9:
        if data[4] != '' :
            avgTemp = float(data[4])
            avg9.append(avgTemp)
        if data[6] != '' :
            minimumtemp = int(data[6])
            low9.append(minimumtemp)
        if data[5] != '':
            maximumtemp = int(data[5])
            high9.append(maximumtemp)
    elif monthnum == 10:
        if data[4] != '' :
            avgTemp = float(data[4])
            avg10.append(avgTemp)
        if data[6] != '' :
            minimumtemp = int(data[6])
            low10.append(minimumtemp)
        if data[5] != '':
            maximumtemp = int(data[5])
            high10.append(maximumtemp)
    elif monthnum == 11:
        if data[4] != '' :
            avgTemp = float(data[4])
            avg11.append(avgTemp)
        if data[6] != '' :
            minimumtemp = int(data[6])
            low11.append(minimumtemp)
        if data[5] != '':
            maximumtemp = int(data[5])
            high11.append(maximumtemp)
    elif monthnum == 12:
        if data[4] != '' :
            avgTemp = float(data[4])
            avg12.append(avgTemp)
        if data[6] != '' :
            minimumtemp = int(data[6])
            low12.append(minimumtemp)
        if data[5] != '':
            maximumtemp = int(data[5])
            high12.append(maximumtemp)


average1 = sum(avg1) / len(avg1)
average2 = sum(avg2) / len(avg2)
average3 = sum(avg3) / len(avg3)
average4 = sum(avg4) / len(avg4)
average5 = sum(avg5) / len(avg5)
average6 = sum(avg6) / len(avg6)
average7 = sum(avg7) / len(avg7)
average8 = sum(avg8) / len(avg8)
average9 = sum(avg9) / len(avg9)
average10 = sum(avg10) / len(avg10)
average11 = sum(avg11) / len(avg11)
average12 = sum(avg12) / len(avg12)

monthNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
highY = [max(high1), max(high2), max(high3), max(high4), max(high5), max(high6), max(high7), max(high8), max(high9), max(high10), max(high11), max(high12)]
lowY = [min(low1), min(low2), min(low3), min(low4), min(low5), min(low6), min(low7), min(low8), min(low9), min(low10), min(low11), min(low12)]
averageBar = [average1, average2, average3, average4, average5, average6, average7, average8, average9, average10, average11, average12]

ax5.bar(monthNumbers, averageBar, color='yellow')
p1 = ax5.plot(monthNumbers, highY, color='red', label = 'High T')
p2 = ax5.plot(monthNumbers, lowY, color='blue', label = 'Low T')
ax = p1 + p2
labels = [l.get_label() for l in ax]
ax5.set_xticks(np.arange(1,13))
ax5.set_yticks(np.arange(0,120,20))
plt.legend(ax, labels, loc='upper right')
plt.show()
