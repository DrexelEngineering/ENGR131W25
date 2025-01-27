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
            keys=['q1-1-solar-panel-monitoring', 'q1-2-# **You’re analyzing wind turbine efficiency data. What happens if a `while` loop is used to monitor wind speeds but lacks a `break` statement in its logic?**'],
            options=[['Below Optimal Output', 'Optimal Solar Output', 'Error', 'No output'], ['The loop runs indefinitely.', 'The loop exits automatically after one iteration.', 'The loop will execute only the first statement inside it.', 'The program raises a syntax error.']],
            descriptions=['You’re designing a solar panel monitoring system. What will the following code output if `sunlight_hours = 9`?\n```python\nif sunlight_hours > 8:\n    print("Optimal Solar Output")\nelse:\n    print("Below Optimal Output")\n```', 'You’re analyzing wind turbine efficiency data. What happens if a `while` loop is used to monitor wind speeds but lacks a `break` statement in its logic?'],
            points=[1.0, 1.0],
        )
class Question3(TFQuestion):
    def __init__(self):
        super().__init__(
            title=f"True or False",
            style=TFStyle,
            question_number=3,
            keys=['q3-1-# **An air quality monitoring system can use an `if` statement to evaluate conditions, such as whether particulate matter exceeds a safe threshold.**', 'q3-2-wind-speed-loop', 'q3-3-solar-battery-break'],
            descriptions=['An air quality monitoring system can use an `if` statement to evaluate conditions, such as whether particulate matter exceeds a safe threshold.', 'A `for` loop can be used to iterate over a sequence of wind speed measurements in a wind farm.', 'In a solar battery management system, the `break` statement can be used to stop a loop once the battery is fully charged.'],
            points=[1.0, 1.0, 1.0],
        )
class Question2(SelectMany):
    def __init__(self):
        super().__init__(
            title=f"Select All That Apply",
            style=MultiSelect,
            question_number=2,
            keys=['q2-1-# **You’re implementing logic for managing battery charging based on voltage levels. Which of the following statements about Python’s `if-else` are true?**', 'q2-2-hydro-turbine-loops'],
            descriptions=['You’re implementing logic for managing battery charging based on voltage levels. Which of the following statements about Python’s `if-else` are true?', 'You’re writing a program to monitor a hydro turbine’s performance. Which of the following are valid loop structures in Python for repeating tasks?'],
            options=[['An `else` block is optional.', 'You can use multiple `elif` conditions to handle different voltage ranges.', 'An `if` block must always have an `else` block.', 'The `if` statement evaluates conditions to determine which code block to execute.'], ['`for` loops.', '`while` loops.', '`do-while` loops.', '`foreach` loops.']],
            points=[2.0, 2.0],
            grade=['parts'],
        )
