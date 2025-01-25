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
            keys=['q1-1-Immutable-Properties', 'q1-2-List-Usage-Materials'],
            options=[['To make the program run faster', 'Because atomic properties like atomic number and mass are immutable physical constants', 'To save memory in the program', 'Because tuples are easier to write than lists'], ['Storing the atomic weights of elements', 'Recording a sequence of heat treatment steps for an alloy', 'Maintaining the electron configuration of noble gases', 'Tracking the speed of light in different materials']],
            descriptions=['Why are atomic properties stored as tuples in materials science programming?', 'Which scenario best demonstrates appropriate use of lists in materials design?'],
            points=[1.0, 1.0],
        )
class Question3(TFQuestion):
    def __init__(self):
        super().__init__(
            title=f"Select if the statement is True or False",
            style=TFStyle,
            question_number=3,
            keys=['q3-1-Mutability-Understanding'],
            descriptions=["In materials science programming, you should use lists to store fundamental physical constants like Avogadro's number or Planck's constant."],
            points=[1.0],
        )
class Question2(SelectMany):
    def __init__(self):
        super().__init__(
            title=f"Select All That Apply",
            style=MultiSelect,
            question_number=2,
            keys=['q2-1-Mutable-Properties', 'q2-2-Immutable-Constants'],
            descriptions=['Which of these materials properties or parameters would be appropriately stored in a list?', 'Which of these materials properties should be stored in tuples?'],
            options=[['Processing temperatures for heat treatment', 'Processing times for each manufacturing step', 'Selected alloying elements for a new material design', 'The atomic number of carbon'], ['Crystal structure of pure elements at standard conditions', 'Atomic mass of isotopes', 'Melting points of pure elements', 'Current material cost from suppliers']],
            points=[2.0, 2.0],
            grade=['parts'],
        )
