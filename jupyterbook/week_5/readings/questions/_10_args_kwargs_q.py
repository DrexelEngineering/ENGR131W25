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
            keys=['q1-1-brawler-abilities', 'q1-2-brawler-statistics'],
            options=[['Super Gadget Passive Ability', 'Super\\nGadget\\nPassive Ability', "['Super', 'Gadget', 'Passive Ability']", 'None'], ["Shelly {'health': 3600, 'power': 10}", 'Shelly (3600, 10)', "Shelly ['health', 'power']", 'Error']],
            descriptions=['What will the following function output?**\n```python\ndef show_abilities(*args):\nfor ability in args:\n    print(ability)\n\nshow_abilities("Super", "Gadget", "Passive Ability")\n```', 'What will the following function output when called as shown?**\n```python\ndef brawler_stats(name, **kwargs):\nprint(name)\nprint(kwargs)\n\nbrawler_stats("Shelly", health=3600, power=10)\n```'],
            points=[1.0, 1.0],
        )
class Question3(TFQuestion):
    def __init__(self):
        super().__init__(
            title=f"True or False",
            style=TFStyle,
            question_number=3,
            keys=['q3-1-args-order', 'q3-2-unpacking-dictionaries', 'q3-3-kwargs-ordering'],
            descriptions=['In a function definition, `*args` must appear before `**kwargs` in the argument list.', 'The `**` operator can unpack a dictionary into a function as keyword arguments.', 'You can pass positional arguments after keyword arguments when calling a function with `**kwargs`.'],
            points=[1.0, 1.0, 1.0],
        )
class Question2(SelectMany):
    def __init__(self):
        super().__init__(
            title=f"Select All That Apply",
            style=MultiSelect,
            question_number=2,
            keys=['q2-1-brawler-args', 'q2-2-brawler-kwargs'],
            descriptions=['Which of the following are true about `*args` in Python?', 'Which of the following are true about `**kwargs` in Python?'],
            options=[['`*args` allows you to pass a variable number of positional arguments to a function.', 'The `*` symbol is required to unpack arguments passed as a list or tuple.', 'You can only use one `*args` in a function definition.', '`*args` automatically converts positional arguments into a dictionary.'], ['`**kwargs` allows passing a variable number of keyword arguments to a function.', 'The `**` symbol is required to unpack a dictionary into keyword arguments.', 'You can only use one `**kwargs` in a function definition.', '`**kwargs` converts arguments into a tuple.']],
            points=[2.0, 2.0],
            grade=['parts'],
        )
