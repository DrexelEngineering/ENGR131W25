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
            keys=['q1-1-helvetica-name-change', 'q1-2-font-weight-update'],
            options=[['A new `__init__` method', 'A method like `update_name(self, new_name)`', 'The `__str__` method', '`change_name(self)`, but without parameters'], ['`Regular`', '`Bold`', '`Helvetica Bold`', '`Error`']],
            descriptions=['Which method is best suited for changing the name of a typeface stored in a class instance?', 'What will the following code output?**\n```python\nclass Font:\n    def __init__(self, name, weight):\n        self.name = name\n        self.weight = weight\n    \n    def update_weight(self, new_weight):\n        self.weight = new_weight\n\nf = Font("Helvetica", "Regular")\nf.update_weight("Bold")\nprint(f.weight)\n```'],
            points=[1.0, 1.0],
        )
class Question3(TFQuestion):
    def __init__(self):
        super().__init__(
            title=f"True or False",
            style=TFStyle,
            question_number=3,
            keys=['q3-1-modifying-instance-attributes', 'q3-2-change-statements-property', 'q3-3-instance-vs-class-attributes'],
            descriptions=['A change method should modify an instance’s attributes directly using `self`.', '@property allows you to change the value of a instance attributes', 'Change methods should always modify class attributes instead of instance attributes.'],
            points=[1.0, 1.0, 1.0],
        )
class Question2(SelectMany):
    def __init__(self):
        super().__init__(
            title=f"Select All That Apply",
            style=MultiSelect,
            question_number=2,
            keys=['q2-1-font-change-methods', 'q2-2-font-style-adjustments'],
            descriptions=['Which of the following are best practices for writing a change method in Python?', 'Which of the following change methods would be appropriate for a `Font` class?'],
            options=[['Using `self.attribute = new_value` inside the method.', 'Using setter decorators.', 'Writing a method that prints the new value.', 'Naming the method something clear, like `set_weight(new_weight)`.'], ['`def change_font(self, new_name)`', '`def adjust_size(self, new_size)`', '`def __init__(self, name, size)`', '`def update_style(self, new_style)`']],
            points=[2.0, 2.0],
            grade=['parts'],
        )
