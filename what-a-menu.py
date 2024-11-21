class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - ${self.price:.2f}"


class Meal(MenuItem):
    def __init__(self, number, name, price, description, is_combo=True):
        super().__init__(name, price)
        self.number = number
        self.description = description
        self.is_combo = is_combo
        self.size = "medium"

    def upgrade_size(self, size):
        size_price_mapping = {"small": -0.50, "medium": 0.00, "large": 0.70}
        if size in size_price_mapping:
            self.price += size_price_mapping[size] - size_price_mapping[self.size]
            self.size = size

    def __str__(self):
        combo_text = "Combo" if self.is_combo else "Single"
        return f"#{self.number} {self.name} ({combo_text}) - {self.size.capitalize()} - ${self.price:.2f}\n    {self.description}"


class Burger(MenuItem):
    def __init__(self, name, price, patty_count=1, has_cheese=False):
        super().__init__(name, price)
        self.patty_count = patty_count
        self.has_cheese = has_cheese

    def add_patty(self):
        self.patty_count += 1
        self.price += 1.50

    def add_cheese(self):
        if not self.has_cheese:
            self.has_cheese = True
            self.price += 0.50

    def __str__(self):
        cheese_text = "with Cheese" if self.has_cheese else ""
        return f"{self.name} {cheese_text} - ${self.price:.2f} ({self.patty_count} Patties)"

class Side(MenuItem):
    def __init__(self, name, price, calories, portion_count=1):
        super().__init__(name, price)
        self.calories = calories
        self.portion_count = portion_count

    def add_portion(self):
        self.portion_count += 1
        self.price += 1.00  # Assume each additional portion costs $1.00

    def __str__(self):
        portion_text = f"{self.portion_count} Portion{'s' if self.portion_count > 1 else ''}"
        return f"{self.name} - ${self.price:.2f} ({self.calories} Cal per portion, {portion_text})"

class Dessert(MenuItem):
    def __init__(self, name, price, calories, serving_count=1):
        super().__init__(name, price)
        self.calories = calories
        self.serving_count = serving_count

    def add_serving(self):
        self.serving_count += 1
        self.price += 1.50  # Assume each additional serving costs $1.50

    def __str__(self):
        serving_text = f"{self.serving_count} Serving{'s' if self.serving_count > 1 else ''}"
        return f"{self.name} - ${self.price:.2f} ({self.calories} Cal per serving, {serving_text})"

class Salad(MenuItem):
    def __init__(self, name, price, calories, serving_count=1):
        super().__init__(name, price)
        self.calories = calories
        self.serving_count = serving_count

    def add_serving(self):
        self.serving_count += 1
        self.price += 2.00  # Assume each additional serving costs $2.00
        self.calories += 100  # Assume each serving adds 100 calories

    def __str__(self):
        serving_text = f"{self.serving_count} Serving{'s' if self.serving_count > 1 else ''}"
        return f"{self.name} - ${self.price:.2f} ({self.calories} Cal per serving, {serving_text})"

class Shake(MenuItem):
    def __init__(self, name, price, calories):
        super().__init__(name, price)
        self.calories = calories

    def __str__(self):
        return f"{self.name} - ${self.price:.2f} ({self.calories} Cal)"


class WhataburgerMenu:
    def __init__(self):
        self.meals = []
        self.burgers = []
        self.sides = []
        self.desserts = []
        self.salads = []
        self.shakes =[]
        self.initialize_menu()

    def initialize_menu(self):

            #meals
        self.meals.append(Meal(1, "Whataburger", 9.59, "Classic Whataburger with fries and drink"))
        self.meals.append(Meal(2, "Double Meat Whataburger", 10.79, "Two beef patties, fries, and drink"))
        self.meals.append(Meal(3, "Triple Meat Whataburger", 12.29, "Three beef patties, fries, and drink"))
        self.meals.append(Meal(4, "Jalapeño & Cheese Whataburger", 10.19, "Whataburger with jalapeños, cheese, fries, and drink"))
        self.meals.append(Meal(5, "Bacon & Cheese Whataburger", 10.89,        "Whataburger with bacon, cheese, fries, and drink"))
        self.meals.append(Meal(6, "Avocado Bacon Burger", 10.99, "Cheese and creamy pepper sause on Texas Toast"))
        self.meals.append(Meal(8, "Double Meat Whataburger Jr.", 7.99, "Double meat smaller burger, fries, and drink"))
        self.meals.append(Meal(7, "Whataburger Jr.", 6.99, "Smaller Whataburger with fries and drink"))
        self.meals.append(Meal(10, "Whatachick’n Sandwich", 9.59, "Crispy chicken sandwich, fries, and drink"))
        self.meals.append(Meal(11, "Grilled Chicken Sandwich", 10.49, "Grilled chicken sandwich, fries, and drink"))
        self.meals.append(Meal(12, "Spicy Chicken Sandwich", 9.79, "Grilled chicken sandwich, fries, and drink"))
        self.meals.append(Meal(13, "Whatachick’n Strips 3 piece", 8.99, "Three crispy chicken strips, fries, and drink"))


            #Alacart
        self.burgers.append(Burger("Whataburger", 5.99, patty_count=1))
        self.burgers.append(Burger("Double Meat Whataburger", 7.19, patty_count=2))
        self.burgers.append(Burger("Triple Meat Whataburger", 8.69, patty_count=3))
        self.burgers.append(Burger("Jalapeño & Cheese Whataburger", 7.29, patty_count=1,))
        self.burgers.append(Burger("Bacon & Cheese Whataburger", 7.29,patty_count=1,))
        self.burgers.append(Burger("Avocado Bacon Burger", 7.49, patty_count=1,))
        self.burgers.append(Burger("Double Meat Whataburger Jr.", 4.59, patty_count=2,))
        self.burgers.append(Burger("Whataburger Jr.", 3.69, patty_count=1,))
        self.burgers.append(Burger("Whatachick'n Sandwich", 5.99,))
        self.burgers.append(Burger("Grilled Chicken Sandwich", 6.89,))
        self.burgers.append(Burger("Spicy Chicken Sandwich",6.29 ,))
        self.burgers.append(Burger("Whatachick'n Strips 3 Piece",5.39,))

        self.sides.append(Side("French Fries", 2.59, 270))
        self.sides.append(Side("Onion Rings", 3.79, 300))
        self.sides.append(Side("Apple Slices", 1.69, 30))

        self.desserts.append(Dessert("Hot Apple Pie", 1.79, 270))
        self.desserts.append(Dessert("Chocolate Chip Cookie", 1.89, 330))
        self.desserts.append(Dessert("Cinnamon Roll", 2.99, 580))

        self.salads.append(Salad("Apple & Cranberry Chicken Salad", 8.99, 390))
        self.salads.append(Salad("Cobb Salad", 7.59, 300))

        self.shakes.append(Shake("Chocolate Shake", 3.99, 500))
        self.shakes.append(Shake("Vanilla Shake", 3.99, 450))
        self.shakes.append(Shake("Strawberry Shake", 3.99, 480))

    def display_menu(self):
            print("Whataburger Combo Meals:")
            for meal in self.meals:
             print(meal)

            print("-----------------------------------------------------")
            print("Alacarts")
            for meal in self.burgers:
                print(meal)

            print("\nSides:")
            for side in self.sides:
                print(side)

            print("\nDesserts:")
            for dessert in self.desserts:
                print(dessert)

            print("\nSalads:")
            for salad in self.salads:
                print(salad)

            print("\nShakes:")
            for shake in self.shakes:
                print(shake)

class Order:
    def __init__(self):
        self.items = []
        self.total = 0.0

    def add_item(self, item):
        """Add an item to the order."""
        self.items.append(item)
        self.total += item.price
        print(f"{item.name} added to your order!")

    def remove_item(self, item_name):
        """Remove an item from the order by name."""
        for item in self.items:
            if item.name.lower() == item_name.lower():
                self.items.remove(item)
                self.total -= item.price
                print(f"{item.name} removed from your order!")
                return
        print(f"Item '{item_name}' not found in your order.")

    def view_order(self):
        """View the current order."""
        if not self.items:
            print("Your order is empty!")
        else:
            print("\n===== Current Order =====")
            for item in self.items:
                print(item)
            print(f"Total: ${self.total:.2f}")
            print("=========================")

    def clear_order(self):
        """Clear the entire order."""
        self.items = []
        self.total = 0.0
        print("Your order has been cleared!")

    def save_order(self, filename="order.txt"):
        """Save the current order to a file."""
        try:
            with open(filename, "w") as file:
                for item in self.items:
                    file.write(f"{item.name},{item.price}\n")
                file.write(f"Total,{self.total}\n")
            print(f"Order saved to {filename}.")
        except Exception as e:
            print(f"Error saving order: {e}")

    def load_order(self, filename="order.txt"):
        """Load a previously saved order from a file."""
        try:
            with open(filename, "r") as file:
                self.clear_order()
                for line in file:
                    name, price = line.strip().split(",")
                    if name == "Total":
                        self.total = float(price)
                    else:
                        self.items.append(MenuItem(name, float(price)))
            print(f"Order loaded from {filename}.")
        except Exception as e:
            print(f"Error loading order: {e}")

    def apply_discount(self, discount_percentage):
        """Apply a percentage discount to the total order."""
        discount = self.total * (discount_percentage / 100)
        self.total -= discount
        print(f"A discount of {discount_percentage}% has been applied. You saved ${discount:.2f}!")

menu = WhataburgerMenu()
menu.display_menu()


def display_main_menu():
    print("\n===== Whataburger Ordering System =====")
    print("1. View Full Menu")
    print("2. Add an Item to Your Order")
    print("3. Remove an Item from Your Order")
    print("4. Replace an Item in Your Order")
    print("5. Customize an Item in Your Order")
    print("6. View Your Current Order")
    print("7. Clear Your Order")
    print("8. Save Your Order")
    print("9. Load a Previous Order")
    print("10. Apply a Discount")
    print("11. Exit")
    print("========================================")


display_main_menu()







