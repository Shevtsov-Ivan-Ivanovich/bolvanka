import csv
with open('db.csv', encoding='utf-8') as db:
    read_file = csv.reader(db)
    for row in read_file:
        print(row)