# diplom

Topic: Разработка трансляции кода из Python в Wolfram Mathematica <!-- (Development of code translation from Python to Wolfram Mathematica) -->

### Description:
pythonwolframtranslator is a python library that can be used to carry out certain mathematical calculations. It is built upon the Wolfram Mathematica Cloud Engine. Connection to the cloud is made possible through the open source library [wolframclient](https://pypi.org/project/wolframclient/).

### How to try it out
Download the repo and add it to your project  
![repo-download2](https://user-images.githubusercontent.com/57032138/197413405-8820f26e-8759-4a28-9578-664184bbec02.png)

or Clone the repo using the following commands
``` shell
git clone https://github.com/kimfom01/coursework.git
```

Install the wolframclient library
``` shell
pip install wolframclient
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

[The document can be found here](https://docs.google.com/document/d/1U_7Qk7QTGbCNAzYMTHI8Gfd0FBSQ6o2Mmyp-psyEcQQ/edit?usp=sharing)

### Feel free to raise issues encountered with the project and I will address them as soon as possible
