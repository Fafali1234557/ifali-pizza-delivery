# 🍕 Ifali's Pizza Delivery

[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Project](https://img.shields.io/badge/Project-Beginner%20Friendly-brightgreen)](#)

A beginner-friendly, **command-line pizza ordering simulator** built with Python. Choose a pizza size, add pepperoni or extra cheese, and instantly see an itemized receipt with your total bill.

> **Note:** This is an educational application. It does not place real pizza orders, process payments, or arrange deliveries.

## ✨ Features

- Choose a **small, medium, or large** pizza.
- Customize your order with **pepperoni** and **extra cheese**.
- Get the correct topping price based on the selected pizza size.
- Enter lowercase or uppercase choices; extra spaces are ignored.
- Receive helpful messages for invalid choices and try again.
- View a clear **order receipt** and total price.
- Run automatic tests for the different pricing combinations.
- No third-party packages required.

## 💵 Price list

| Pizza size | Base price | Pepperoni add-on | Extra cheese |
|---|---:|---:|---:|
| Small (S) | $15 | +$2 | +$1 |
| Medium (M) | $20 | +$3 | +$1 |
| Large (L) | $25 | +$3 | +$1 |

All prices are illustrative and expressed in **US dollars (USD)**.

## 📁 Project structure

```text
ifali-pizza-delivery/
├── pizza_delivery.py       # Interactive ordering program
├── test_pizza_delivery.py  # Automated tests for pricing logic
├── .gitignore              # Excludes Python cache and local files
└── README.md               # Project documentation
```

## 🚀 Getting started

**Prerequisite:** Python 3 installed on your computer.

1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Run the app:

   ```bash
   python pizza_delivery.py
   ```

   On some systems, use `python3 pizza_delivery.py` or, on Windows, `py pizza_delivery.py`.

No installation or external dependencies are required.

## 🖥️ Example usage

```text
🍕 Welcome to Ifali's Pizza Delivery! 🍕

Pizza sizes:
  S - Small: $15
  M - Medium: $20
  L - Large: $25

Choose a size (S/M/L): s
Add pepperoni? (Y/N): y
Add extra cheese? (Y/N): y

---------- ORDER RECEIPT ----------
Pizza (Small):    $15
Pepperoni:        $2
Extra cheese:     $1
-----------------------------------
TOTAL:           $18
Thank you for choosing Ifali! 🍕
```

## 🧠 How it works

The program separates ordering and price calculation into small, reusable functions:

- **`get_valid_choice()`** requests input, removes extra spaces with `.strip()`, converts letters to uppercase with `.upper()`, and repeats until the answer is valid.
- **`calculate_total()`** starts with the pizza's base price and adds only the toppings selected by the customer.
- **`main()`** shows the menu, collects the order, and prints an itemized receipt.

Pizza prices are stored in dictionaries rather than repeated throughout the code. The `if __name__ == "__main__":` guard lets the app run normally while allowing its calculation function to be imported for testing.

### Python concepts practised

Functions · Dictionaries · Conditional statements · `while` loops · `for` loops · Input validation · Boolean values · String methods · F-strings · Basic unit testing

## ✅ Run the tests

From the project directory, run:

```bash
python -m unittest -v
```

The test suite checks **all 12 combinations** of three sizes and two optional toppings, plus an invalid-size case.

## 🔭 Ideas for future versions

- [ ] Let customers order more than one pizza at a time.
- [ ] Calculate delivery fees and applicable taxes.
- [ ] Add drink and side options.
- [ ] Save receipts or order history to a file.
- [ ] Build a graphical interface or web-based ordering experience.

## 🎯 Project goal

This project was developed to strengthen my understanding of Python fundamentals by applying conditional logic, functions, dictionaries, and user input validation to a realistic everyday example.

Suggestions and constructive feedback are welcome. ⭐ If you find the project useful, consider starring the repository!
