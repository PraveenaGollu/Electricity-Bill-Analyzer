# Electricity Bill Analyzer

## About the Project

Electricity Bill Analyzer is a Python project that I developed to calculate electricity consumption and estimate electricity bills for household appliances. The main purpose of this project is to help users understand how much electricity they are consuming based on the appliances they use and the number of hours they run them.

In this project, users can add their household appliances by entering the appliance name, power rating and quantity. They can also record how many hours each appliance is used per day and for how many days. Based on these details, the program calculates the total electricity consumption and displays an estimated electricity bill.

## Technologies Used

I developed this project using Python. I used JSON files to store appliance and usage details, the CSV module to generate electricity reports and the OS module to manage file paths.

## How the Project Works

When the program starts, it displays a menu with different options. Users can add appliances, record their usage, calculate electricity units, estimate their bill and identify the appliance with the highest electricity consumption. They can also export their electricity consumption details into a CSV file for future reference.

## Electricity Calculation

The project calculates electricity consumption using the formula:

Units = (Watts × Quantity × Hours × Days) / 1000

For the estimated bill, I used a sample electricity rate of ₹3.10 per unit with an additional fixed charge of ₹50. This is only a sample calculation and not an official electricity tariff.

## How to Run

To run this project, first download the repository to your computer and open the project folder in VS Code or Terminal. Make sure Python 3 is installed and execute the command `python3 main.py`.

The program will display a menu where you can select the required operation and enter the details.

## What I Learned

While developing this project, I learned how to work with Python functions, loops, conditional statements, lists, dictionaries and file handling. I also gained practical experience in storing data using JSON files and generating reports using CSV files.

## Author

Praveena Gollu

GitHub: https://github.com/PraveenaGollu
