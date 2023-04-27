import csv
import random


def __get_random(lower, upper):
    return [
        random.randint(lower, upper),
        random.randint(lower, upper),
        random.randint(lower, upper),
        random.randint(lower, upper)
    ]


def generate_data(lines):
    with open("../out/data.csv", "w") as output_file:
        writer = csv.writer(output_file)
        for i in range(lines):
            row = __get_random(-9, 9)
            writer.writerow(row)


if __name__ == "__main__":
    generate_data()