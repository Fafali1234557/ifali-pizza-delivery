"""Ifali's Pizza Delivery: a simple command-line pizza order calculator."""

PIZZA_PRICES = {"S": 15, "M": 20, "L": 25}
PIZZA_SIZES = {"S": "Small", "M": "Medium", "L": "Large"}
PEPPERONI_PRICES = {"S": 2, "M": 3, "L": 3}
EXTRA_CHEESE_PRICE = 1


def get_valid_choice(prompt, valid_choices):
    """Keep asking until the user enters one of the allowed choices."""
    while True:
        choice = input(prompt).strip().upper()
        if choice in valid_choices:
            return choice
        print(f"Invalid choice. Please enter {' or '.join(valid_choices)}.")


def calculate_total(size, add_pepperoni, add_cheese):
    """Return the total price for one pizza and its selected toppings."""
    if size not in PIZZA_PRICES:
        raise ValueError("Pizza size must be S, M, or L.")

    total = PIZZA_PRICES[size]
    if add_pepperoni:
        total += PEPPERONI_PRICES[size]
    if add_cheese:
        total += EXTRA_CHEESE_PRICE
    return total


def main():
    print("🍕 Welcome to Ifali's Pizza Delivery! 🍕")
    print("\nPizza sizes:")
    for size, price in PIZZA_PRICES.items():
        print(f"  {size} - {PIZZA_SIZES[size]}: ${price}")

    size = get_valid_choice("\nChoose a size (S/M/L): ", PIZZA_PRICES)
    add_pepperoni = get_valid_choice("Add pepperoni? (Y/N): ", ("Y", "N")) == "Y"
    add_cheese = get_valid_choice("Add extra cheese? (Y/N): ", ("Y", "N")) == "Y"

    pizza_price = PIZZA_PRICES[size]
    pepperoni_price = PEPPERONI_PRICES[size] if add_pepperoni else 0
    cheese_price = EXTRA_CHEESE_PRICE if add_cheese else 0
    total = calculate_total(size, add_pepperoni, add_cheese)

    print("\n---------- ORDER RECEIPT ----------")
    print(f"Pizza ({PIZZA_SIZES[size]}):    ${pizza_price}")
    print(f"Pepperoni:        ${pepperoni_price}")
    print(f"Extra cheese:     ${cheese_price}")
    print("-----------------------------------")
    print(f"TOTAL:           ${total}")
    print("Thank you for choosing Ifali! 🍕")


if __name__ == "__main__":
    main()
