from wolframclient.evaluation import WolframLanguageSession
session = WolframLanguageSession()

class PyWolfTranslator:
    """
    A class used to represent the translator object and calulate given expression
    
    ...
    
    Attributes
    ----------
    equation : str
        a formatted string in the Wolfram Mathematica expression form
    symbol : str
        the symbol determining what will be evaluated
    var: str
        represents the varibles to be evaluated (default is None)

    Methods
    -------
    evaluate_equation():
        calculates the expression initialized in the constructor and returns a result in latex format
    """
    def __init__(self, equation, symbol, var=None):
        """
        Parameters
        ----------
        equation : str
            a formatted string in the Wolfram Mathematica expression form
        symbol : str
            the symbol determining what will be evaluated
        var: str
            represents the varibles to be evaluated (default is None)
        """
        self._equation = equation
        self._symbol = symbol
        self._var = var
    
    @property
    def equation(self):
        return self._equation
    
    @property
    def symbol(self):
        return self._symbol

    @property
    def var(self):
        return self._var
    
    def evaluate_equation(self):
        """
        Calculates the expression initialized in the constructor and returns a result in latex format

        Returns
        -------
        str
            a result in latex format
        """
        # Not all symbols can be evaluated
        # TODO: compile a list of symbols that the class can evaluate and use it to raise an exception when the user calls a symbol that isn't supported
        eq = f"{self._equation}"
        if self._var == None:
            sym_form = f'{self._symbol}[{eq}]'
        else:
            sym_form = f'{self._symbol}[{eq}, {self._var}]'
        result = session.evaluate(sym_form)
        result_to_latex = session.evaluate(f'ToString[TeXForm[{result}]]')
        self.__close_session()
        return result_to_latex

    def __close_session(self):
        """
        Closes the session
        """
        session.stop()
