from pykubegrader.widgets.select_many import MultiSelect, SelectMany
from pykubegrader.widgets.true_false import TFQuestion, TFStyle
from pykubegrader.widgets.multiple_choice import MCQuestion, MCQ
import pykubegrader.initialize
import panel as pn

pn.extension()

class Question1(MCQuestion):
    def __init__(self):
        super().__init__(
            title=f"Why are descriptive variable names recommended?",
            style=MCQ,
            question_number=1,
            keys=['q1-1-Descriptive-Variable-Names', 'q1-2-Converting-Variable-Types'],
            options=[['To make the program run faster', 'To make the code easier to understand and maintain', 'To avoid syntax errors in Python', 'To ensure compatibility with older Python versions'], ['Assigning a float to a variable that previously held a string', 'Using the `float()` function to convert a string to a numeric type', 'Using a new variable name for a different type of value', 'Concatenating a number with a string']],
            descriptions=['Why are descriptive variable names recommended?', 'What is an example of converting variable types in Python, as shown in the notebook?'],
            points=[1.0, 1.0],
        )
class Question3(TFQuestion):
    def __init__(self):
        super().__init__(
            title=f'Constants in Python are enforced by the interpreter to never change their values.',
            style=TFStyle,
            question_number=3,
            keys=['q3-1-Constants-tf'],
            descriptions=['Constants in Python are enforced by the interpreter to never change their values.'],
            points=[1.0],
        )
class Question3(SelectMany):
    def __init__(self):
        super().__init__(
            title=f'Which of these rules are correct for naming variables in Python?',
            style=MultiSelect,
            question_number=3,
            keys=['q3-1-Rules-for-Naming-Variables', 'q3-2-Multi-Variable-Assignment'],
            descriptions=['Which of these rules are correct for naming variables in Python?', 'Which of the following illustrate multi-variable assignment in Python?'],
            options=[['Variables must start with a letter or an underscore (`_`).', 'Variables can contain spaces.', 'Variable names are case-sensitive.', 'Variables can include numbers but cannot start with them.'], ['`a, b, c = 1, 2, 3`', '`a = b = c = 0`', '`a = 1; b = 2; c = 3`', '`a, b = 1 2`']],
            points=[2.0, 2.0],
            grade=['parts'],
        )
