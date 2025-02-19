# Quiz 8 Practice Cookbook

## Step 1: Sets the Assignment Number

```bash
ASSIGNMENT_NUMBER="practicequiz_9" &&
ASSIGNMENT_NAME="practicequiz_9 - Classes"
```

## Step 2: Building the Assignment with a Local Docker Image

### Load the Docker Environment

```bash
docker run -it -v ./:/usr/src/app jagar2/engr_131_python_env:latest
```

### Building the Assignment

```bash
pip install -U mistune &&
otter assign ./*.ipynb dist &&
mkdir ./dist/test_solution &&
chown -R $USER:$USER ./dist &&
cp ./dist/autograder/*.ipynb ./dist/test_solution/
```

This will fix one dependency issue with the mistune package, run otter assign, and copy the autograder notebook to the test_solution folder.

### Testing the Assignment

```bash
otter run -a ./dist/autograder/*.zip ./dist/test_solution/*.ipynb 
mv results.json ./dist/test_solution/results.json
```

This will test that the solution generated receives full credit. The results.json file will be moved to the test_solution folder. This is used to add the assignment to the database.

Exit the docker container. exit

```bash
sudo chown -R $(whoami) ./
```

actvity /home/ferroelectric/PRIVATE_ENGR131_W24/SOLUTIONS/week9/quiz9_practice/dist/student/quiz9-classes-practice.ipynb