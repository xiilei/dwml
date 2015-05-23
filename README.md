## dwml - A Python library for reading DrawingML of Microsoft office (2007 and above),And Convert them to latex

 Usage
=======

```python
from dwml import omml
for omath in omml.load('tests/composite.xml'):
    print(omath.latex)
```

#### A simple module for converting word omml to latex

```python
from dwml.docx import to_latex
to_latex(filename='tests/simple.docx')
```