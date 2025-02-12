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
            keys=['q1-1-player-inheritance', 'q1-2-quarterback-subclass'],
            options=[['Inheritance allows a class to reuse attributes and methods from another class.', 'Inheritance copies methods from one class to another, but they cannot be modified.', 'Inheritance makes all child classes identical to their parent class.', 'Inheritance only works with built-in Python classes.'], ['`Patrick Mahomes 97 99`', '`Error: Quarterback must define all attributes explicitly`', '`None None None`', '`97 Patrick Mahomes 99`']],
            descriptions=['Which of the following best describes class inheritance in Python?', 'What will the following code output?**\n```python\nclass Player:\n    def __init__(self, name, rating):\n        self.name = name\n        self.rating = rating\n\nclass Quarterback(Player):\n    def __init__(self, name, rating, throwing_power):\n        super().__init__(name, rating)\n        self.throwing_power = throwing_power\n\nqb = Quarterback("Patrick Mahomes", 97, 99)\nprint(qb.name, qb.rating, qb.throwing_power)\n```'],
            points=[1.0, 1.0],
        )
class Question3(TFQuestion):
    def __init__(self):
        super().__init__(
            title=f"True or False",
            style=TFStyle,
            question_number=3,
            keys=['q3-1-base-class', 'q3-2-overriding-methods', 'q3-3-super-method'],
            descriptions=['A base class in Python is a class that other classes inherit from.', 'A child class can override methods from a parent class by redefining them.', 'The `super()` function is required in all child class constructors.'],
            points=[1.0, 1.0, 1.0],
        )
class Question2(SelectMany):
    def __init__(self):
        super().__init__(
            title=f"Select All That Apply",
            style=MultiSelect,
            question_number=2,
            keys=['q2-1-madden-positions', 'q2-2-nfl-inheritance-methods'],
            descriptions=['Which of the following are benefits of using inheritance in an NFL Madden game class structure?', 'Which methods are essential to correctly implement inheritance in an NFL Madden player class?'],
            options=[['Reduces code duplication by reusing attributes.', 'Allows specialized player classes like `Quarterback` or `WideReceiver`.', 'Forces all subclasses to define their own methods separately.', 'Makes it easy to add new player positions with different attributes.'], ['`def __init__(self, name, rating):`', '`super().__init__(name, rating)`', '`class RunningBack(Player):`', '`def inherit_attributes(self):`']],
            points=[2.0, 2.0],
            grade=['parts'],
        )
