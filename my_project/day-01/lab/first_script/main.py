def print_fruits(fruit_list, fruit_to_remove):
    print(f"\nHere are the fruits except '{fruit_to_remove}':")
    for fruit in fruit_list:
        if fruit.lower() != fruit_to_remove.lower():
            print(fruit)

def main():
    print("Welcome to the Fruit Printer Program!")

    fruits = input("Enter a list of fruits separated by commas: ").split(',')

    fruits = [fruit.strip() for fruit in fruits]

    fruit_to_remove = input("What fruit should we remove? ")

    print_fruits(fruits, fruit_to_remove)

    print("\nThank you for using the Fruit Printer Program! Goodbye.")

if __name__ == "__main__":
    main()
