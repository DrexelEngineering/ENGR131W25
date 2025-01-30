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
            keys=['q1-1-door-direction-parameters', 'q1-2-door-return-values'],
            options=[['Correct', 'Wrong', 'None', 'Error'], ['It returns `None` by default.', 'It raises an error.', 'It loops indefinitely.', 'It returns the first argument passed to it.']],
            descriptions=['What will the following function call output?**\n```python\ndef check_door(direction):\n    if direction == "push":\n        return "Correct"\n    else:\n        return "Wrong"\n        \nprint(check_door("pull"))\n```', 'What happens if a function has no `return` statement?'],
            points=[1.0, 1.0],
        )
class Question3(TFQuestion):
    def __init__(self):
        super().__init__(
            title=f"True or False",
            style=TFStyle,
            question_number=3,
            keys=['q3-1-default-parameters', 'q3-2-multiple-arguments', 'q3-3-return-early'],
            descriptions=['A function parameter can have a default value, which is used if no argument is passed for that parameter.', 'A Python function can only accept one argument.', 'The `return` statement can be used to exit a function before all lines of code in the function are executed.'],
            points=[1.0, 1.0, 1.0],
        )
class Question2(SelectMany):
    def __init__(self):
        super().__init__(
            title=f"Select All That Apply",
            style=MultiSelect,
            question_number=2,
            keys=['q2-1-function-parameters', 'q2-2-return-statement-usage'],
            descriptions=['Which of the following are true about function parameters in Python?', 'Which of the following are true about the `return` statement in Python?'],
            options=[['Parameters are placeholders for arguments passed to a function.', 'A function can accept multiple parameters.', 'Parameters must always have default values.', 'Parameters are optional when calling a function.'], ["The `return` statement ends a function's execution.", 'A function can return multiple values.', 'If no `return` statement is provided, the function returns `None`.', 'A function cannot include more than one `return` statement.']],
            points=[2.0, 2.0],
            grade=['parts'],
        )
