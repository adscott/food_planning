import sys

from collections import namedtuple
from datetime import date


FoodItem = namedtuple("FoodItem", ["name", "weight", "energy"])
Meal = namedtuple("Meal", ["name", "food_items"])
Day = namedtuple("Day", ["date", "meals"])
Section = namedtuple("Section", ["start", "end", "days", "extras"])

food_items = set([
    FoodItem("Babybel", 20, 1563 / 5.0),
    FoodItem("Back Country Beef Teriyaki", 175, 3130),
    FoodItem("Back Country Beef and Pasta Hotpot", 175, 3190),
    FoodItem("Back Country Cooked Breakfast", 175, 3700),
    FoodItem("Back Country Roast Chicken", 175, 3180),
    FoodItem("Beef Jerky", 180, 1130 * 1.8),
    FoodItem("Belvita Biscuits", 50, 901),  # https://www.woolworths.com.au/shop/productdetails/715921/belvita-milk-cereal-breakfast-biscuits
    FoodItem("Chilli & Lime Soya Crisps", 400, 2070 * 4),
    FoodItem("Dried Cranberries", 170, 1370 * 1.7),  # https://www.woolworths.com.au/shop/productdetails/95093/ocean-spray-craisins-dried-cranberries
    FoodItem("Dried Mushrooms", 50, 700),
    FoodItem("Dried Peas", 100, 337),
    FoodItem("Home Coffee", 0, 0),
    FoodItem("Home Porridge", 0, 1000),
    FoodItem("Instant Coffee", 0, 70),
    FoodItem("Maple Flavoured Cashews", 200, 2310 * 2),
    FoodItem("Newcastle Dinner", 0, 3000),
    FoodItem("Nut Bar", 35, 750),
    FoodItem("Original Soya Crisps", 400, 2120 * 4),
    FoodItem("Peanut M&Ms", 180, 2140 * 1.8),
    FoodItem("Scoop Peanut Butter", 0, 570), FoodItem("Jar Peanut Butter", 400, 0), #  Split weight and energy to make counting easier
    FoodItem("Snickers", 50, 1030),
    FoodItem("Spicy Broad Beans", 100, 1960),
    FoodItem("Spicy Noodle Pack", 85, 1640),
    FoodItem("Sweet Chilli Flavoured Cashews", 200, 2280 * 2),  # https://www.woolworths.com.au/shop/productdetails/728223/woolworths-cashews-sweet-chilli-flavoured
    FoodItem("Tuna Pouch", 160, 890),
    FoodItem("Whitaker's Almond Slab", 45, 1103),
    FoodItem("Whitaker's Coconut Slab", 50, 1215),
    FoodItem("Wholegrain Wrap", 45, 496),  # https://www.woolworths.com.au/shop/productdetails/634919/woolworths-wholegrain-wrap-8pk
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
                    Meal("Breakfast", ["Whitaker's Almond Slab"]),
                    Meal("Lunch", ["Wholegrain Wrap", "Tuna Pouch"]),
                    Meal("Dinner", ["Back Country Beef Teriyaki"]),
                ]),
                Day(date(2022, 2, 5), [
                    Meal("Breakfast", ["Nut Bar", "Nut Bar"]),
                    Meal("Lunch", ["Wholegrain Wrap", "Babybel", "Babybel"]),
                    Meal("Dinner", ["Spicy Noodle Pack", "Spicy Noodle Pack"]),
                ]),
                Day(date(2022, 2, 6), [
                    Meal("Breakfast", ["Back Country Cooked Breakfast"]),
                    Meal("Lunch", ["Wholegrain Wrap", "Scoop Peanut Butter", "Scoop Peanut Butter"]),
                    Meal("Dinner", ["Back Country Beef and Pasta Hotpot"]),
                ]),
                Day(date(2022, 2, 7), [
                    Meal("Breakfast", ["Nut Bar", "Nut Bar"]),
                    Meal("Lunch", ["Wholegrain Wrap", "Scoop Peanut Butter", "Scoop Peanut Butter"]),  # Hoping for a burger this day.
                    Meal("Dinner", ["Spicy Noodle Pack", "Spicy Noodle Pack"]),
                ]),
            ],
            [
                "Beef Jerky",
                "Belvita Biscuits",
                "Belvita Biscuits",
                "Chilli & Lime Soya Crisps",
                "Dried Cranberries",
                "Dried Mushrooms",
                "Instant Coffee",
                "Jar Peanut Butter",
                "Maple Flavoured Cashews",
                "Peanut M&Ms",
                "Snickers",
                "Snickers",
                "Snickers",
                "Snickers",
                "Spicy Broad Beans",
            ]),
    Section("Somersby", "Newcastle", [
                Day(date(2022, 2, 8), [
                    Meal("Breakfast", ["Back Country Cooked Breakfast"]),
                    Meal("Lunch", ["Wholegrain Wrap", "Babybel", "Babybel"]),
                    Meal("Dinner", ["Spicy Noodle Pack", "Spicy Noodle Pack"]),
                ]),
                Day(date(2022, 2, 9), [
                    Meal("Breakfast", ["Whitaker's Coconut Slab"]),
                    Meal("Lunch", ["Wholegrain Wrap", "Tuna Pouch"]),
                    Meal("Dinner", ["Back Country Roast Chicken"]),
                ]),
                Day(date(2022, 2, 10), [
                    Meal("Breakfast", ["Nut Bar", "Nut Bar"]),
                    Meal("Lunch", ["Wholegrain Wrap", "Babybel", "Babybel"]),
                    Meal("Dinner", ["Spicy Noodle Pack", "Spicy Noodle Pack"]),
                ]),
                Day(date(2022, 2, 11), [
                    Meal("Breakfast", ["Whitaker's Almond Slab"]),
                    Meal("Lunch", ["Wholegrain Wrap", "Scoop Peanut Butter", "Scoop Peanut Butter"]),
                    Meal("Dinner", ["Newcastle Dinner"]),
                ]),
        ], [
                "Beef Jerky",
                "Belvita Biscuits",
                "Belvita Biscuits",
                "Dried Cranberries",
                "Dried Peas",
                "Instant Coffee",
                "Jar Peanut Butter",
                "Original Soya Crisps",
                "Peanut M&Ms",
                "Snickers",
                "Snickers",
                "Snickers",
                "Snickers",
                "Spicy Broad Beans",
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
            energy_total = extras_energy / len(section.days)
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
