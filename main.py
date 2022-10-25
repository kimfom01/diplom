from pythonwolframtranslator import PyWolfTranslator
from auth import consumer_key, consumer_secret

def test_runner(key, secret, eq, symb, var=None):
    mytest = PyWolfTranslator(key, secret)

    if var == None:
        return mytest.evaluate_equation(eq, symb)
    return mytest.evaluate_equation(eq, symb, var)


eq = 'Sin[x + I y]'
symbol = 'ComplexExpand'
var = None

result = test_runner(consumer_key, consumer_secret, eq, symbol, var)
print(result)

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