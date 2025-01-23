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
            keys=['q1-1-first-date-while-syntax', 'q1-2-first-date-while-purpose'],
            options=[['`while (condition) { }`', '`while condition:`', '`loop while condition:`', '`while: condition`'], ['To execute a block of code while a condition is `True`', 'To execute a block of code a fixed number of times', 'To execute a block of code for each item in a sequence', 'To declare variables inside a loop']],
            descriptions=['What is the correct syntax for a `while` loop in Python?', 'What is the purpose of a `while` loop in Python?'],
            points=[1.0, 1.0],
        )
class Question3(TFQuestion):
    def __init__(self):
        super().__init__(
            title=f"True or False",
            style=TFStyle,
            question_number=3,
            keys=['q3-1-first-date-while-infinite', 'q3-2-first-date-while-check-before', 'q3-3-first-date-while-break'],
            descriptions=['A `while True:` loop will run infinitely unless there is a `break` statement inside it.', 'A `while` loop checks its condition before executing the loop body.', 'A `while` loop will always execute at least once, even if the condition is `False` initially.'],
            points=[1.0, 1.0, 1.0],
        )
class Question2(SelectMany):
    def __init__(self):
        super().__init__(
            title=f"Select All That Apply",
            style=MultiSelect,
            question_number=2,
            keys=['q2-1-first-date-while-features', 'q2-2-first-date-while-common-errors'],
            descriptions=['Which of the following are true about `while` loops in Python?', 'Which of the following can cause an infinite `while` loop in Python?'],
            options=[['A `while` loop executes as long as its condition is `True`.', 'A `while` loop can run infinitely if the condition never becomes `False`.', 'A `while` loop can include a `break` statement to exit early.', 'A `while` loop requires a `range()` function.'], ['Forgetting to update variables inside the loop', 'Using a `True` condition without a `break` statement', 'Setting the condition to `False`', 'Including unreachable code after a `break` statement']],
            points=[2.0, 2.0],
            grade=['parts'],
        )
