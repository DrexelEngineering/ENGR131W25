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
            keys=['q1-1-headis-player-class', 'q1-2-player-initialization', 'q1-3-method-behavior'],
            options=[['A class is a function that returns player statistics.', 'A class is a data structure that stores player scores in a list.', 'A class is a blueprint for creating player objects with attributes like speed and skill.', 'A class is a loop that continuously tracks player movements.'], ['It prints the player’s attributes.', 'It defines the behavior of the player.', 'It initializes the attributes of a new player instance.', 'It is an optional function used only in advanced Python programming.'], ['A method is a variable inside a class.', 'A method defines behaviors for objects created from the class.', 'A method is only used to store values.', 'A method is only available in Python version 3.10+.']],
            descriptions=['Which of the following best describes a Python class representing a Headis player?', 'What does the `__init__` method do in a class like `HeadisPlayer`?', 'Which of the following best describes a method in a class like `HeadisPlayer`?'],
            points=[1.0, 1.0, 1.0],
        )
class Question3(TFQuestion):
    def __init__(self):
        super().__init__(
            title=f"True or False",
            style=TFStyle,
            question_number=3,
            keys=['q3-1-instance-vs-class', 'q3-2-headis-function-classes'],
            descriptions=['An instance of a class is a specific object created from that class.', 'Classes and functions can be used interchangeably  in  Python'],
            points=[1.0, 1.0],
        )
class Question2(SelectMany):
    def __init__(self):
        super().__init__(
            title=f"Select All That Apply",
            style=MultiSelect,
            question_number=2,
            keys=['q2-1-headis-game-rules'],
            descriptions=['Which of the following are true about Python classes in the context of a Headis game?'],
            options=[['A class can represent the Headis game itself, with players as objects.', 'Each player can be an instance of the `HeadisPlayer` class.', 'A class must always have a `__str__` method to work.', 'A class can define methods for actions like "hit ball" and "jump."']],
            points=[2.0],
        )
