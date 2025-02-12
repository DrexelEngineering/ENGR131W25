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
            keys=['q1-1-pokemon-polymorphism', 'q1-2-polymorphism-example'],
            options=[['A subclass always overrides a method from the parent class.', 'Different classes define the same method name but with different behavior.', 'Python automatically converts one class type into another.', 'A class can only inherit from one parent class.'], ['`A Pokémon attacks! A Pokémon attacks!`', '`Pikachu uses Thunderbolt! Charizard uses Flamethrower!`', '`Error: attack() must be defined in the base class`', '`None`']],
            descriptions=['Which of the following best describes polymorphism in Python?', 'What will the following code output?**\n```python\nclass Pokemon:\n    def attack(self):\n        return "A Pokémon attacks!"\n\nclass Pikachu(Pokemon):\n    def attack(self):\n        return "Pikachu uses Thunderbolt!"\n\nclass Charizard(Pokemon):\n    def attack(self):\n        return "Charizard uses Flamethrower!"\n\np1 = Pikachu()\np2 = Charizard()\nprint(p1.attack(), p2.attack())\n```'],
            points=[1.0, 1.0],
        )
class Question3(TFQuestion):
    def __init__(self):
        super().__init__(
            title=f"True or False",
            style=TFStyle,
            question_number=3,
            keys=['q3-1-overriding-methods', 'q3-2-different-methods', 'q3-3-base-class-method'],
            descriptions=['A subclass can override a method from a parent class to provide different behavior.', 'Polymorphism requires methods in different classes to have identical implementations.', 'A method in the base class must always be defined in order for polymorphism to work.'],
            points=[1.0, 1.0, 1.0],
        )
class Question2(SelectMany):
    def __init__(self):
        super().__init__(
            title=f"Select All That Apply",
            style=MultiSelect,
            question_number=2,
            keys=['q2-1-polymorphism-methods'],
            descriptions=['Which of the following statements about polymorphism are true?'],
            options=[['Polymorphism allows different classes to share method names with different implementations.', 'Polymorphism requires a common parent functions for all related classes.', 'A single function can call the same method on different objects.', 'Polymorphism makes it impossible to override methods.']],
            points=[2.0],
            grade=['parts'],
        )
