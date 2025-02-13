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
            keys=['q1-1-multiple-inheritance-definition', 'q1-2-rolex-multiple-parents'],
            options=[['- A class that inherits from more than one parent class.', '- A class that cannot override methods from a parent class.', '- A way to prevent subclasses from inheriting methods.', '- A method for handling time zone calculations.'], ['- `Displaying local time.`', '- `Displaying GMT time.`', '- `Error: Method resolution conflict.`', '- `None`']],
            descriptions=['Which of the following best describes multiple inheritance in Python?', 'What will the following code output?**\n```python\nclass TimeDisplay:\n    def show_time(self):\n        return "Displaying local time."\n\nclass GMTFunctionality:\n    def show_time(self):\n        return "Displaying GMT time."\n\nclass RolexGMT(TimeDisplay, GMTFunctionality):\n    pass\n\nwatch = RolexGMT()\nprint(watch.show_time())\n```'],
            points=[1.0, 1.0],
        )
class Question3(TFQuestion):
    def __init__(self):
        super().__init__(
            title=f"True or False",
            style=TFStyle,
            question_number=3,
            keys=['q3-1-diamond-problem', 'q3-2-mro-sequence', 'q3-3-single-inheritance-requirement'],
            descriptions=["Python's method resolution order (MRO) helps resolve method conflicts in multiple inheritance.", 'In multiple inheritance, Python follows a strict order to check for methods in parent classes.', 'Python does not allow a class to inherit from more than one parent class.'],
            points=[1.0, 1.0, 1.0],
        )
class Question2(SelectMany):
    def __init__(self):
        super().__init__(
            title=f"Select All That Apply",
            style=MultiSelect,
            question_number=2,
            keys=['q2-1-rolex-inheritance-benefits', 'q2-2-rolex-diamond-mix'],
            descriptions=['What are the benefits of using multiple inheritance in the design of a Rolex GMT class?', 'Which of the following would be valid parent classes for a Rolex GMT watch model using multiple inheritance?'],
            options=[['- Combines functionalities from different classes (e.g., time display and GMT tracking).', '- Allows the class to inherit and override methods from multiple sources.', '- Ensures that only one parent class can contribute methods.', '- Simplifies code reuse by leveraging existing class behaviors.'], ['- `class Timekeeping:`', '- `class LuxuryBrand:`', '- `class BatteryPowered:`', '- `class GoldPlated:`']],
            points=[2.0, 2.0],
            grade=['parts'],
        )
