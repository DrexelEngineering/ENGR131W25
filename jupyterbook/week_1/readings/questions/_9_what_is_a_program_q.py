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
            keys=['q1-1-What-is-a-Program', 'q1-2-Program-Input', 'q1-3-Purpose-of-Loops', 'q1-4-Art-of-the-Breakdown'],
            options=[['A series of random operations performed by a computer.', 'A sequence of instructions for a computer to execute.', 'A list of files stored on a computer.', 'A method for designing bridges and reactors.'], ['Typing on a keyboard.', 'streaming heat maps from sensors.', 'Printing results to the screen.', 'Retrieving data from a smartwatch.'], ['To prevent errors in a program.', 'To repeat actions with slight variations.', 'To make the program visually appealing.', 'To store large amounts of data.'], ['Writing as many lines of code as possible.', 'Solving the biggest part of a problem first.', 'Breaking down large problems into smaller, manageable tasks.', 'Running multiple programs at the same time.']],
            descriptions=['What is a program?', 'Which of the following is NOT an example of program input?', 'What is the primary purpose of loops in programming?', 'Which of these best describes the “art of the breakdown” in programming?'],
            points=[1.0, 1.0, 1.0, 1.0],
        )
class Question2(TFQuestion):
    def __init__(self):
        super().__init__(
            title=f"Select if the statement is True or False",
            style=TFStyle,
            question_number=2,
            keys=['q2-1-Program-recipe', 'q2-2-Output-keyboard', 'q2-3-Conditional-Execution', 'q2-4-Repetition', 'q2-5-Relevance of Programming'],
            descriptions=['A program is like a recipe for a computer, consisting of precise instructions.', 'Output refers to the process of getting data from a keyboard or a file.', 'Conditional execution allows programs to make decisions based on certain conditions.', 'Repetition in programming eliminates the need for performing the same task multiple times.', 'Programming is only useful for computer science and has little relevance to engineering fields like civil or biomedical engineering.'],
            points=[1.0, 1.0, 1.0, 1.0, 1.0],
        )
