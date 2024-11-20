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


class WhataburgerMenu:
    def __init__(self):
        self.meals = []
        self.burgers = []
        self.initialize_menu()

    def initialize_menu(self):

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

    def display_menu(self):
        print("Whataburger Combo Meals:")
        for meal in self.meals:
            print(meal)
        print("\nSingle Burgers:")
        for burger in self.burgers:
            print(burger)



menu = WhataburgerMenu()
menu.display_menu()







