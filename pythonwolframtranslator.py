from wolframclient.evaluation import WolframLanguageSession
session = WolframLanguageSession()

class PyWolfTranslator:
    def __init__(self, equation, symbol, parameters=''):
        self._equation = equation
        self._symbol = symbol
        self._parameters = parameters
    
    @property
    def equation(self):
        return self._equation
    
    @property
    def symbol(self):
        return self._symbol

    @property
    def parmeters(self):
        return self._parameters
    
    def evaluate_equation(self):
        eq = f"{self._equation}"
        if self.parmeters == '':
            sym_form = f'{self._symbol}[{eq}]'
        else:
            sym_form = f'{self._symbol}[{eq}, {self._parameters}]'
        result = session.evaluate(sym_form)
        result_to_latex = session.evaluate(f'ToString[TeXForm[{result}]]')
        self.__close_session()
        return result_to_latex

    def __close_session(self):
        session.stop()
