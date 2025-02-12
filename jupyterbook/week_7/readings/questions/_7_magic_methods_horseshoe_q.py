from pykubegrader.widgets.select_many import MultiSelect, SelectMany
from pykubegrader.widgets.true_false import TFQuestion, TFStyle
from pykubegrader.widgets.multiple_choice import MCQuestion, MCQ
import pykubegrader.initialize
import panel as pn

pn.extension()

class Question1(MCQuestion):
    def __init__(self):
        super().__init__(
            title=f"Select the Best Answer",
            style=MCQ,
            question_number=1,
            keys=['q1-1-horseshoecrab-init-method', 'q1-2-horseshoecrab-string-method'],
            options=[['It prints the attributes of the horseshoe crab.', 'It initializes the attributes of a new `HorseshoeCrab` instance.', 'It defines the default behavior of the class.', 'It is required for every class in Python.'], ['`HorseshoeCrab`', '`Horseshoe Crab of species Limulus polyphemus`', '`<__main__.HorseshoeCrab object at 0x...>`', '`Error`']],
            descriptions=['What does the `__init__` method do in a class like `HorseshoeCrab`?', 'What will the following code output?**\n```python\nclass HorseshoeCrab:\n    def __init__(self, species):\n        self.species = species\n    \n    def __str__(self):\n        return f"Horseshoe Crab of species {self.species}"\n\nh = HorseshoeCrab("Limulus polyphemus")\nprint(h)\n```'],
            points=[1.0, 1.0],
        )
class Question3(TFQuestion):
    def __init__(self):
        super().__init__(
            title=f"True or False",
            style=TFStyle,
            question_number=3,
            keys=['q3-1-magic-method-naming', 'q3-2-string-representation', 'q3-3-horseshoecrab-addition'],
            descriptions=['All magic methods in Python start and end with double underscores (`__`).', 'If a class does not define `__str__`, calling `print()` on an instance will return a default memory address representation.', 'The `__add__` magic method allows us to use the `+` operator with class instances.'],
            points=[1.0, 1.0, 1.0],
        )
class Question2(SelectMany):
    def __init__(self):
        super().__init__(
            title=f"Select All That Apply",
            style=MultiSelect,
            question_number=2,
            keys=['q2-1-horseshoecrab-magic-methods', 'q2-2-horseshoecrab-comparison'],
            descriptions=['Which of the following are valid magic methods in Python?', 'Which magic methods are useful for comparing two `HorseshoeCrab` objects?'],
            options=[['`__init__`', '`__str__`', '`__add__`', '`__hemocyanin__`'], ['`__eq__`', '`__lt__`', '`__compare__`', '`__gt__`']],
            points=[2.0, 2.0],
            grade=['parts'],
        )
