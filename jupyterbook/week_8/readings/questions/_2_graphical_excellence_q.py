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
            keys=['q1-1-visualization-principles', 'q1-2-color-usage', 'q1-3-visualization-errors', 'q1-4-software-selection'],
            options=[['To make figures as colorful as possible.', 'To accurately and efficiently communicate data insights.', 'To create abstract artistic representations of data.', 'To use the most complex software available.'], ['It makes figures look more aesthetically pleasing.', 'It enhances memorability and helps distinguish data categories.', 'It should be avoided due to accessibility concerns.', 'It is only useful for digital formats, not print.'], ['Using only black and white figures.', 'Using bar plots to represent means without showing distribution.', 'Avoiding any use of graphical elements.', 'Providing too much uncertainty in figures.'], ['Use only basic spreadsheet programs for all figures.', 'Choose a tool that allows flexibility and customization of visuals.', 'Avoid learning new software and rely only on default settings.', 'Only use proprietary software for scientific figures.']],
            descriptions=['What is the primary goal of effective data visualization?', 'Why is color an important tool in data visualization?', 'Which of the following is a common issue found in scientific visualizations?', 'What is the best approach when selecting a tool for data visualization?'],
            points=[1.0, 1.0, 1.0, 1.0],
        )
class Question3(TFQuestion):
    def __init__(self):
        super().__init__(
            title=f"True or False",
            style=TFStyle,
            question_number=3,
            keys=['q3-1-diagram-first', 'q3-2-black-and-white', 'q3-3-data-ink-ratio', 'q3-4-bar-chart-usage'],
            descriptions=['Before making a figure, it is best to determine the key message before selecting the visualization style.', 'Black-and-white figures are always more effective than color figures.', 'A higher data-ink ratio means more of the figure is dedicated to displaying actual data rather than unnecessary design elements.', 'Bar charts are always the best way to represent grouped data means.'],
            points=[1.0, 1.0, 1.0, 1.0],
        )
class Question2(SelectMany):
    def __init__(self):
        super().__init__(
            title=f"Select All That Apply",
            style=MultiSelect,
            question_number=2,
            keys=['q2-1-visualization-best-practices', 'q2-2-figure-geometries', 'q2-3-small-multiples', 'q2-4-infographic-benefits'],
            descriptions=['Which of the following are best practices for effective data visualization?', 'Which of the following statements about figure geometries are true?', 'What are the benefits of using small multiples (paneling) in visualization?', 'Why should researchers consider using infographics in their publications?'],
            options=[['Prioritize the message before selecting the figure type.', 'Always use 3D bar plots for better aesthetics.', 'Include uncertainty measures when applicable.', 'Keep figure captions detailed and self-explanatory.'], ['Different geometries (bar, scatter, heatmap) should be selected based on the data type.', 'Scatterplots should only be used when there is no visible trend in the data.', 'Heatmaps can effectively display large datasets with patterns over time.', 'Histograms are useful for visualizing numerical data distributions.'], ['They allow for direct comparisons across different variables.', 'They reduce the need for legends in figures.', 'They make it easier to compare changes over time.', 'They simplify complex datasets into a single view.'], ['Infographics improve memorability of visual content.', 'They replace the need for any written descriptions.', 'They can blend multiple elements such as text, images, and diagrams effectively.', 'Infographics are only useful for non-scientific audiences.']],
            points=[2.0, 2.0, 2.0, 2.0],
            grade=['parts'],
        )
