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
            keys=['q1-1-Atomic-Number-Storage', 'q1-2-Atomic-Mass-Storage'],
            options=[['Float', 'String', 'Integer', 'List'], ['Integer', 'Float', 'String', 'Tuple']],
            descriptions=['Which Python datatype would be most appropriate for storing the atomic number of an element?', 'If you needed to store the atomic mass of an element (e.g., Carbon-12 as 12.011), which datatype would you use?'],
            points=[1.0, 1.0],
        )
class Question3(TFQuestion):
    def __init__(self):
        super().__init__(
            title=f"Select if the statement is True or False",
            style=TFStyle,
            question_number=3,
            keys=['q3-1-Dictionary-Element-Properties', 'q3-2-Proton-Storage'],
            descriptions=['A dictionary would be the most appropriate datatype for storing multiple properties of a single element (symbol, atomic number, atomic mass, etc.).', 'You would use a float to store the number of protons in an atom.'],
            points=[1.0, 1.0],
        )
class Question2(SelectMany):
    def __init__(self):
        super().__init__(
            title=f"Select All That Apply",
            style=MultiSelect,
            question_number=2,
            keys=['q2-1-Electron-Configuration-Storage', 'q2-2-Element-Properties-Storage'],
            descriptions=['Electron orbital configurations are defined using 1s2 2s2 2p6 notation what are viable data types for storing this information?', 'If you have an element what data types might you use to describe its attributes in python?'],
            options=[['String', 'List', 'Tuple', 'Integer'], ['dictionary', 'word', 'list', 'fuzzyint', 'tuple', 'bit', 'float', 'char', 'string']],
            points=[2.0, 2.0],
            grade=['parts'],
        )
