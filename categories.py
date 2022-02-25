from collections import namedtuple
from pint import UnitRegistry
from tabulate import tabulate

ureg = UnitRegistry()

Category = namedtuple("Category", ["name", "lower"])

_categories = [
    Category("heavy", (0 * 1000 * ureg.calorie) / (1 * ureg.ounce)),
    Category("moderate", (110 * 1000 * ureg.calorie) / (1 * ureg.ounce)),
    Category("lightweight", (125 * 1000 * ureg.calorie) / (1 * ureg.ounce)),
    Category("very light", (140 * 1000 * ureg.calorie) / (1 * ureg.ounce)),
    Category("ultralight", (155 * 1000 * ureg.calorie) / (1 * ureg.ounce)),
    Category("hyperlight", (170 * 1000 * ureg.calorie) / (1 * ureg.ounce)),
]


def metric_energy(idiot_energy):
    return idiot_energy.to(ureg.kilojoule / ureg.gram)


def print_categories():
    rows = []
    for i, category in enumerate(_categories):
        if i == (len(_categories) - 1):
            rows.append([category.name, metric_energy(category.lower)])
        else:
            rows.append([category.name, metric_energy(category.lower), metric_energy(_categories[i + 1].lower)])

    print(tabulate(rows))


if __name__ == "__main__":
    print_categories()
