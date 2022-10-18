from wolframclient.evaluation import WolframLanguageSession
session = WolframLanguageSession()

class PyWolfTranslator:
    def __init__(self, equation, symbol):
        self._equation = equation
        self._symbol = symbol
    
    @property
    def equation(self):
        return self._equation
    
    @property
    def symbol(self):
        return self._symbol
    
    def evaluate_equation(self):
        eq_form = f"{self._equation}"
        sym_form = self._symbol
        expr = "With[{eq = " + f"{eq_form}" + "}, " + f"{sym_form}]"
        result_temp = session.evaluate_wrap(expr)
        tmp = session.evaluate_wrap("ToString[TeXForm[{}]]".format(result_temp.result[0][0][1]))
        tmp_result = str(tmp)
        ind = tmp_result.index('=') + 1
        ind_end = tmp_result.index('>')
        result_to_latex = tmp_result[ind:ind_end]
        return result_to_latex



eq = 'x^2 + a x + 1 == 0'
symbol = 'Solve[eq, x]'
mytest = PyWolfTranslator(eq, symbol)
print(mytest.equation)
result = mytest.evaluate_equation()
print(result)