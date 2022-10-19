from pythonwolframtranslator import PyWolfTranslator

# eq = 'Derivative[2][x][t] - (3 t) + Derivative[1][x][t] == 0'
# symbol = 'DSolve[eq, x[t], t]'

eq = 'x^2 + 2 x - 15 = 0'
symbol = 'Solve[eq, x]'

mytest = PyWolfTranslator(eq, symbol)
result = mytest.evaluate_equation()

print(result)