import sys

from collections import namedtuple


FoodItem = namedtuple("FoodItem", ["name", "weight", "energy"])

food_items = set([
    FoodItem("Home Coffee", 0, 0),
    FoodItem("Home Porridge", 0, 500),
    FoodItem("Whitaker's Peanut Slab", 68, 1000),
    FoodItem("Beef Jerky", 68, 1000),
    FoodItem("Spicy Noodle Pack", 75, 1000),
    FoodItem("Backcountry Meal Roast Chicken Dinner", 175, 3200),
])

Meal = namedtuple("Meal", ["name", "food_items"])

meals = {
    1: [
        Meal("Breakfast", ["Home Coffee", "Home Porridge"]),
        Meal("Morning Snacks", []),
        Meal("Lunch", ["Wrap", "Babybel", "Babybel"]),
        Meal("Afternoon Snacks", []),
        Meal("Dinner", ["Spicy Noodle Pack", "Spicy Noodle Pack"]),
    ],
    2: [
        Meal("Breakfast", ["Whitaker's Peanut Slab"]),
        Meal("Morning Snacks", []),
        Meal("Lunch", []),
        Meal("Afternoon Snacks", []),
        Meal("Dinner", ["Backcountry Meal Roast Chicken Dinner"]),
    ],
    3: [
        Meal("Breakfast", ["Nut Bar", "Nut Bar"]),
        Meal("Morning Snacks", []),
        Meal("Lunch", []),
        Meal("Afternoon Snacks", []),
        Meal("Dinner", ["Spicy Noodle Pack", "Spicy Noodle Pack"]),
    ],
}

extras = [
    "Beef Jerky",
    "Dried Mushrooms",
]


ret = 0


def lookup(food_item_name):
    try:
        return next(food_item for food_item in food_items if food_item_name == food_item.name)
    except Exception:
        global ret
        ret = -1
        print(f"Can't find {food_item_name}")
        return FoodItem("", 0, 0)


def main():
    weight_total = 0
    for day in sorted(meals.keys()):
        energy_total = 0
        for meal in meals[day]:
            for food_item_name in meal.food_items:
                food_item = lookup(food_item_name)
                energy_total += food_item.energy
                weight_total += food_item.weight
        print(f"Day {day}: {energy_total} KJ")

    for extra in extras:
        weight_total += lookup(extra).weight

    print(f"Total Weight: {weight_total} gm")

    sys.exit(ret)


if __name__ == "__main__":
    main()
