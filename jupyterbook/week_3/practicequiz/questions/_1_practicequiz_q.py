from pykubegrader.widgets.select_many import MultiSelect, SelectMany
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
            keys=['q1-1-Sport-Car-Engine-Tracking-System', 'q1-2-Default-Fuel-Type-in-Car-Array', 'q1-3-NumPy Basics in Engine Performance Analysis'],
            options=[['np.max()', 'np.size()', 'np.size()', 'np.arange()'], ['It was designed by Ferrari engineers', 'It uses C code under the hood', 'It uses Python code under the hood', 'It uses CUDA to enable GPU acceleration'], ['Creates a 5x5 array filled with zeros.', 'Creates a 5x5 array filled with ones.', 'Creates an array of zeros with shape (5, 5, 5).', 'Returns an error.']],
            descriptions=['Which method would you use to find the max horsepower of a NumPy array representing engine output power as a function of time?', 'Numpy is fast like a race car at matrix multiplication because?', "What does `np.zeros((5, 5))` do in a car's engine monitoring system?"],
            points=[1.0, 1.0, 1.0],
        )
class Question2(SelectMany):
    def __init__(self):
        super().__init__(
            title=f"Select All That Apply",
            style=MultiSelect,
            question_number=2,
            keys=['q2-1-SymPy-Capabilities-in-Performance-Tuning', 'q2-2-Valid-NumPy-Array-Creation-Methods'],
            descriptions=['Which of the following are SymPy capabilities used to model sport car suspension dynamics?', 'Which of the following are valid ways to create a NumPy array for tracking tire pressure?'],
            options=[['Solving equations symbolically.', 'Calculating definite integrals.', 'Performing symbolic differentiation.', 'Generating random numbers.', 'Creating arrays for numerical computation.'], ['np.zeros()', 'np.array([])', 'np.string()', 'np.arange()', 'np.random.random()']],
            points=[2.0, 2.0],
            grade=['parts'],
        )
