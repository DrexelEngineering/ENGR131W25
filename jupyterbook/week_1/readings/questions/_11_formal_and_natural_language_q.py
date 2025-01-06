from pykubegrader.widgets.select_many import MultiSelect, SelectMany
from pykubegrader.widgets.true_false import TFQuestion, TFStyle
from pykubegrader.widgets.multiple_choice import MCQuestion, MCQ
import pykubegrader.initialize
import panel as pn

pn.extension()

class Question1(MCQuestion):
    def __init__(self):
        super().__init__(
            title=f"What is a primary difference between natural and formal languages?",
            style=MCQ,
            question_number=1,
            keys=['q1-1-Natural-v-Formal Languages', 'q1-2-Examples-of-Languages', 'q1-3-Tokens-in-Formal-Languages', 'q1-4-Python-Print-Function'],
            options=[['Natural languages are concise, while formal languages are verbose.', 'Formal languages are designed to be unambiguous, while natural languages rely on context.', 'Formal languages evolve naturally over time.', 'Natural languages have strict syntax rules like formal languages.'], ['Klingon', 'English', 'Python', 'Emoji'], ['Pieces of information passed between computers.', 'The building blocks of a program, such as words, numbers, and symbols.', 'Synonyms for syntax rules.', 'The process of understanding the structure of code.'], ['Displays the literal text `"The other shoe fell."` on the screen.', 'Displays a figurative message about something falling.', 'Stores the text as a variable.', 'Executes an error because of ambiguity.']],
            descriptions=['What is a primary difference between natural and formal languages?', 'Which of the following is an example of a formal language?', 'What are tokens in a formal language?', 'In Python, what does the following line of code do? `print("The other shoe fell.")`'],
            points=[2.0, 2.0, 2.0, 2.0],
        )
class Question2(MCQuestion):
    def __init__(self):
        super().__init__(
            title=f"Syntax in programming refers to the ______ of a program.",
            style=MCQ,
            question_number=2,
            keys=['q2-1-Programming-Syntax', 'q2-2-Parsing-in-Programming'],
            options=[['Speed', 'Structure', 'Ambiguity', 'Parsing'], ['Guessing the intent of ambiguous statements.', 'Running a program to find syntax errors.', 'Breaking a sentence or statement into tokens and understanding its structure.', 'Removing redundant tokens from code.']],
            descriptions=['Syntax in programming refers to the ______ of a program.', 'Parsing is the process of ______.'],
            points=[1.0, 1.0],
        )
class Question4(TFQuestion):
    def __init__(self):
        super().__init__(
            title=f'Formal languages like Python are designed to rely on context to resolve ambiguity.',
            style=TFStyle,
            question_number=4,
            keys=['q4-1-Context-in-Formal-Languages', 'q4-2-parsing-in-natural-languages', 'q4-3-Programming-Syntax-Errors', 'q4-4-error-tolerance', 'q4-5-formal-languages-engineering'],
            descriptions=['Formal languages like Python are designed to rely on context to resolve ambiguity.', 'Parsing in natural languages happens subconsciously, while parsing in formal languages requires explicit effort.', 'A missing comma in a Python program can cause a syntax error.', 'Both natural and formal languages are equally tolerant of errors.', 'Formal languages like Python are valuable for solving engineering problems systematically.'],
            points=[1.0, 1.0, 1.0, 1.0, 1.0],
        )
class Question3(SelectMany):
    def __init__(self):
        super().__init__(
            title=f'Which of the following are features of formal languages?',
            style=MultiSelect,
            question_number=3,
            keys=['q3-1-Features-of-Formal-Languages'],
            descriptions=['Which of the following are features of formal languages?'],
            options=[['Ambiguity', 'Conciseness', 'Strict syntax rules', 'Reliance on redundancy']],
            points=[2.0],
            grade=['parts'],
        )
