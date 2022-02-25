import sys

from collections import namedtuple
from datetime import date
from operator import attrgetter

from tabulate import tabulate

from categories import category, ureg

kj = ureg.kilojoule
g = ureg.gram

FoodItem = namedtuple("FoodItem", ["name", "weight", "energy"])
Meal = namedtuple("Meal", ["name", "food_items"])
Day = namedtuple("Day", ["date", "meals"])
Section = namedtuple("Section", ["start", "end", "days", "extras"])

food_items = set([
    FoodItem("Babybel", 20 * g, 1563 / 5.0 * kj),
    FoodItem("Back Country Beef Teriyaki", 175 * g, 3130 * kj),
    FoodItem("Back Country Beef and Pasta Hotpot", 175 * g, 3190 * kj),
    FoodItem("Back Country Cooked Breakfast", 175 * g, 3700 * kj),
    FoodItem("Back Country Roast Chicken", 175 * g, 3180 * kj),
    FoodItem("Beef Jerky", 180 * g, 1130 * 1.8 * kj),
    FoodItem("Belvita Biscuits", 50 * g, 901 * kj),  # https://www.woolworths.com.au/shop/productdetails/715921/belvita-milk-cereal-breakfast-biscuits
    FoodItem("Chilli & Lime Soya Crisps", 400 * g, 2070 * 4 * kj),
    FoodItem("Dried Cranberries", 170 * g, 1370 * 1.7 * kj),  # https://www.woolworths.com.au/shop/productdetails/95093/ocean-spray-craisins-dried-cranberries
    FoodItem("Dried Mushrooms", 50 * g, 700 * kj),
    FoodItem("Dried Peas", 100 * g, 337 * kj),
    FoodItem("Home Coffee", 0 * g, 0 * kj),
    FoodItem("Home Porridge", 0 * g, 1000 * kj),
    FoodItem("Instant Coffee", 0 * g, 70 * kj),
    FoodItem("Maple Flavoured Cashews", 200 * g, 2310 * 2 * kj),
    FoodItem("Newcastle Dinner", 0 * g, 3000 * kj),
    FoodItem("Nut Bar", 35 * g, 750 * kj),
    FoodItem("Original Soya Crisps", 400 * g, 2120 * 4 * kj),
    FoodItem("Peanut M&Ms", 180 * g, 2140 * 1.8 * kj),
    FoodItem("Scoop Peanut Butter", 0 * g, 570 * kj), FoodItem("Jar Peanut Butter", 400 * g, 0 * kj),  # Split weight and energy to make counting easier
    FoodItem("Snickers", 50 * g, 1030 * kj),
    FoodItem("Spicy Broad Beans", 100 * g, 1960 * kj),
    FoodItem("Spicy Noodle Pack", 85 * g, 1640 * kj),
    FoodItem("Sweet Chilli Flavoured Cashews", 200 * g, 2280 * 2 * kj),  # https://www.woolworths.com.au/shop/productdetails/728223/woolworths-cashews-sweet-chilli-flavoured
    FoodItem("Tuna Pouch", 160 * g, 890 * kj),
    FoodItem("Whitaker's Almond Slab", 45 * g, 1103 * kj),
    FoodItem("Whitaker's Coconut Slab", 50 * g, 1215 * kj),
    FoodItem("Wholegrain Wrap", 45 * g, 496 * kj),  # https://www.woolworths.com.au/shop/productdetails/634919/woolworths-wholegrain-wrap-8pk
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
    print(tabulate([[f.name, category(f.energy, f.weight)] for f in sorted(food_items, key=attrgetter('name'))]))
    print("\n")

    for section in sections:
        rows = []
        print(f"Section: {section.start} to {section.end}")
        weight_total = 0
        energy_total = 0
        extras_weight = 0
        extras_energy = 0

        for extra in section.extras:
            extras_weight += lookup(extra).weight
            extras_energy += lookup(extra).energy

        for day in section.days:
            energy_day = extras_energy / len(section.days)
            weight_day = extras_weight / len(section.days)
            for meal in day.meals:
                for food_item_name in meal.food_items:
                    food_item = lookup(food_item_name)
                    energy_day += food_item.energy
                    weight_day += food_item.weight
            energy_total += energy_day
            weight_total += weight_day
            rows.append([day.date.strftime('%a %-d %b'), energy_day, weight_day, category(energy_day, weight_day)])

        rows.append(["Section", energy_total, weight_total, category(energy_total, weight_total)])
        print(tabulate(rows))
        print("\n")

    sys.exit(ret)


if __name__ == "__main__":
    main()
