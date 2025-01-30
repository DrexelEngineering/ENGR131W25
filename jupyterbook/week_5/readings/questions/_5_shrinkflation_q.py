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
            keys=['q1-1-shrinkflation-prices', 'q1-2-global-local-variables'],
            options=[['5', 'Error: `new_price` is not defined.', 'None', 'The function returns 5.'], ['The global variable is overwritten.', 'The local variable takes precedence inside the function.', 'Both variables are combined into one.', 'The program raises an error.']],
            descriptions=['What is the output of the following code?\n```python\ndef calculate_price():\n    new_price = 5\n\ncalculate_price()\nprint(new_price)\n```', 'What happens if a local variable has the same name as a global variable?'],
            points=[1.0, 1.0],
        )
class Question3(TFQuestion):
    def __init__(self):
        super().__init__(
            title=f"True or False",
            style=TFStyle,
            question_number=3,
            keys=['q3-1-global-keyword', 'q3-2-local-variables', 'q3-3-multiple-scopes'],
            descriptions=['Using the `global` keyword inside a function allows you to modify a global variable.', 'Local variables are destroyed once the function they belong to finishes execution.', 'It’s possible for a global variable and a local variable to have the same name but behave differently in their respective scopes.'],
            points=[1.0, 1.0, 1.0],
        )
class Question2(SelectMany):
    def __init__(self):
        super().__init__(
            title=f"Select All That Apply",
            style=MultiSelect,
            question_number=2,
            keys=['q2-1-global-and-local-variables', 'q2-2-shrinkflation-variables'],
            descriptions=['Which of the following are true about global and local variables in Python?', 'Which of the following scenarios involve issues with variable scope?'],
            options=[['A global variable is accessible inside a function unless shadowed by a local variable.', 'A local variable is created when assigned inside a function.', 'A local variable can be accessed outside the function where it was created.', 'Using the `global` keyword inside a function allows you to modify a global variable.'], ['A function tries to modify a global variable without declaring it as global.', 'A local variable inside a function is accessed outside the function.', 'A global variable is used directly in a function without being declared.', 'Two functions use local variables with the same name.']],
            points=[2.0, 2.0],
            grade=['parts'],
        )
