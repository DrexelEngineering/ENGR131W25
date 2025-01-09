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
            keys=['q1-1-Pootie-Tang-Uppercase', 'q1-2-Replace-Strings'],
            options=[['`phrase.uppercase()`', '`uppercase(phrase)`', '`phrase.upper()`', '`phrase.toUpperCase()`'], ['`phrase.replace("awesome", "cool")`', '`replace(phrase, "cool", "awesome")`', '`phrase.replace("cool", "awesome")`', '`phrase.sub("cool", "awesome")`']],
            descriptions=['Pootie Tang wants his catchphrase "Wa Da Tah!" to be LOUDER. How can he make it uppercase in Python?', 'Pootie Tang’s line "PootieTang is cool" needs a style upgrade. What Python method can he use to replace "cool" with "awesome"?'],
            points=[1.0, 1.0],
        )
class Question3(TFQuestion):
    def __init__(self):
        super().__init__(
            title=f"True or False",
            style=TFStyle,
            question_number=3,
            keys=['q3-1-String-Repeat-tf'],
            descriptions=['Using the `*` operator, Pootie Tang can repeat his phrase "Sa Da Tay!" three times in Python.'],
            points=[1.0],
        )
class Question2(SelectMany):
    def __init__(self):
        super().__init__(
            title=f"Select All That Apply",
            style=MultiSelect,
            question_number=2,
            keys=['q2-1-String-Methods'],
            descriptions=['Which of the following are valid string methods in Python? (Select all that apply)'],
            options=[['`join()`', '`split()`', '`replace()`', '`combine()`', '`upper()`']],
            points=[2.0],
            grade=['parts'],
        )
