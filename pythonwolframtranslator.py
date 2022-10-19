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
        expression = "With[{eq = " + f"{eq_form}" + "}, " + f"{sym_form}]"
        result_temp = session.evaluate_wrap(expression)
        # print(result_temp) ## don't forget to delete
        # self.print_res((result_temp.result[0])) ## don't forget to delete
        val = result_temp.result
        tmp = session.evaluate_wrap("ToString[TeXForm[{}]]".format(val))
        # tmp = session.evaluate_wrap("ToString[TeXForm[{}]]".format(self.__flatten_to_list(result_temp.result[0]))) 
        print(tmp) ## don't forget to delete
        tmp_result = str(tmp)
        ind = tmp_result.index('=') + 1
        ind_end = tmp_result.index('>')
        result_to_latex = tmp_result[ind:ind_end]
        self.__close_session()
        return result_to_latex
    
    def print_res(self, res):
        print(self.__flatten_to_list(res))
    
    def __flatten_to_list(self, tuple_value):
        li = []
        for test in tuple_value:
            if type(test) is tuple:
                for item in test:
                    if type(item) is tuple:
                        li.extend(item)
                    else:
                        li.append(item)
            else:
                li.append(test)
        return li

    def __close_session(self):
        session.stop()
