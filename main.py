import time
from pythonwolframtranslator import PyWolfTranslator
from auth import consumer_key, consumer_secret


def test_runner(key, secret, equation, symbol, variable=None):
    mytest = PyWolfTranslator(key, secret)

    if variable is None:
        return mytest.evaluate_equation(equation, symbol)
    return mytest.evaluate_equation(equation, symbol, variable)


eq = '{y\'[x] + y[x] == x, y[0] == 1}'
sym = 'NDSolveValue'
var = 'y, {x, 0, 10}'

start = time.time()
result = test_runner(consumer_key, consumer_secret, eq, sym, var)
print(result)
print(time.time() - start)

# eq = 'x^2 + 2 x + 1'
# symbol = 'Factor'
# var = None

# eq = 'x^2 + 3 x - 4 == 0'
# symbol = 'Roots'
# var = 'x'

# eq = '(x^3 - 1)/(x - 1)'
# symbol = 'Limit'
# var = 'x -> 1'

# eq = 'x^6'
# symbol = 'D'
# var = 'x'

# eq = '8 x^4'
# symbol = 'Integrate'
# var = 'x'

# eq = 'y\'[x] + y[x] == x'
# symbol = 'DSolveValue'
# var = 'y[x], x'

# eq = 'Sin[x + I y]'
# symbol = 'ComplexExpand'
# var = None
