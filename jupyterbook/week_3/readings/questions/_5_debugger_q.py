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
            keys=['q1-1-Debugging-History', 'q1-2-Error-Symptoms', 'q1-3-Debugging-Techniques'],
            options=[['A logic error in the Harvard Mark II', 'A syntax error in an early computer program', 'A literal moth stuck in a relay', 'A hardware malfunction due to overheating'], ['Start rewriting the entire program', 'Identify the symptoms and check error messages', 'Remove random lines of code until it works', 'Restart your computer'], ['Debugging with a physical rubber duck to press against buttons', 'Explaining your code, line by line, to a rubber duck or inanimate object', 'Using an automated tool to debug code', 'A debugging method where you remove bugs randomly']],
            descriptions=['What was the original "bug" that led to the term "debugging" in computing?', 'When your program crashes, what should you do first?', 'What is rubber duck debugging?'],
            points=[1.0, 1.0, 1.0],
        )
class Question3(TFQuestion):
    def __init__(self):
        super().__init__(
            title=f"True or False",
            style=TFStyle,
            question_number=3,
            keys=['q3-1-Error-Messages-TF-debugger', 'q3-2-Debugging-Mindset', 'q3-3-Rubber-Duck-Debugging'],
            descriptions=['Error messages are unhelpful and should be ignored.', 'Debugging should be approached methodically, making one change at a time.', 'Rubber duck debugging works because explaining your code out loud helps identify errors.'],
            points=[1.0, 1.0, 1.0],
        )
class Question2(SelectMany):
    def __init__(self):
        super().__init__(
            title=f"Select All That Apply",
            style=MultiSelect,
            question_number=2,
            keys=['q2-1-Debugging-Tools', 'q2-2-Debugging-Scenarios'],
            descriptions=['Which of the following are effective debugging tools? (Select all that apply)', 'Which of the following are common debugging scenarios? (Select all that apply)'],
            options=[['Print statements', 'Built-in debuggers in IDEs', 'Restarting your computer', 'Carefully reading error messages'], ['Code crashes due to a runtime error', 'Code runs but produces incorrect results', 'Code refuses to run due to a syntax error', 'Code works perfectly on the first try']],
            points=[2.0, 2.0],
            grade=['parts'],
        )
