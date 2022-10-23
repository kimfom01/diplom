from wolframclient.evaluation import SecuredAuthenticationKey, WolframCloudSession


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
    sak: Any
        represents a Secured Authentication Key generated using the Wolfram Language function
    session: Any
        represent a session to a given cloud enabling simple API call

    Methods
    -------
    evaluate_equation():
        calculates the expression initialized in the constructor and returns a result in latex format
    """
    # TODO: add a method to convert the output to human readable form
    # Not all symbols can be evaluated
    # TODO: compile a list of symbols that the class can evaluate and use it to raise an exception when the user calls a symbol that isn't supported

    def __init__(self, consumer_key, consumer_secret):
        """
        Parameters
        ----------
        consumer_key : str
            a public key generated from wolframcloud used to connect to the cloud api
        consumer_secret : str
            a secret key generated from wolframcloud used to connect to the cloud api
        """
        self.sak = SecuredAuthenticationKey(consumer_key, consumer_secret)
        self.session = WolframCloudSession(credentials=self.sak)

    @property
    def equation(self):
        return self._equation

    @property
    def symbol(self):
        return self._symbol

    @property
    def var(self):
        return self._var

    def evaluate_equation(self, equation, symbol, var=None):
        """
        Calculates the expression initialized in the constructor and returns a result in latex format

        ...

        Parameters
        ----------
        equation : str
            a formatted string in the Wolfram Mathematica expression form
        symbol : str
            the symbol determining what will be evaluated
        var: str
            represents the varibles to be evaluated (default is None)

        Returns
        -------
        str
            a result in latex format
        """

        self._equation = equation
        self._symbol = symbol
        self._var = var

        self.session.start()
        if not self.session.authorized():
            raise ValueError(
                "Not Authorized! Please verify your secure authentication key!")
        eq = f"{self._equation}"
        if self._var == None:
            sym_form = f'{self._symbol}[{eq}]'
        else:
            sym_form = f'{self._symbol}[{eq}, {self._var}]'
        result = self.session.evaluate('ToString[TeXForm[{}]]'.format(self.session.evaluate(sym_form)))
        self.__close_session()
        return result

    def __close_session(self):
        """
        Closes the session
        """
        self.session.stop()
