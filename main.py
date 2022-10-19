from pythonwolframtranslator import PyWolfTranslator

eq = 'Derivative[2][x][t] - (3 t) + Derivative[1][x][t] == 0'
symbol = 'DSolve[eq, x[t], t]'
mytest = PyWolfTranslator(eq, symbol)
# print(mytest.equation)
result = mytest.evaluate_equation()
print(result)