import sys

from collections import namedtuple
from datetime import date

from categories import ureg


FoodItem = namedtuple("FoodItem", ["name", "weight", "energy"])
Meal = namedtuple("Meal", ["name", "food_items"])
Day = namedtuple("Day", ["date", "meals"])
Section = namedtuple("Section", ["start", "end", "days", "extras"])

food_items = set([
    FoodItem("Babybel", 20 * ureg.gram, 1563 / 5.0 * ureg.kilojoule),
    FoodItem("Back Country Beef Teriyaki", 175 * ureg.gram, 3130 * ureg.kilojoule),
    FoodItem("Back Country Beef and Pasta Hotpot", 175 * ureg.gram, 3190 * ureg.kilojoule),
    FoodItem("Back Country Cooked Breakfast", 175 * ureg.gram, 3700 * ureg.kilojoule),
    FoodItem("Back Country Roast Chicken", 175 * ureg.gram, 3180 * ureg.kilojoule),
    FoodItem("Beef Jerky", 180 * ureg.gram, 1130 * 1.8 * ureg.kilojoule),
    FoodItem("Belvita Biscuits", 50 * ureg.gram, 901 * ureg.kilojoule),  # https://www.woolworths.com.au/shop/productdetails/715921/belvita-milk-cereal-breakfast-biscuits
    FoodItem("Chilli & Lime Soya Crisps", 400 * ureg.gram, 2070 * 4 * ureg.kilojoule),
    FoodItem("Dried Cranberries", 170 * ureg.gram, 1370 * 1.7 * ureg.kilojoule),  # https://www.woolworths.com.au/shop/productdetails/95093/ocean-spray-craisins-dried-cranberries
    FoodItem("Dried Mushrooms", 50 * ureg.gram, 700 * ureg.kilojoule),
    FoodItem("Dried Peas", 100 * ureg.gram, 337 * ureg.kilojoule),
    FoodItem("Home Coffee", 0 * ureg.gram, 0 * ureg.kilojoule),
    FoodItem("Home Porridge", 0 * ureg.gram, 1000 * ureg.kilojoule),
    FoodItem("Instant Coffee", 0 * ureg.gram, 70 * ureg.kilojoule),
    FoodItem("Maple Flavoured Cashews", 200 * ureg.gram, 2310 * 2 * ureg.kilojoule),
    FoodItem("Newcastle Dinner", 0 * ureg.gram, 3000 * ureg.kilojoule),
    FoodItem("Nut Bar", 35 * ureg.gram, 750 * ureg.kilojoule),
    FoodItem("Original Soya Crisps", 400 * ureg.gram, 2120 * 4 * ureg.kilojoule),
    FoodItem("Peanut M&Ms", 180 * ureg.gram, 2140 * 1.8 * ureg.kilojoule),
    FoodItem("Scoop Peanut Butter", 0 * ureg.gram, 570 * ureg.kilojoule), FoodItem("Jar Peanut Butter", 400 * ureg.gram, 0 * ureg.kilojoule),  # Split weight and energy to make counting easier
    FoodItem("Snickers", 50 * ureg.gram, 1030 * ureg.kilojoule),
    FoodItem("Spicy Broad Beans", 100 * ureg.gram, 1960 * ureg.kilojoule),
    FoodItem("Spicy Noodle Pack", 85 * ureg.gram, 1640 * ureg.kilojoule),
    FoodItem("Sweet Chilli Flavoured Cashews", 200 * ureg.gram, 2280 * 2 * ureg.kilojoule),  # https://www.woolworths.com.au/shop/productdetails/728223/woolworths-cashews-sweet-chilli-flavoured
    FoodItem("Tuna Pouch", 160 * ureg.gram, 890 * ureg.kilojoule),
    FoodItem("Whitaker's Almond Slab", 45 * ureg.gram, 1103 * ureg.kilojoule),
    FoodItem("Whitaker's Coconut Slab", 50 * ureg.gram, 1215 * ureg.kilojoule),
    FoodItem("Wholegrain Wrap", 45 * ureg.gram, 496 * ureg.kilojoule),  # https://www.woolworths.com.au/shop/productdetails/634919/woolworths-wholegrain-wrap-8pk
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
            print(f"{day.date.strftime('%a %-d %b')}: {energy_total}")

        print(f"Section Weight: {weight_total}\n")

    sys.exit(ret)


if __name__ == "__main__":
    main()
