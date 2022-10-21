from pythonwolframtranslator import PyWolfTranslator

# eq = 'Derivative[2][x][t] - (3 t) + Derivative[1][x][t] == 0'
# symbol = 'DSolveValue'
# params = 'x[t], t'

# eq = 'x^2 + 2 x - 15 == 0'
# symbol = 'Roots'
# params = 'x'

# eq = 'x^2 + 2 x + 1'
# symbol = f'Factor[{eq}]'

# eq = 'x^2 + 3 x - 4 == 0'
# symbol = 'Roots'
# params = 'x'

# eq = '(x^3 - 1)/(x - 1)'
# symbol = 'Limit'
# params = 'x -> 1'

# eq = 'x^6'
# symbol = f'D[{eq}, x]'
# params = 'x'

# eq = '8 x^4'
# symbol = f'Integrate[{eq}, x]'
# params = 'x'

eq = 'y\'[x] + y[x] == x'
symbol = f'DSolveValue[{eq}, y[x], x]'
params = 'x'

# eq = 'Sin[x + I y]'
# symbol = f'ComplexExpand[{eq}]'

# eq = 'E^(I x)'
# symbol = f'ExpToTrig[{eq}]'

mytest = PyWolfTranslator(eq, symbol, params)
result = mytest.evaluate_equation()

print(result)
