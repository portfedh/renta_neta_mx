# Renta Neta Calculator

This Python script calculates the net income after taxes based on the gross income and a specified income tax rate. The calculator also provides additional details such as the effective tax rate, taxable income, and blind deduction.

## Usage

To use the Renta Neta Calculator, follow these steps:

1. Run the script: python renta_neta_calculator.py

2. Enter the required inputs when prompted:

  - Monthly gross income (Monto de renta mensual)
  - Income tax rate (Tasa de impuestos PF). Use 0.35 if the rate is unknown.

3. The script will then calculate the net income and display the results, including various financial details such as gross income, net income, blind deduction, taxable income, taxes payable, and the effective tax rate.

## Code Overview

The main functionality of the Renta Neta Calculator is implemented in the RentaNeta class. Here's a brief overview of the key methods:

  - __init__(self): Initializes the RentaNeta object by getting user inputs, calculating the net rent, and printing the output.

  - get_inputs(self): Prompts the user for input values, including monthly gross income and income tax rate.

  - calculate_net_rent(self): Performs the calculations to determine net income, blind deduction, taxable income, taxes payable, and effective tax rate.

  - print_output(self): Displays the results in a formatted manner.

The script concludes with a conditional check to run the RentaNeta class if the script is executed directly.

## Note

Make sure to have Python installed on your system to run the script. If Python is not installed, you can download it from python.org.

Feel free to customize the script or incorporate it into your projects as needed.
