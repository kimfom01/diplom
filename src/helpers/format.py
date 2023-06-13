import csv

final = ""

with open("../out/demo.txt") as file:
    _ = file.readline()
    text = file.read()
    text = text.replace("\n", "")
    text = text.replace(";00", ";00\n")
    final = text

headers = ["solution", "blank"]

with open("../out/new_demo.txt", "w+") as file:
    head = csv.DictWriter(file, delimiter=";", fieldnames=headers)
    head.writeheader()
    file.write(final)
