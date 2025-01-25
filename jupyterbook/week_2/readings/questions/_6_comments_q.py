from pykubegrader.widgets.select_many import MultiSelect, SelectMany
from pykubegrader.widgets.true_false import TFQuestion, TFStyle
from pykubegrader.widgets.multiple_choice import MCQuestion, MCQ
import pykubegrader.initialize
import panel as pn

pn.extension()

class Question2(MCQuestion):
    def __init__(self):
        super().__init__(
            title=f"Select the Best Answer",
            style=MCQ,
            question_number=2,
            keys=['q2-1-description-of-a-comment-in-python', 'q2-2-Comment-Functionality'],
            options=[['A line of code that performs arithmetic operations', 'Text ignored by the Python interpreter, used to explain code', 'A special variable storing metadata about the program', 'A mandatory section in every Python program'], ['Defines a function for calculating stress', 'Explains the purpose of the program', 'Computes the stress from force and area', 'Is executed by Python']],
            descriptions=['Which of the following best describes a comment in Python?', 'In the example provided, what does the following line of code do? `# This program calculates stress from force and area`'],
            points=[1.0, 1.0],
        )
class Question1(TFQuestion):
    def __init__(self):
        super().__init__(
            title=f"Select if the statement is True or False",
            style=TFStyle,
            question_number=1,
            keys=['q1-1-tf-executed-comments', 'q1-2-tf-starting-question'],
            descriptions=['Comments in Python are executed by the interpreter.', 'A comment in Python must always start with a `#`.'],
            points=[1.0, 1.0],
        )
class Question3(SelectMany):
    def __init__(self):
        super().__init__(
            title=f"Select All That Apply",
            style=MultiSelect,
            question_number=3,
            keys=['q3-1-Using-Comments-in-Python', 'q3-2-Valid-Python-Comments'],
            descriptions=['Which of these are valid reasons to use comments in Python?', 'Which of the following lines are valid Python comments? the text that is written inside the \\` \\` exclusive of the ` is the code seen by the interpreter'],
            options=[['To explain complex code', 'To store temporary variables', 'To improve code readability', 'To communicate assumptions or logic to future readers'], ['`# This is a comment`', '`This is not a comment`', '`#Calculate the area`', '`// This is not a Python comment`']],
            points=[2.0, 2.0],
            grade=['parts'],
        )
