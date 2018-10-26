#!/usr/bin python3

def series_01():
    fruits = ["Apples", "Pears", "Oranges", "Peaches"]
    print(fruits)
    new_fruits = input("Enter a new fruits: ")
    fruits.append(new_fruits)
    print(fruits)
    index = int(input(f"Give a number between 1 and {len(fruits)}: "))
    print("You chose: " + (fruits[index - 1] if index > 0 and index <= len(fruits) else "Error!"))

    print()
    fruits = ["Grapes"] + fruits
    print(fruits)

    fruits.insert(0, "Plums")
    print(fruits)

    print()
    print("Fruits that tart with P:")
    for fruit in fruits:
        if fruit[:1].lower() == "p":
            print(fruit)

if __name__ == '__main__':
    series_01()