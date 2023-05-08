import csv
import random

csv_path = "../out/matrices.csv"


def __get_random(lower, upper):
    return [
        random.randint(lower, upper),
        random.randint(lower, upper),
        random.randint(lower, upper),
        random.randint(lower, upper)
    ]


def generate_matrices(lines):
    headers = ["a[0]", "a[1]", "a[2]", "a[3]"]

    with open(csv_path, "w") as output_file:
        head = csv.DictWriter(output_file, delimiter=",", fieldnames=headers)
        head.writeheader()

        body = csv.writer(output_file)
        for _ in range(lines):
            row = __get_random(-9, 9)
            body.writerow(row)


if __name__ == "__main__":
    generate_matrices()
