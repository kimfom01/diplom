from pythonwolframtranslator import PyWolfTranslator

# eq = 'Derivative[2][x][t] - (3 t) + Derivative[1][x][t] == 0'
# symbol = 'DSolveValue'
# var = 'x[t], t'

# eq = 'x^2 + 2 x - 15 == 0'
# symbol = 'Roots'
# var = 'x'

# eq = 'x^2 + 2 x + 1'
# symbol = f'Factor[{eq}]'
# var = ''

# eq = 'x^2 + 3 x - 4 == 0'
# symbol = 'Roots'
# var = 'x'

# eq = '(x^3 - 1)/(x - 1)'
# symbol = 'Limit'
# var = 'x -> 1'

# eq = 'x^6'
# symbol = f'D[{eq}, x]'
# var = 'x'

# eq = '8 x^4'
# symbol = f'Integrate[{eq}, x]'
# var = 'x'

eq = 'y\'[x] + y[x] == x'
symbol = f'DSolveValue[{eq}, y[x], x]'
var = 'x'

# eq = 'Sin[x + I y]'
# symbol = f'ComplexExpand[{eq}]'
# var = ''

# eq = 'E^(I x)'
# symbol = f'ExpToTrig[{eq}]'
# var = ''

mytest = PyWolfTranslator('CkD8JODcVcYDXXx/xU0IHzBBdrRZmaqvW6iRiedcrgk=',
                          '8RaVLaIsJAO3F8D0IakGi1UrDay0Uf2GLFK85LJaNtk=')
result = mytest.evaluate_equation(eq, symbol, var)

print(result)
# print(mytest.__doc__)
