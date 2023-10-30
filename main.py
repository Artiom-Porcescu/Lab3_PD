import csv
from collections import defaultdict
from datetime import datetime, timedelta

#first task
with open('dataset.csv', 'r') as file:
    reader = csv.reader(file)
    data = list(reader)

dates = [row[0] for row in data]
values = [row[1] for row in data]

with open('X.csv', 'w', newline='') as x_file, open('Y.csv', 'w', newline='') as y_file:
    x_writer = csv.writer(x_file)
    y_writer = csv.writer(y_file)

    for date, value in zip(dates, values):
        x_writer.writerow([date])
        y_writer.writerow([value])

#second task
with open('dataset.csv', 'r') as file:
    reader = csv.reader(file)
    data = list(reader)

data_by_year = defaultdict(list)
for row in data:
    year = row[0][:4]
    data_by_year[year].append(row)

for year, year_data in data_by_year.items():
    output_file_name = f"{year}0101_{year}1231.csv"
    with open(output_file_name, 'w', newline='') as output_file:
        writer = csv.writer(output_file)
        writer.writerows(year_data)
