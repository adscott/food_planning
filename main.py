import sys

from collections import namedtuple
from datetime import date

from tabulate import tabulate

from categories import category, ureg

kcal = ureg.calorie * 1000
kj = ureg.kilojoule
g = ureg.gram


class FoodItem(object):
    def __init__(self, name, recorded_weight, energy, packaged):
        self.name = name
        self.energy = energy
        self.weight = recorded_weight if packaged else recorded_weight * 1.1


Meal = namedtuple("Meal", ["name", "food_items"])
Day = namedtuple("Day", ["date", "meals"])
Section = namedtuple("Section", ["start", "end", "days", "extras"])

food_items = set([
    FoodItem("Campers Pantry Cream Rice Pudding with Apple", 68 * g, 1832 * kj, True),
    FoodItem("Radix Breakfast Mixed Berry", 175.1 * g, 806 * kcal, True),
    FoodItem("Radix Breakfast Apple & Cinnamon", 178.9 * g, 800 * kcal, True),
    FoodItem("Radix Meal Barbecue Beef", 156.2 * g, 801 * kcal, True),
    FoodItem("Radix Meal Basil Pesto", 157.8 * g, 805 * kcal, True),
    FoodItem("Radix Meal Indian Curry", 164.6 * g, 799 * kcal, True),
    FoodItem("Radix Meal Mexican Chilli", 155.7 * g, 799 * kcal, True),
    FoodItem("Radix Meal Mint & Rosemary", 153.6 * g, 809 * kcal, True),

    FoodItem("Byron Bay Macadamia Muesli with Powdered Milk", (100 + 35) * g, (2560 + 757) * kj, False),

    FoodItem("Whitaker's Almond Slab", 45 * g, 1103 * kj, False),
    FoodItem("Whitaker's Coconut Slab", 50 * g, 1215 * kj, False),

    FoodItem("Coles Choc Coated Nut Bar", 35 * g, 812 * kj, False),
    FoodItem("Sam's Pantry Honey Salted Macadamia Nut Bar", 34 * g, 764 * kj, False),
    FoodItem("Sam's Pantry Salted Caramel Nut Bar", 34 * g, 762 * kj, False),

    FoodItem("Tailwind Recovery Chocolate", 67 * g, 245 * kcal, True),
    FoodItem("Tailwind Recovery Salted Caramel", 64.3 * g, 240 * kcal, True),
    FoodItem("Tailwind Recovery Vanilla", 65.3 * g, 240 * kcal, True),

    FoodItem("Instant Coffee", 50 * g, 0 * kj, True),
    FoodItem("Hot Chocolate", (35 + 18.5 + 25 + 15) * g, (757 + 331 + 375 + 564) * kj, False),  # 250ml instant milk, 2 tbsp cocao powder, 2 tbsp refined sugar

    FoodItem("Peanut M&Ms", 180 * g, 2140 * 1.8 * kj, False),
    FoodItem("Ritz Crackers", 106 * g, 5 * 429 * kj, True),
    FoodItem("Butterfingers Pure Butter Macadamia Shortbread", 189 * g, 659 * 6 * kj, True),
])

sections = [
    Section("Somersby", "Newcastle", [
                Day(date(2022, 6, 14), [
                    Meal("Hiking", [
                        "Tailwind Recovery Salted Caramel",
                    ]),
                    Meal("Dinner", ["Radix Meal Mint & Rosemary", "Whitaker's Coconut Slab"]),
                ]),
                Day(date(2022, 6, 15), [
                    Meal("Breakfast", ["Radix Breakfast Mixed Berry"]),
                    Meal("Hiking", [
                        "Coles Choc Coated Nut Bar",
                        "Coles Choc Coated Nut Bar",
                        "Coles Choc Coated Nut Bar",
                        "Coles Choc Coated Nut Bar",
                        "Sam's Pantry Honey Salted Macadamia Nut Bar",
                        "Tailwind Recovery Chocolate",
                    ]),
                    Meal("Dinner", ["Radix Meal Mexican Chilli", "Whitaker's Almond Slab"]),
                ]),
                Day(date(2022, 6, 16), [
                    Meal("Breakfast", ["Radix Breakfast Apple & Cinnamon"]),
                    Meal("Hiking", [
                        "Coles Choc Coated Nut Bar",
                        "Coles Choc Coated Nut Bar",
                        "Sam's Pantry Salted Caramel Nut Bar",
                        "Tailwind Recovery Vanilla",
                    ]),
                    Meal("Dinner", ["Radix Meal Basil Pesto", "Whitaker's Coconut Slab"]),
                ]),
                Day(date(2022, 6, 17), [
                    Meal("Breakfast", ["Radix Breakfast Mixed Berry"]),
                    Meal("Hiking", [
                        "Coles Choc Coated Nut Bar",
                        "Coles Choc Coated Nut Bar",
                        "Coles Choc Coated Nut Bar",
                        "Coles Choc Coated Nut Bar",
                        "Sam's Pantry Honey Salted Macadamia Nut Bar",
                        "Tailwind Recovery Chocolate",
                    ]),
                    Meal("Dinner", ["Radix Meal Barbecue Beef", "Campers Pantry Cream Rice Pudding with Apple"]),
                ]),
                Day(date(2022, 6, 18), [
                    Meal("Breakfast", ["Byron Bay Macadamia Muesli with Powdered Milk"]),
                    Meal("Hiking", [
                        "Coles Choc Coated Nut Bar",
                        "Coles Choc Coated Nut Bar",
                        "Coles Choc Coated Nut Bar",
                        "Coles Choc Coated Nut Bar",
                        "Sam's Pantry Salted Caramel Nut Bar",
                        "Tailwind Recovery Salted Caramel",
                    ]),
                    Meal("Dinner", ["Whitaker's Coconut Slab"]),
                ]),
                Day(date(2022, 6, 19), [
                    Meal("Breakfast", ["Byron Bay Macadamia Muesli with Powdered Milk"]),
                    Meal("Hiking", [
                        "Coles Choc Coated Nut Bar",
                        "Coles Choc Coated Nut Bar",
                        "Sam's Pantry Honey Salted Macadamia Nut Bar",
                        "Tailwind Recovery Chocolate",
                    ]),
                ]),
        ], [
            "Instant Coffee",
            "Peanut M&Ms",
            "Hot Chocolate",
            "Hot Chocolate",
            "Butterfingers Pure Butter Macadamia Shortbread",
            "Ritz Crackers",
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
        return FoodItem("", 0, 0, True)


def main():
    print(tabulate(sorted(([f.name, category(f.energy, f.weight), "{:.2f}".format(f.energy.to(kj) / f.weight)] for f in food_items), key=lambda x: x[2])))
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
            rows.append([day.date.strftime('%a %-d %b'), "{:.0f}".format(energy_day.to(kj)), "{:.0f}".format(weight_day), category(energy_day, weight_day)])

        rows.append([])
        rows.append(["Section", "{:.0f}".format(energy_total.to(kj)), "{:.0f}".format(weight_total), category(energy_total, weight_total)])
        print(tabulate(rows, stralign="right"))
        print("\n")

    sys.exit(ret)


if __name__ == "__main__":
    main()
