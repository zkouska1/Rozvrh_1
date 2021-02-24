import csv


with open('address.csv','r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
print("snad")
























