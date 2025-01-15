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
            keys=['q1-1-Why-is-NumPy-faster-than-Python-lists-for-numerical-computations', 'q1-2-characteristics-of-NumPy-arrays', 'q1-3-shape-of-a-NumPy-array'],
            options=[['NumPy arrays are implemented in Python', 'NumPy uses efficient C-based implementation for arrays', 'NumPy arrays are immutable', 'NumPy uses machine learning techniques'], ['Arrays can store elements of mixed types', 'Arrays have a fixed size after creation', 'Arrays cannot perform mathematical operations', 'Arrays are always one-dimensional'], ['`.shape`', '`.ndim`', '`.dtype`', '`.size`']],
            descriptions=['Why is NumPy faster than Python lists for numerical computations?', 'Which of the following is a characteristic of NumPy arrays?', 'Which attribute would you use to find the shape of a NumPy array?'],
            points=[1.0, 1.0, 1.0],
        )
class Question3(TFQuestion):
    def __init__(self):
        super().__init__(
            title=f"True or False",
            style=TFStyle,
            question_number=3,
            keys=['q3-1-Numpy-basics-mutibility', 'q3-2-NumPy-basics-broadcasting', 'q3-3-NumPy-basics-sort'],
            descriptions=['NumPy arrays are mutable, meaning their elements can be modified.', 'Broadcasting in NumPy allows operations between arrays of different shapes.', 'The `np.sort()` function modifies the original array in place by default.'],
            points=[1.0, 1.0, 1.0],
        )
class Question2(SelectMany):
    def __init__(self):
        super().__init__(
            title=f"Select All That Apply",
            style=MultiSelect,
            question_number=2,
            keys=['q2-1-preallocating-memory-in-numpy', 'q2-2-element-wise-operations-in-numpy'],
            descriptions=['Which of the following methods are used for preallocating memory in NumPy?', 'Which of the following operations can be performed element-wise in NumPy?'],
            options=[['`np.zeros()`', '`np.ones()`', '`np.random()`', '`np.empty()`'], ['Addition', 'Subtraction', 'Multiplication', 'Integration']],
            points=[2.0, 2.0],
            grade=['parts'],
        )
