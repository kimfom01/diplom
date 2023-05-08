from core.pythonwolframtranslator import PyWolfTranslator
from auth import consumer_key, consumer_secret

csv_path = "./out/matrices.csv"


def solve_equation(key, secret, equation, symbol, variable=None):
    mytest = PyWolfTranslator(key, secret)

    if variable is None:
        return mytest.evaluate_equation(equation, symbol)
    return mytest.evaluate_equation(equation, symbol, variable)


def calculate_eigen_values(lines):
    result = []

    with open(csv_path) as file:
        _ = file.readline()

        for _ in range(lines):
            line = file.readline()
            line = line.replace("\n", "")
            matrix = line.split(",")
            eq = f'x\'[t] == -{matrix[0]} y[t] - {matrix[1]} x[t]^2, y\'[t] == {matrix[2]} x[t] - {matrix[3]} y[t]^3, x[0] == y[0] == 1'
            eq = '{' + eq + '}'
            sym = 'NDSolveValue'
            var = '{x, y}, {t, 0, 20}'
            result.append(solve_equation(
                consumer_key, consumer_secret, eq, sym, var))
    return result


lines = 1000

values = calculate_eigen_values(lines)

values = str(list(map(str, values)))

with open("output.txt", "w") as final:
    final.writelines(values)


# eq = '{x\'[t] == -y[t] - x[t]^2, y\'[t] == 2 x[t] - y[t]^3, x[0] == y[0] == 1}'
# sym = 'NDSolveValue'
# var = '{x, y}, {t, 0, 20}'

# result = test_runner(consumer_key, consumer_secret, eq, sym, var)
# print(result)

# eq = 'x^2 + 2 x + 1'
# sym = 'Factor'
# var = None

# eq = 'x^2 + 3 x - 4 == 0'
# sym = 'Roots'
# var = 'x'

# eq = '(x^3 - 1)/(x - 1)'
# sym = 'Limit'
# var = 'x -> 1'

# eq = 'x^6'
# sym = 'D'
# var = 'x'

# eq = '8 x^4'
# sym = 'Integrate'
# var = 'x'

# eq = '{y\'[x] + y[x] == x, y[0] == 1}'
# sym = 'NDSolveValue'
# var = 'y, {x, 0, 10}'

# eq = 'Sin[x + I y]'
# sym = 'ComplexExpand'
# var = None
