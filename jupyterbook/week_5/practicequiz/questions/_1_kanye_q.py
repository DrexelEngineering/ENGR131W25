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
            keys=['q1-1-kanye-function-definition', 'q1-2-args-kwargs-kanye'],
            options=[['Functions in Python must start with `"Kanye_"` to work.', 'Functions must be declared with the `def` keyword.', 'Python automatically recognizes functions even if you don’t use `def`.', 'Functions can only return string values.'], ['`*args`', '`**kwargs`', 'Both `*args` and `**kwargs`', 'Neither `*args` nor `**kwargs`']],
            descriptions=['Kanye insists that functions should be named after him. What is the correct way to define a function in Python?', 'Kanye sometimes interrupts himself mid-sentence, adding multiple unexpected thoughts. How can we write a function that accepts any number of arguments?'],
            points=[1.0, 1.0],
        )
class Question3(TFQuestion):
    def __init__(self):
        super().__init__(
            title=f"True or False",
            style=TFStyle,
            question_number=3,
            keys=['q3-1-function-kanye-scope', 'q3-2-args-order-kanye', 'q3-3-optional-arguments-kanye'],
            descriptions=['Kanye says, "Everything I say should be accessible forever." Does that mean variables inside a function are accessible globally?', 'Kanye believes order doesn’t matter in music. But in Python, do positional arguments always have to come before `*args`?', 'Optional arguments must have default values.'],
            points=[1.0, 1.0, 1.0],
        )
class Question2(SelectMany):
    def __init__(self):
        super().__init__(
            title=f"Select All That Apply",
            style=MultiSelect,
            question_number=2,
            keys=['q2-1-return-multiple-kanye-thoughts', 'q2-2-kwargs-usage-kanye'],
            descriptions=['Kanye gives multiple opinions in a single interview. What’s true about Python function return values?', 'Kanye sometimes adds extra context to his statements. What’s true about `**kwargs` in Python functions?'],
            options=[['A function can return multiple values using tuples.', 'The `return` statement is optional in Python because Kanye said so.', 'A function can only return one value.', 'A function can return different data types at the same time.'], ['`**kwargs` allows passing multiple keyword arguments into a function.', '`**kwargs` must always be the last argument in the function signature.', '`**kwargs` arguments are accessed as a dictionary inside the function.', '`**kwargs` must be used if a function has more than two parameters.']],
            points=[2.0, 2.0],
            grade=['parts'],
        )
