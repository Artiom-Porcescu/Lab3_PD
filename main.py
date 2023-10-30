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

#third task
with open('dataset.csv', 'r') as file:
    reader = csv.reader(file)
    headers = next(reader)
    data = list(reader)

dates = [datetime.strptime(row[0], '%Y/%m/%d') for row in data]

data_by_week = defaultdict(list)
for date, row in zip(dates, data):
    start_of_week = date - timedelta(days=date.weekday())
    end_of_week = start_of_week + timedelta(days=6)
    week_key = f"{start_of_week.strftime('%Y%m%d')}_{end_of_week.strftime('%Y%m%d')}"
    data_by_week[week_key].append(row)

for week, week_data in data_by_week.items():
    output_file_name = f"{week}.csv"
    with open(output_file_name, 'w', newline='') as output_file:
        writer = csv.writer(output_file)
        writer.writerow(headers)
        writer.writerows(week_data)
