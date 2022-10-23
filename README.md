# coursework

Topic: Разработка трансляции кода из Python в Wolfram Mathematica <!-- (Development of code translation from Python to Wolfram Mathematica) -->

### Description:
pythonwolframtranslator is a python library that can be used to carry out certain mathematical calculations. It is built upon the Wolfram Mathematica Cloud Engine. Connection to the cloud is made possible through the open source library [wolframclient](https://pypi.org/project/wolframclient/).

### How to try it out
Install the library
``` sh
$ pip install wolframclient
```
[Generate a Secured Authentication Key](https://reference.wolfram.com/language/WolframClientForPython/docpages/basic_usages.html#wolfram-cloud-interactions:~:text=Generate%20a%20Secured%20Authentication%20Key) or you can use mine for demo purposes. The Secure Authentication Key consists of a consumer key and a consumer secret key. They will be used to connect to the cloud API.

Import the pythonwolframtranslator
``` py
from pythonwolframtranslator import PyWolfTranslator
```

Instantiate the object
``` py
my_object = PyWolfTranslator(consumer_key, consumer_secret)
```

Call the evaluate_equation method
``` py
eq = 'Sin[x + I y]'
symbol = f'ComplexExpand'

result1 = my_object.evaluate_equation(eq, symbol)
# output -> \sin (x) \cosh (y)+i \cos (x) \sinh (y)

eq = 'x^2 + 3 x - 4 == 0'
symbol = 'Roots'
var = 'x'

result2 = my_object.evaluate_equation(eq, symbol, var)
# output -> x=-4\lor x=1
```

Some of the supported symbols can be found [here](https://www.wolfram.com/language/fast-introduction-for-math-students/en/)

### Feel free to raise issues encountered with the project and I will address them as soon as possible