import csv
import json

with open("rules.json", mode = "r") as file:
    rules = json.load(file)
    rate = rules["daily_fine"]

with open("library.csv" , mode = "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row["Status"] == "Late":
            days = int(row["Days Overdue"])
            total_fine = days * rate
            print(f"Book: {row['Book Name']} | Total Fine: ${total_fine:.2f}")

        else:
            print("No fine for this book")

        


