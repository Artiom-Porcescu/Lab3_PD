import csv

# Чтение исходного CSV-файла
with open('dataset.csv', 'r') as file:
    reader = csv.reader(file)
    data = list(reader)

# Разделение на даты и данные
dates = [row[0] for row in data]
values = [row[1] for row in data]

# Запись в файлы X.csv и Y.csv
with open('X.csv', 'w', newline='') as x_file, open('Y.csv', 'w', newline='') as y_file:
    x_writer = csv.writer(x_file)
    y_writer = csv.writer(y_file)

    for date, value in zip(dates, values):
        x_writer.writerow([date])
        y_writer.writerow([value])
