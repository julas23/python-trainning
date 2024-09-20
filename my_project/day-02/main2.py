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
    # Create an instance of FruitBasket
    basket = FruitBasket()

    # Ask the user how many fruits they want to add
    num_fruits = int(input("How many fruits do you want to add to the basket? "))

    # Loop to add multiple fruits based on user input
    for _ in range(num_fruits):
        name = input("Enter the fruit name: ")
        color = input("Enter the fruit color: ")
        fruit = Fruit(name, color)
        basket.add_fruit(fruit)

    # Print the basket content
    basket.print_basket()

if __name__ == "__main__":
    main()
