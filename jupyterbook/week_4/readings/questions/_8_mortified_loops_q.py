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
            keys=['q1-1-mortified-loop-syntax', 'q1-2-mortified-break-effect'],
            options=[['`for i in range(10):`', '`for (i = 0; i < 10; i++):`', '`foreach i in range(10):`', '`loop i from 0 to 10:`'], ['Terminates the loop entirely', 'Skips the rest of the current iteration and continues to the next iteration', 'Skips the entire program execution', 'Pauses the loop temporarily']],
            descriptions=['What is the correct syntax for a `for` loop in Python?', 'What does the `break` statement do in Python loops?'],
            points=[1.0, 1.0],
        )
class Question3(TFQuestion):
    def __init__(self):
        super().__init__(
            title=f"True or False",
            style=TFStyle,
            question_number=3,
            keys=['q3-1-mortified-loop-behavior', 'q3-2-mortified-loop-termination', 'q3-3-mortified-continue-effect'],
            descriptions=['A `for` loop in Python can only iterate over numeric values.', 'The `break` statement stops the execution of a loop and resumes the code after the loop.', 'The `continue` statement skips the remaining code in the loop for the current iteration and moves to the next iteration.'],
            points=[1.0, 1.0, 1.0],
        )
class Question2(SelectMany):
    def __init__(self):
        super().__init__(
            title=f"Select All That Apply",
            style=MultiSelect,
            question_number=2,
            keys=['q2-1-mortified-loop-utilities', 'q2-2-mortified-for-loop-features'],
            descriptions=['Which Python statements can alter the flow of a loop?', 'Which of the following are true about `for` loops in Python?'],
            options=[['`break`', '`continue`', '`end`', '`exit()`'], ['They can iterate over strings.', 'They can iterate over lists.', 'They require a `range` function.', 'They cannot use a `break` statement.']],
            points=[2.0, 2.0],
            grade=['parts'],
        )
