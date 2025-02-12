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
            keys=['q1-1-abstraction-definition', 'q1-2-abstract-methods'],
            options=[['A class that defines methods but does not implement them.', 'A way to store data without using classes.', 'A method that forces all subclasses to have different method names.', 'A function that automatically fixes bit flips in software.'], ['The program runs with no errors.', 'The method `apply_brakes` is automatically defined in `obj`.', 'An error occurs because abstract classes cannot be instantiated.', '`obj` will execute `apply_brakes()` with default behavior.']],
            descriptions=['Which of the following best describes abstraction in Python?', 'What will happen if you try to instantiate an abstract class in Python?**\n```python\nfrom abc import ABC, abstractmethod\n\nclass AcceleratorControl(ABC):\n    @abstractmethod\n    def apply_brakes(self):\n        pass\n\nobj = AcceleratorControl()\n```'],
            points=[1.0, 1.0],
        )
class Question3(TFQuestion):
    def __init__(self):
        super().__init__(
            title=f"True or False",
            style=TFStyle,
            question_number=3,
            keys=['q3-1-abstract-class', 'q3-2-subclassing'],
            descriptions=['An abstract class can contain both abstract and non-abstract methods.', 'A subclass of an abstract class must implement all abstract methods unless it is also an abstract class.'],
            points=[1.0, 1.0],
        )
class Question2(SelectMany):
    def __init__(self):
        super().__init__(
            title=f"Select All That Apply",
            style=MultiSelect,
            question_number=2,
            keys=['q2-1-toyota-abstraction-failure', 'q2-2-abstraction-methods'],
            descriptions=['How could better abstraction have helped Toyota prevent accelerator failures?', 'Which of the following statements about abstract methods are true?'],
            options=[['Abstract base classes could have enforced proper handling of acceleration overrides.', 'Abstract methods could have required implementing fail-safe mechanisms in all subclasses.', 'Keeping all code in one huge function would have been more reliable.', 'Reducing dependencies between software components could have made debugging easier.'], ['An abstract method **must** be implemented by subclasses.', 'Abstract methods **can** have a default implementation.', 'Abstract methods **cannot** take arguments.', 'Abstract methods **must** be decorated with `@abstractmethod`.']],
            points=[2.0, 2.0],
            grade=['parts'],
        )
