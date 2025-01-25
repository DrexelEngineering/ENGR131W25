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
            keys=['q1-1-Floating-Point-Precision'],
            options=[['(0.1 + 0.2) == 0.3', 'abs((0.1 + 0.2) - 0.3) < 1e-10', 'if int(0.1 + 0.2) == int(0.3)', 'if str(0.1 + 0.2) == str(0.3)']],
            descriptions=['A NIST scientist needs to compare two measurements: 0.1 + 0.2 and 0.3. Which Python code would be most appropriate for this comparison?'],
            points=[1.0],
        )
class Question3(TFQuestion):
    def __init__(self):
        super().__init__(
            title=f"True or False",
            style=TFStyle,
            question_number=3,
            keys=['q3-1-Precision-Loss-tf'],
            descriptions=['When converting between different numerical types in Python (e.g., float to int), precision loss can occur.'],
            points=[1.0],
        )
class Question2(SelectMany):
    def __init__(self):
        super().__init__(
            title=f"Select All That Apply",
            style=MultiSelect,
            question_number=2,
            keys=['q2-1-Number-Representation'],
            descriptions=['Which of the following statements about number representation in Python are correct? (Select all that apply)'],
            options=[['Integers in Python have unlimited precision', 'Floating-point numbers can represent decimal numbers', 'All decimal numbers can be represented exactly in binary', 'The math.isclose() function is better than == for comparing floats', 'Double precision floating-point numbers are more efficient than single precision']],
            points=[2.0],
            grade=['parts'],
        )
