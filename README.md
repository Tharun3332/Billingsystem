# 🍔 Burger Billing System in Python

A simple console-based restaurant billing system developed in Python. This project simulates a basic billing system for a burger outlet, allowing customers to place orders, apply student discounts, add delivery charges, and optionally include a tip before generating a final bill.

## 📌 Features

- Displays a menu of food items with prices.
- Accepts multiple item orders with quantity.
- Calculates total amount dynamically.
- Applies 20% discount for students.
- Adds 5% delivery charge if required.
- Option to add a tip (₹2, ₹5, or ₹10).
- Displays a formatted final bill using the `tabulate` library.

## 🛠️ Technologies Used

- **Python** (core logic)
- **Tabulate** – for printing structured tables
- Control Structures – `if-else`, `while` loops
- Built-in data types – `lists`, `append`, `input`, etc.

## 🖥️ How It Works

1. On execution, a menu with food items is shown.
2. Users can enter the food item name and quantity.
3. Optionally apply a student discount.
4. Choose whether delivery is needed (adds a charge).
5. Optionally add a tip to the total bill.
6. A final bill is displayed with all details in tabulated form.

## 🔧 Setup Instructions

1. Make sure Python is installed (preferably Python 3).
2. Install the `tabulate` module if not already installed:

   ```bash
   pip install tabulate
