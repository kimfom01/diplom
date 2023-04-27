from core.pythonwolframtranslator import PyWolfTranslator
from auth import consumer_key, consumer_secret


def test_runner(key, secret, equation, symbol, variable=None):
    mytest = PyWolfTranslator(key, secret)

    if variable is None:
        return mytest.evaluate_equation(equation, symbol)
    return mytest.evaluate_equation(equation, symbol, variable)


eq = '{x\'[t] == -y[t] - x[t]^2, y\'[t] == 2 x[t] - y[t]^3, x[0] == y[0] == 1}'
sym = 'NDSolveValue'
var = '{x, y}, {t, 0, 20}'

result = test_runner(consumer_key, consumer_secret, eq, sym, var)
print(result)

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
