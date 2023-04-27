from generator import generate_data, csv_path
import numpy as np


def calculate_eigen_values(lines):
    eigen_values = []

    with open(csv_path) as file:
        for _ in range(lines):
            line = file.readline()
            line_array = line.split(",")
            array = np.array(
                [[int(line_array[0]), int(line_array[1])],
                 [int(line_array[2]),
                  int(line_array[3].replace("\n", ""))]])
            value, _ = np.linalg.eig(array)
            eigen_values.append(value)
    return eigen_values


def write_output(eigen_values):
    with open("../out/output.txt", "w") as output:
        for value in eigen_values:
            found = False
            for num in value:
                if num >= 0:
                    found = True
                    break
            if found:
                output.write("1\n")
            else:
                output.write("0\n")


lines = 1000

generate_data(lines)

eigen_values = calculate_eigen_values(lines)

write_output(eigen_values)
