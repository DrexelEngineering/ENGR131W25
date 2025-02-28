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
            keys=['q1-1-what-is-scikit-image-used-for', 'q1-2-what-type-of-data-structure-does-scikit-image-use-to-represent-images', 'q1-4-what-coordinate-convention-does-scikit-image-use-for-images', 'q1-5-what-does-image-segmentation-do-in-scikit-image', 'q1-6-how-to-do-edge-detection-in-scikit-image'],
            options=[['Image processing and analysis', 'Numerical computations', 'Creating 3D graphics', 'Audio signal processing'], ['Python dictionaries', 'NumPy arrays', 'Pandas DataFrames', 'Python lists'], ['Cartesian coordinates with (0, 0) at the bottom-left corner', 'Cartesian coordinates with (0, 0) at the top-left corner', 'Matrix-style indexing with (0, 0) at the top-left corner', 'Polar coordinates with the origin at the center of the image'], ['It labels pixels in an image to identify objects of interest.', 'It compresses image file sizes.', 'It converts grayscale images to color.', 'It generates 3D models of images.'], ['`feature.canny`', '`filters.threshold_otsu`', '`io.imread`', '`exposure.adjust_gamma`']],
            descriptions=['What is scikit-image primarily used for?', 'What type of data structure does scikit-image use to represent images?', 'Which coordinate convention does `scikit-image` use for images?', 'What does image segmentation do in scikit-image?', 'Which function in scikit-image is used for edge detection?'],
            points=[2.0, 2.0, 2.0, 2.0, 2.0],
        )
class Question3(TFQuestion):
    def __init__(self):
        super().__init__(
            title=f"True or False",
            style=TFStyle,
            question_number=3,
            keys=['q3-1-images-in-scikit-image-are-stored-as-numpy-arrays-TF', 'q3-2-the-io-submodule-in-scikit-image-is-used-for-reading-and-writing-images-TF', 'q3-3-scikit-image-is-designed-specifically-for-3d-image-analysis-TF', 'q3-4-the-origin-0-0-in-scikit-image-images-is-located-at-the-bottom-left-corner-TF', 'q3-5-scikit-image-color-images-are-represented-as-arrays-with-an-extra-dimension-for-rgb-channels-TF', 'q3-6-edge-detection-works-perfectly-for-all-segmentation-problems-TF'],
            descriptions=['Images in scikit-image are stored as NumPy arrays.', 'The `io` submodule in scikit-image is used for reading and writing images.', 'Scikit-image is designed specifically for 3D image analysis.', 'The origin (0, 0) in `scikit-image` images is located at the bottom-left corner.', 'In `scikit-image`, color images are represented as arrays with an extra dimension for RGB channels.', 'Edge detection works perfectly for all segmentation problems.'],
            points=[1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
        )
class Question2(SelectMany):
    def __init__(self):
        super().__init__(
            title=f"Select All That Apply",
            style=MultiSelect,
            question_number=2,
            keys=['q2-1-which-of-the-following-are-key-functionalities-of-numpy-arrays-in-scikit-image', 'q2-2-which-of-the-following-image-properties-can-be-calculated-using-numpy-arrays-in-scikit-image', 'q2-3-which-of-the-following-functionalities-are-supported-by-scikit-image', 'q2-4-which-of-the-following-submodules-belong-to-scikit-image', 'q2-5-what-are-challenges-in-image-segmentation'],
            descriptions=['Which of the following are key functionalities of NumPy arrays in `scikit-image`? (Select all that apply)', 'Which of the following image properties can be calculated using NumPy arrays in `scikit-image`? (Select all that apply)', 'Which of the following functionalities are supported by scikit-image? (Select all that apply)', 'Which of the following submodules belong to scikit-image? (Select all that apply)', 'What are challenges in image segmentation? (Select all that apply)'],
            options=[['Efficiently storing image data', 'Applying mathematical operations to images', 'Representing images as dictionaries', 'Enabling pixel-wise manipulations'], ['Image dimensions', 'Intensity range', 'Average brightness', 'Pixel coordinates in polar form'], ['Loading images from files', 'Applying filters', 'Visualizing images with matplotlib', 'Performing mathematical operations on images'], ['`io`', '`filters`', '`data`', '`numpy`'], ['Uneven lighting in images', 'Similar intensity levels for objects and background', 'Large file sizes', 'Small gaps in detected edges']],
            points=[3.0, 3.0, 3.0, 3.0, 3.0],
            grade=['parts'],
        )
