from pykubegrader.widgets.select_many import MultiSelect, SelectMany
from pykubegrader.widgets.true_false import TFQuestion, TFStyle
from pykubegrader.widgets.multiple_choice import MCQuestion, MCQ
import pykubegrader.initialize
import panel as pn

pn.extension()

class Question2(MCQuestion):
    def __init__(self):
        super().__init__(
            title=f"Select the Best Answer",
            style=MCQ,
            question_number=2,
            keys=['q2-1-train-test-split', 'q2-2-standard-scaler', 'q2-3-one-hot-encoder', 'q2-4-linear-regression', 'q2-5-random-forest', 'q2-6-svc-default-kernel', 'q2-7-model-evaluation', 'q2-8-pipeline-usage'],
            options=[['`sklearn.model_selection`', '`sklearn.metrics`', '`sklearn.preprocessing`', '`sklearn.decomposition`'], ['`MinMaxScaler`', '`StandardScaler`', '`Normalizer`', '`Binarizer`'], ['`LabelEncoder`', '`OneHotEncoder`', '`OrdinalEncoder`', '`FeatureHasher`'], ['`sklearn.svm`', '`sklearn.linear_model`', '`sklearn.tree`', '`sklearn.ensemble`'], ['Bagging', 'Boosting', 'Stacking', 'Voting'], ['Linear', 'Polynomial', 'RBF', 'Sigmoid'], ['`confusion_matrix`', '`train_test_split`', '`fit_transform`', '`PCA`'], ['To chain multiple transformers and estimators.', 'To visualize decision trees.', 'To import datasets.', 'To calculate feature importance.']],
            descriptions=['Which module contains the `train_test_split` function?', 'Which of the following scales features to zero mean and unit variance?', 'Which class is used for one-hot encoding categorical variables?', 'Which module contains `LinearRegression`?', 'Which ensemble method is used in Random Forest?', 'What is the default kernel for `SVC` in scikit-learn?', 'Which of the following is used to evaluate model performance?', 'What is the primary purpose of using pipelines in scikit-learn?'],
            points=[1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
        )
class Question1(TFQuestion):
    def __init__(self):
        super().__init__(
            title=f"True or False",
            style=TFStyle,
            question_number=1,
            keys=['q1-1-scikit-learn-import', 'q1-2-train-test-split', 'q1-3-standard-scaler', 'q1-4-feature-selection', 'q1-5-knn-classifier', 'q1-6-random-forest', 'q1-7-svc-kernel', 'q1-8-cross-validation', 'q1-9-pipeline'],
            descriptions=['The correct way to import scikit-learn is: `import scikit-learn as skl`.', '`train_test_split` is used to split data into training and testing sets.', '`StandardScaler` scales features by subtracting the mean and scaling to unit variance.', 'Scikit-learn has built-in methods for feature selection.', 'K-Nearest Neighbors is a supervised learning algorithm in scikit-learn.', 'Random Forest in scikit-learn can use bagging as an ensemble method.', "The default kernel for `SVC` in scikit-learn is linear - if you don't know this you can look at the docstring for `SVC` to find out.", '`cross_val_score` performs cross-validation on a model in scikit-learn.', 'Pipelines in scikit-learn are used to chain multiple estimators and transformers.'],
            points=[1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
        )
class Question3(SelectMany):
    def __init__(self):
        super().__init__(
            title=f"Select All That Apply",
            style=MultiSelect,
            question_number=3,
            keys=['q3-1-supervised-learning', 'q3-2-feature-scaling', 'q3-3-model-selection', 'q3-4-dimensionality-reduction'],
            descriptions=['Which of the following are supervised learning algorithms in scikit-learn?', 'Which of the following are used for feature scaling in scikit-learn?', 'Which modules are used for model selection and evaluation?', 'Which techniques are used for dimensionality reduction in scikit-learn?'],
            options=[['`LinearRegression`', '`KNeighborsClassifier`', '`PCA`', '`RandomForestClassifier`'], ['`MinMaxScaler`', '`StandardScaler`', '`Normalizer`', '`LabelEncoder`'], ['`sklearn.model_selection`', '`sklearn.metrics`', '`sklearn.preprocessing`', '`sklearn.datasets`'], ['`PCA`', '`TruncatedSVD`', '`LinearDiscriminantAnalysis`', '`RandomForestClassifier`']],
            points=[2.0, 2.0, 2.0, 2.0],
            grade=['parts'],
        )
