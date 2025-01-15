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
            keys=['q1-1-what-calculates-derivatives', 'q1-2-what-calculates-integrals', 'q1-3-what-calculates-limits'],
            options=[['`integrate()`', '`diff()`', '`solve()`', '`limit()`'], ['`diff()`', '`integrate()`', '`solve()`', '`expand()`'], ['The behavior of a function as it approaches a value', 'The area under a curve', 'The derivative of a function', 'The roots of a function']],
            descriptions=['Which SymPy function calculates derivatives?', 'Which SymPy function calculates integrals?', 'What does the `limit()` function calculate?'],
            points=[1.0, 1.0, 1.0],
        )
class Question3(TFQuestion):
    def __init__(self):
        super().__init__(
            title=f"True or False",
            style=TFStyle,
            question_number=3,
            keys=['q3-1-linsolve-non-linear-equations', 'q3-2-sympy-solves-nonlinear-equations', 'q3-3-dsolve-function', 'q3-4-dsolve-function-numpy'],
            descriptions=["SymPy's `linsolve()` function can solve nonlinear equations.", "SymPy's `roots()` function can find roots of a polynomial.", 'The `dsolve()` function is used for solving differential equations.', 'NumPy can use symbols to solve mathematical expressions.'],
            points=[1.0, 1.0, 1.0, 1.0],
        )
class Question2(SelectMany):
    def __init__(self):
        super().__init__(
            title=f"Select All That Apply",
            style=MultiSelect,
            question_number=2,
            keys=['q2-1-what-is-the-diff-function-used-for-in-sympy', 'q2-2-what-is-the-integrate-function-used-for-in-sympy'],
            descriptions=["What can SymPy's `diff()` function be used for? (Select all that apply)", "What are some uses of SymPy's `integrate()` function? (Select all that apply)"],
            options=[['Calculate the rate of change of a function', 'Find the slope of a curve', 'Solve equations', 'Calculate higher-order derivatives'], ['Compute the area under a curve', 'Calculate the volume of a solid', 'Find the rate of change of a function', 'Solve for roots of equations']],
            points=[2.0, 2.0],
            grade=['parts'],
        )
