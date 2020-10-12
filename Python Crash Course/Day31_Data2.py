import csv
from datetime import datetime
import matplotlib.pyplot as plt

# El Ejercicio ya acepta las 2 fuentes de datos por buscar por indices

#filename = 'data/death_valley_2018_simple.csv'
filename = 'data/sitka_weather_2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    
    max_temp = header_row.index('TMAX')
    min_temp = header_row.index('TMIN')
    date_col = header_row.index('DATE')
    title_file = header_row.index('NAME')

    # Get dates and high and low temperatures from this file
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[date_col], '%Y-%m-%d')
        try:
            high = int(row[max_temp])
            low = int(row[min_temp])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# Plot the high and low temperatures
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot

title =f"Daily high and low temperatures -2018\n{row[title_file]}, CA"
plt.title(title, fontsize=20)
plt.xlabel('',fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()