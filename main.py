import sys

from collections import namedtuple
from datetime import date


FoodItem = namedtuple("FoodItem", ["name", "weight", "energy"])
Meal = namedtuple("Meal", ["name", "food_items"])
Day = namedtuple("Day", ["date", "meals"])
Section = namedtuple("Section", ["start", "end", "days", "extras"])

food_items = set([
    FoodItem("Belvita Biscuits", 50, 901),  # https://www.woolworths.com.au/shop/productdetails/715921/belvita-milk-cereal-breakfast-biscuits
    FoodItem("Babybel", 20, 1563 / 5.0),
    FoodItem("Back Country Beef Teriyaki", 175, 3130),
    FoodItem("Back Country Cooked Breakfast", 175, 3700),
    FoodItem("Back Country Roast Chicken", 175, 3180),
    FoodItem("Beef Jerky", 180, 1130 * 1.8),
    FoodItem("Dried Mushrooms", 40, 0),
    FoodItem("Home Coffee", 0, 0),
    FoodItem("Home Porridge", 0, 1000),
    FoodItem("Newcastle Dinner", 0, 3000),
    FoodItem("Nut Bar", 35, 750),
    FoodItem("Snickers", 50, 1030),
    FoodItem("Spicy Noodle Pack", 85, 1640),
    FoodItem("Whitaker's Peanut Slab", 50, 1120),
    FoodItem("Wholegrain Wrap", 45, 496),  # https://www.woolworths.com.au/shop/productdetails/634919/woolworths-wholegrain-wrap-8pk
    FoodItem("Sweet Chilli Flavoured Cashews", 200, 2280 * 2),  # https://www.woolworths.com.au/shop/productdetails/728223/woolworths-cashews-sweet-chilli-flavoured
    FoodItem("Scoop Peanut Butter", 23, 570),
    FoodItem("Tuna Pouch", 74, 382),
    FoodItem("Dried Cranberries", 170, 1370 * 1.7),  # https://www.woolworths.com.au/shop/productdetails/95093/ocean-spray-craisins-dried-cranberries
    FoodItem("Peanut M&Ms", 180, 2140 * 1.8),
])

sections = [
    Section("Sydney", "Somersby",
            [
                Day(date(2022, 2, 3), [
                    Meal("Breakfast", ["Home Coffee", "Home Porridge"]),
                    Meal("Lunch", ["Wholegrain Wrap", "Babybel", "Babybel"]),
                    Meal("Dinner", ["Spicy Noodle Pack", "Spicy Noodle Pack"]),
                ]),
                Day(date(2022, 2, 4), [
                    Meal("Breakfast", ["Whitaker's Peanut Slab"]),
                    Meal("Lunch", ["Wholegrain Wrap", "Tuna Pouch"]),
                    Meal("Dinner", ["Back Country Beef Teriyaki"]),
                ]),
                Day(date(2022, 2, 5), [
                    Meal("Breakfast", ["Nut Bar", "Nut Bar"]),
                    Meal("Lunch", ["Wholegrain Wrap", "Scoop Peanut Butter", "Scoop Peanut Butter"]),
                    Meal("Dinner", ["Spicy Noodle Pack", "Spicy Noodle Pack"]),
                ]),
                Day(date(2022, 2, 6), [
                    Meal("Breakfast", ["Back Country Cooked Breakfast"]),
                    Meal("Lunch", ["Wholegrain Wrap", "Babybel", "Babybel"]),
                    Meal("Dinner", ["Back Country Beef Teriyaki"]),
                ]),
                Day(date(2022, 2, 7), [
                    Meal("Breakfast", ["Nut Bar", "Nut Bar"]),
                    Meal("Lunch", ["Wholegrain Wrap", "Scoop Peanut Butter", "Scoop Peanut Butter"]),  # Hoping for a burger this day.
                    Meal("Dinner", ["Spicy Noodle Pack", "Spicy Noodle Pack"]),
                ]),
            ],
            [
                "Beef Jerky",
                "Dried Cranberries",
                "Dried Mushrooms",
                "Peanut M&Ms",
                "Snickers",
                "Snickers",
                "Snickers",
                "Snickers",
                "Sweet Chilli Flavoured Cashews",
            ]),
    Section("Somersby", "Newcastle", [
                Day(date(2022, 2, 8), [
                    Meal("Breakfast", []),
                    Meal("Lunch", ["Wholegrain Wrap", "Babybel", "Babybel"]),
                    Meal("Dinner", ["Spicy Noodle Pack", "Spicy Noodle Pack"]),
                ]),
                Day(date(2022, 2, 9), [
                    Meal("Breakfast", ["Whitaker's Peanut Slab"]),
                    Meal("Lunch", ["Wholegrain Wrap", "Tuna Pouch"]),
                    Meal("Dinner", ["Back Country Beef Teriyaki"]),
                ]),
                Day(date(2022, 2, 10), [
                    Meal("Breakfast", ["Nut Bar", "Nut Bar"]),
                    Meal("Lunch", ["Wholegrain Wrap", "Babybel", "Babybel"]),
                    Meal("Dinner", ["Spicy Noodle Pack", "Spicy Noodle Pack"]),
                ]),
                Day(date(2022, 2, 11), [
                    Meal("Breakfast", ["Back Country Cooked Breakfast"]),
                    Meal("Lunch", ["Wholegrain Wrap", "Scoop Peanut Butter", "Scoop Peanut Butter"]),
                    Meal("Dinner", ["Newcastle Dinner"]),
                ]),
        ], [
                "Beef Jerky",
                "Dried Cranberries",
                "Dried Peas",
                "Peanut M&Ms",
                "Snickers",
                "Snickers",
                "Snickers",
                "Snickers",
                "Sweet Chilli Flavoured Cashews",
        ])
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
    for section in sections:
        print(f"Section: {section.start} to {section.end}")
        weight_total = 0
        extras_energy = 0

        for extra in section.extras:
            weight_total += lookup(extra).weight
            extras_energy += lookup(extra).energy

        for day in section.days:
            energy_total = extras_energy / len(day.meals)
            for meal in day.meals:
                for food_item_name in meal.food_items:
                    food_item = lookup(food_item_name)
                    energy_total += food_item.energy
                    weight_total += food_item.weight
            print(f"{day.date.strftime('%a %-d %b')}: {int(energy_total)} KJ")

        print(f"Section Weight: {weight_total} g\n")

    sys.exit(ret)


if __name__ == "__main__":
    main()
