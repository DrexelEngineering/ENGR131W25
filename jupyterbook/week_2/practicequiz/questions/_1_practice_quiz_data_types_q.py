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
            keys=['q1-1-Data-Structure-Modification', 'q1-2-Type-Conversion'],
            options=[['Dictionary', 'Frozenset', 'Tuple', 'String'], ['5.14 (Int)', '5.14 (Float)', '5.14 (String)', '3.142 (String)']],
            descriptions=['Which of the following Python data structures allows modification after creation?', 'What would be the output of the following code: `float("3.14") + 2`?'],
            points=[1.0, 1.0],
        )
class Question3(TFQuestion):
    def __init__(self):
        super().__init__(
            title=f"Select if the statement is True or False",
            style=TFStyle,
            question_number=3,
            keys=['q3-1-String-Operations', 'q3-2-List-Uniqueness'],
            descriptions=['In Python, the operation `"Hello"[1:3]` includes the character at index 3.', 'List elements in Python must be unique within the same list.'],
            points=[1.0, 1.0],
        )
class Question2(SelectMany):
    def __init__(self):
        super().__init__(
            title=f"Select All That Apply",
            style=MultiSelect,
            question_number=2,
            keys=['q2-1-Dictionary-Operations', 'q2-2-List-Methods'],
            descriptions=['Which of the following operations are valid for Python dictionaries?', 'Which of the following list methods modify the list in-place?'],
            options=[['Using a integer as a dictionary key', 'Adding new key value pairs after creation', 'Using lists as dictionary keys', 'Having duplicate keys in a dictionary'], ['append()', 'count()', 'sort()', 'index()']],
            points=[2.0, 2.0],
            grade=['parts'],
        )
