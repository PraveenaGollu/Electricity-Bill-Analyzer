import json
import csv
import os

BASE = os.path.dirname(os.path.abspath(__file__))

def load(file):
    path = os.path.join(BASE, file)
    try:
        with open(path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save(file, data):
    path = os.path.join(BASE, file)
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

def add_appliance():
    data = load("appliances.json")
    name = input("Appliance name: ")
    watts = float(input("Power in watts: "))
    quantity = int(input("Quantity: "))
    data.append({"name": name, "watts": watts, "quantity": quantity})
    save("appliances.json", data)
    print("Appliance added!")

def record_usage():
    data = load("usage.json")
    name = input("Appliance name: ")
    hours = float(input("Hours per day: "))
    days = int(input("Number of days: "))
    data.append({"name": name, "hours": hours, "days": days})
    save("usage.json", data)
    print("Usage saved!")

def calculate():
    appliances = load("appliances.json")
    usage = load("usage.json")
    results = []

    for u in usage:
        for a in appliances:
            if u["name"].lower() == a["name"].lower():
                units = (a["watts"] * a["quantity"] * u["hours"] * u["days"]) / 1000
                results.append([a["name"], round(units, 2)])

    for item in results:
        print(item[0], ":", item[1], "units")

    total = sum(item[1] for item in results)
    print("Total units:", round(total, 2))
    return total, results

def calculate_bill():
    total, results = calculate()
    if total > 0:
        print("Estimated bill: Rs.", round(total * 3.10 + 50, 2))
        print("Sample rate only, not an official tariff.")

def highest_consumption():
    total, results = calculate()
    if results:
        print("Highest consumption:", max(results, key=lambda x: x[1]))

def export_csv():
    total, results = calculate()
    if results:
        path = os.path.join(BASE, "electricity_report.csv")
        with open(path, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Appliance", "Units"])
            writer.writerows(results)
        print("CSV report created!")

def main():
    while True:
        print("\n1. Add Appliance")
        print("2. Record Usage")
        print("3. Calculate Units")
        print("4. Calculate Bill")
        print("5. Highest Consumption")
        print("6. Export CSV")
        print("0. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_appliance()
        elif choice == "2":
            record_usage()
        elif choice == "3":
            calculate()
        elif choice == "4":
            calculate_bill()
        elif choice == "5":
            highest_consumption()
        elif choice == "6":
            export_csv()
        elif choice == "0":
            print("Thank you!")
            break
        else:
            print("Invalid choice!")

main()
