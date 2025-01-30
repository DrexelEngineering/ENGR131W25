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
            keys=['q1-1-mall-parking-calculator', 'q1-2-narrow-path-conditions'],
            options=[['5', '10', '15', 'None'], ['Access is clear.', 'Access blocked!', 'Error', 'No output']],
            descriptions=['You’re creating a program to calculate parking fees at the mall. What will the following function call output?\n```python\ndef calculate_parking_fee(hours):\n    if hours <= 2:\n        return 5\n    elif hours <= 5:\n        return 10\n    else:\n        return 15\n\nprint(calculate_parking_fee(4))\n```', 'The woman who refused to sell her house insists on a narrow path to her home being clear at all times. What will the following code output if `clear_path = False`?\n```python\nif clear_path:\n    print("Access is clear.")\nelse:\n    print("Access blocked!")\n```'],
            points=[1.0, 1.0],
        )
class Question3(TFQuestion):
    def __init__(self):
        super().__init__(
            title=f"True or False",
            style=TFStyle,
            question_number=3,
            keys=['q3-1-house-accessibility', 'q3-2-shop-opening-loops', 'q3-3-escalator-shutdown'],
            descriptions=['The woman’s house can only be accessed if the path is clear. This condition can be checked using an `if` statement.', 'A `for` loop can iterate over a list of shops to print their opening hours.', "In the mall, the `break` statement can stop an escalator's loop when maintenance is required."],
            points=[1.0, 1.0, 1.0],
        )
class Question2(SelectMany):
    def __init__(self):
        super().__init__(
            title=f"Select All That Apply",
            style=MultiSelect,
            question_number=2,
            keys=['q2-1-shop-opening-functions', 'q2-2-mall-escalator-loops'],
            descriptions=['The mall has multiple shops, each with its own opening and closing rules. Which of the following are true about Python functions for this scenario?', 'The mall’s escalators need to run on a schedule. Which of the following are true about `for` and `while` loops for this task?'],
            options=[['A function can take the opening time and closing time as arguments.', 'A function can calculate the total hours a shop is open.', 'A function can return multiple outputs, such as the opening and closing times.', 'A function must include both an `if` block and an `else` block to work.'], ['A `for` loop can iterate over a schedule of hours.', 'A `while` loop can run as long as the escalators are operational.', 'A `for` loop requires a condition to start.', 'A `while` loop cannot include a `break` statement.']],
            points=[2.0, 2.0],
            grade=['parts'],
        )
