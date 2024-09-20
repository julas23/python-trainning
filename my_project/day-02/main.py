class Fruit:
    def __init__(self, name, color):
        self.name = name
        self.color = color

class FruitBasket:
    def __init__(self):
        self.basket = []

    def add_fruit(self, fruit):
        self.basket.append(fruit)
        print(f"{fruit.name} added to the basket.")

    def remove_fruit(self, fruit):
        if fruit in self.basket:
            self.basket.remove(fruit)
            print(f"{fruit.name} removed from the basket.")
        else:
            print(f"{fruit.name} is not in the basket.")

    def print_basket(self):
        if self.basket:
            print("Fruits in the basket:")
            for fruit in self.basket:
                print(f"- {fruit.name} ({fruit.color})")
        else:
            print("The basket is empty.")

def main():
    # Create an instance of Fruit
    apple = Fruit("Apple", "Red")

    # Create an instance of FruitBasket
    basket = FruitBasket()

    # Add the fruit to the basket
    basket.add_fruit(apple)

    # Remove the fruit from the basket
    basket.remove_fruit(apple)

    # Print the basket content
    basket.print_basket()

if __name__ == "__main__":
    main()