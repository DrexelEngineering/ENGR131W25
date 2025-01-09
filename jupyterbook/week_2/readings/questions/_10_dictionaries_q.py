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
            keys=['q1-1-Dictionary-Access', 'q1-2-Dictionary-Modification'],
            options=[['"views"', '100', '{"views": 100}', '50'], ['`metrics.add("shares", 25)`', '`metrics["shares"] = 25`', '`metrics.shares = 25`', '`metrics = {"shares": 25}`']],
            descriptions=['Given the dictionary: `metrics = {"views": 100, "likes": 50}`, what would `metrics["views"]` return?', 'Which of these correctly adds a new key-value pair to an existing dictionary?'],
            points=[1.0, 1.0],
        )
class Question3(TFQuestion):
    def __init__(self):
        super().__init__(
            title=f"Select if the statement is True or False",
            style=TFStyle,
            question_number=3,
            keys=['q3-1-Dictionary-Values'],
            descriptions=['Dictionary values can be of different types within the same dictionary (e.g., mixing strings and numbers).'],
            points=[1.0],
        )
class Question2(SelectMany):
    def __init__(self):
        super().__init__(
            title=f"Select All That Apply",
            style=MultiSelect,
            question_number=2,
            keys=['q2-1-Valid-Dictionary-Keys'],
            descriptions=['Which of these can be used as dictionary keys in Python?'],
            options=[['`"pageviews"`', '`[1, 2, 3]`', '`42`', '`{"nested": "dict"}`']],
            points=[2.0],
            grade=['parts'],
        )
