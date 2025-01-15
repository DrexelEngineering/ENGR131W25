from pykubegrader.widgets.select_many import MultiSelect, SelectMany
from pykubegrader.widgets.true_false import TFQuestion, TFStyle
from pykubegrader.widgets.multiple_choice import MCQuestion, MCQ
import pykubegrader.initialize
import panel as pn

pn.extension()

class Question1(MCQuestion):
    def __init__(self):
        super().__init__(
            title=f"Syntax-Errors",
            style=MCQ,
            question_number=1,
            keys=['q1-1-syntax-errors', 'q1-2-semantic-errors'],
            options=[['The program runs but produces incorrect results', 'The program crashes while running', 'The program doesn’t run at all', 'Python automatically fixes the error for you'], ['Your code violates Python syntax rules', 'Your program crashes unexpectedly during execution', 'Your program runs but produces incorrect results', 'Your code contains typos that prevent it from running']],
            descriptions=['What happens when your Python program has a syntax error?', 'Which statement best describes a semantic error?'],
            points=[1.0, 1.0],
        )
class Question3(TFQuestion):
    def __init__(self):
        super().__init__(
            title=f"Syntax Errors",
            style=TFStyle,
            question_number=3,
            keys=['q3-1-Syntax-Errors-TF', 'q3-2-Semantic-Errors-TF', 'q3-3-Error-Debugging-TF'],
            descriptions=['Python can run a program even if it contains syntax errors.', 'Semantic errors can only occur in complex programs, not in simple ones.', 'Using known inputs and outputs is a good technique for finding semantic errors.'],
            points=[1.0, 1.0, 1.0],
        )
class Question2(SelectMany):
    def __init__(self):
        super().__init__(
            title=f"Runtime Error Characteristics",
            style=MultiSelect,
            question_number=2,
            keys=['q2-1-Runtime-Error-Characteristics', 'q2-2-Error-Handling-Techniques'],
            descriptions=['Which of the following are characteristics of runtime errors? (Select all that apply)', 'Which of the following are valid techniques for handling runtime errors in Python? (Select all that apply)'],
            options=[['They occur during program execution', 'They can be caused by dividing by zero', 'They always involve syntax issues', 'They never require consultation with a debugging duck'], ['Using `try/except` blocks', 'Validating user inputs before performing operations', 'Ignoring the error and proceeding with execution', 'Writing code without any error-handling mechanisms']],
            points=[2.0, 2.0],
            grade=['parts'],
        )
