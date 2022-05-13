import sys

from collections import namedtuple
from datetime import date
from operator import attrgetter

from tabulate import tabulate

from categories import category, ureg

kcal = ureg.calorie * 1000
kj = ureg.kilojoule
g = ureg.gram

FoodItem = namedtuple("FoodItem", ["name", "weight", "energy"])
Meal = namedtuple("Meal", ["name", "food_items"])
Day = namedtuple("Day", ["date", "meals"])
Section = namedtuple("Section", ["start", "end", "days", "extras"])

food_items = set([
    FoodItem("Campers Pantry Cream Rice Pudding with Apple", 68 * g, 1832 * kj),
    FoodItem("Peanut M&Ms", 180 * g, 2140 * 1.8 * kj),
    FoodItem("Radix Breakfast Mixed Berry", 175.1 * g, 806 * kcal),
    FoodItem("Radix Breakfast Apple & Cinnamon", 178.9 * g, 800 * kcal),
    FoodItem("Radix Meal Barbecue Beef", 156.2 * g, 801 * kcal),
    FoodItem("Radix Meal Basil Pesto", 157.8 * g, 805 * kcal),
    FoodItem("Radix Meal Indian Curry", 164.6 * g, 799 * kcal),
    FoodItem("Radix Meal Mexican Chilli", 155.7 * g, 799 * kcal),
    FoodItem("Radix Meal Mint & Rosemary", 153.6 * g, 809 * kcal),
    FoodItem("Whitaker's Almond Slab", 45 * g, 1103 * kj),
    FoodItem("Whitaker's Coconut Slab", 50 * g, 1215 * kj),
])

sections = [
    Section("Somersby", "Newcastle", [
                Day(date(2022, 6, 14), [
                    Meal("Dinner", ["Radix Meal Indian Curry", "Whitaker's Coconut Slab"]),
                ]),
                Day(date(2022, 6, 15), [
                    Meal("Breakfast", ["Radix Breakfast Mixed Berry"]),
                    Meal("Hiking", []),
                    Meal("Dinner", ["Radix Meal Mexican Chilli", "Whitaker's Almond Slab"]),
                ]),
                Day(date(2022, 6, 16), [
                    Meal("Breakfast", ["Radix Breakfast Apple & Cinnamon"]),
                    Meal("Hiking", []),
                    Meal("Dinner", ["Radix Meal Basil Pesto", "Whitaker's Coconut Slab"]),
                ]),
                Day(date(2022, 6, 17), [
                    Meal("Breakfast", ["Radix Breakfast Mixed Berry"]),
                    Meal("Hiking", []),
                    Meal("Dinner", ["Radix Meal Barbecue Beef", "Campers Pantry Cream Rice Pudding with Apple"]),
                ]),
                Day(date(2022, 6, 18), [
                    Meal("Breakfast", []),
                    Meal("Hiking", []),
                    Meal("Dinner", ["Radix Meal Mint & Rosemary", "Whitaker's Coconut Slab"]),
                ]),
                Day(date(2022, 6, 19), [
                    Meal("Breakfast", []),
                    Meal("Hiking", []),
                ]),
        ], [
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
        weight_total = 0 * g
        energy_total = 0 * kj
        extras_weight = 0 * g
        extras_energy = 0 * kj

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
            rows.append([day.date.strftime('%a %-d %b'), energy_day.to(kj), weight_day, category(energy_day, weight_day)])

        rows.append(["Section", energy_total.to(kj), weight_total, category(energy_total, weight_total)])
        print(tabulate(rows))
        print("\n")

    sys.exit(ret)


if __name__ == "__main__":
    main()
