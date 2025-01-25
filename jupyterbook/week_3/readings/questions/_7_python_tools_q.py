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
            keys=['q1-1-what-is-numpy-used-for', 'q1-2-which-is-pandas-most-suitable-for', 'q1-3-what-is-matplotlib-used-for'],
            options=[['Handling symbolic mathematics', 'Numerical operations on large arrays and matrices', 'Creating static visualizations', 'Statistical analysis and modeling'], ['Symbolic mathematics', 'Solving differential equations', 'Handling and analyzing structured data', 'Visualizing complex plots'], ['Solving optimization problems', 'Building statistical models', 'Creating visualizations such as plots and graphs', 'Performing symbolic computations']],
            descriptions=['What is NumPy primarily used for?', 'Which of the following tasks is Pandas most suitable for?', 'What is Matplotlib primarily used for?'],
            points=[1.0, 1.0, 1.0],
        )
class Question3(TFQuestion):
    def __init__(self):
        super().__init__(
            title=f"True or False",
            style=TFStyle,
            question_number=3,
            keys=['q3-1-sympy-and-viz', 'q3-2-ml-libraries', 'q3-3-opencv-TF'],
            descriptions=['SymPy is primarily used for creating visualizations.', 'Scikit-learn is a library designed for machine learning tasks such as classification and regression.', 'OpenCV is primarily used for symbolic mathematics.'],
            points=[1.0, 1.0, 1.0],
        )
class Question2(SelectMany):
    def __init__(self):
        super().__init__(
            title=f"Select All That Apply",
            style=MultiSelect,
            question_number=2,
            keys=['q2-1-match-libraries-to-purposes', 'q2-2-numpy-or-sympy'],
            descriptions=['Match the following libraries with their primary purposes', 'Which of the following libraries are used for numerical or symbolic computations?'],
            options=[['NumPy: Symbolic mathematics', 'Pandas: Handling structured data', 'SciPy: Advanced scientific computing', 'Matplotlib: Creating visualizations'], ['NumPy', 'SymPy', 'OpenCV', 'Matplotlib']],
            points=[2.0, 2.0],
            grade=['parts'],
        )
