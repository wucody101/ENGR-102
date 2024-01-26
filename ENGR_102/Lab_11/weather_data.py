# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Cody Wu
# Section:      520
# Assignment:   11.13 : Lab: Weather Data
# Date:         8 November 2023

#open files and read
weather = open("WeatherDataCLL.csv", "r")
weather_data = weather.readline()
weather_data = weather.read().split('\n')
workingset = []

for data in weather_data:
    split = data.split(",")
    workingset.append(split)

minimumtemp = 1000.0
maximumtemp = 0.0
for data in workingset:
    if data[6] != '' :
        if int(data[6]) < minimumtemp:
            minimumtemp = int(data[6])
    if data[5] != '':
        if int(data[5]) > maximumtemp:
            maximumtemp = int(data[5])

print(f'10-year maximum temperature: {maximumtemp} F')
print(f'10-year minimum temperature: {minimumtemp} F')

month = input("Please enter a month: ")
year = input("Please enter a year: ")

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
    monthnum = data[0][0]
    if data[0][1] != '/':
        monthnum += data[0][1]
    monthnum = int(monthnum)
    if months[month] == monthnum and year in data[0][-4:] :
        days += 1
        if data[4] != '' :
            avgTemp += float(data[4])
            avgTempdays += 1
        if data[3] != '' :
            humidity += float(data[3])
            humiditydays += 1
        if data[1] != '' :
            windspeed += float(data[1])
            windspeeddays += 1
        if data[2] != '0' and data[2] != '':
            prepdays += 1

print(f'For {month} {year}:')
print(f'Mean average daily temperature: {(avgTemp / avgTempdays):.1f} F')
print(f'Mean relative humidity: {(humidity / humiditydays):.1f}%')
print(f'Mean daily wind speed: {(windspeed / windspeeddays):.2f} mph')
print(f'Percentage of days with precipitation: {(prepdays / days) * 100:.1f}%')
