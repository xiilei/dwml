## dwml - ms-office omml to latex converter
 [![Build status](https://api.travis-ci.org/xiilei/dwml.png?branch=master)](https://travis-ci.org/xiilei/dwml)

![dwml demo](https://raw.githubusercontent.com/xiilei/dwml/master/tests/composite_ml.png)   

转换为

```latex
f\left(x\right)
  =a_{0}+\sum_{n=1}^{\infty}\left(a_{n}\cos(\frac{n\pi x}{L})
  +b_{n}\sin(\frac{n\pi x}{L})\right)
```

 Usage
=======

```python
from dwml import omml
for omath in omml.load('tests/composite.xml'):
    print(omath.latex)
```

#### [A sample](https://github.com/xiilei/dwml/blob/master/tests/docx.py) that converting word math formula to latex 

```python
from tests.docx import to_latex
to_latex(filename='tests/simple.docx')
```
