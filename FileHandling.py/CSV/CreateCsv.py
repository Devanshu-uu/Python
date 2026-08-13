import csv

with open("Students.csv","w",newline="") as file:
    writer=csv.writer(file)
    writer.writerow(["Name","Marks","City"])
    writer.writerow(["Devanshu",100,"Delhi"])
    writer.writerow(["Gulshan",95,"Delhi"]


                    )
with open("Students.csv","r") as file:
    reader=csv.reader(file)
    for row in reader:
        print(row)
    