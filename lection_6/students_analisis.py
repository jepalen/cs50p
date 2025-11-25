import csv
import random

def calculate_age():
    return random.randint(20, 55)

with open('students2.csv','r') as view, open ('students_analisis.csv','w') as analysis :
    reader= csv.DictReader(view)
    
    writer = csv.DictWriter(analysis,fieldnames=reader.fieldnames + ["probable_age"])
    writer.writeheader()
    for row in reader:
        row["probable_age"] =calculate_age()
        writer.writerow(row)
        print(f"{row['name']} is in {row['country']} is probably {row['probable_age']}")  
