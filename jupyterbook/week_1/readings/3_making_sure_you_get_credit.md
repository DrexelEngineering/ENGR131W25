# 📖 Making Sure You Get Credit

![](./assets/figures/credit.webp)

## 📚 Learning Objectives

I am sure you all want to get credit for the work you do, this is your guide. 

## 📖 Introduction

When you encounter a webpage with a ❓ icon, it means that you have to complete a task. This task can be a quiz, a coding exercise, or a discussion question. 

1. To access the assignment, you need to open the notebook in JupyterLab. Sorry, you can't complete the assignment on your local machine.

![](assets/figures/nbpuller.png)

## Starting the Assignment

1. Open the notebook in JupyterLab.
2. Read the instructions carefully.
3. Run the initialization block of code to get started. You can do this by pressing `Shift + Enter` or clicking the `Run` button in the toolbar.

## Types of Questions

### Multiple Choice Questions

We have multiple choice questions that you can answer by selecting the correct option. To view the code block, run the cell by pressing `Shift + Enter`.

#### Run the code block below to display the question:

the code block will look like this:

```python
# Run this block of code by pressing Shift + Enter to display the question
from questions._11_formal_and_natural_language_q import Question4
Question4().show()
```

#### Respond

select the correct option. There is only one correct answer.

#### Submit

Press the `Submit` button. 

![](assets/figures/submit.png)

if your submission is received, you will see a message like this:

![](assets/figures/response_submitted.png)

### True False Questions

There will be several true/false questions, select the best answer. You must run the code block to display the question, and submit the question similar to the multiple choice questions.

### Select Many Questions

There will be several select many questions. For these questions you must select all the answers that apply. You must run the code block to display the question, and submit the question similar to the multiple choice questions. You will get credit only if you select all the correct answers.

### Free Response Coding Questions

There will be several free response coding questions. There will be detailed instructions for each question. Your code will replace code that has `...`. You will need to run the block of code that you write, and then submit the question by running the grader block of code which looks like this:

```python
grader.check("question")
``` 

This will check your answers and provide feedback.

## 📝 Submission

To submit your assignment and get credit you must run the submit assignment block of code. This will look like this:

```python
from pykubegrader.submit.submit_assignment import submit_assignment

submit_assignment("week1-readings", "<notebook>")
```

When you run this block of code your assignment will be submitted and you will receive a message like this containing your grade:

![](assets/figures/submitting-assignment.png)


