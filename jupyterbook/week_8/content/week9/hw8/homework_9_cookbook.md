# Homework 4 Cookbook

## Step 1: Creating the GitHub Repository in DrexelEngineering

To create an assignment, we need to first make a GitHub repository with a template that contains the github action file in the DrexelEngineering organization. The easiest way to do that is take the previous homework assignment as a template. This is an option when creating a new repository.

It is helpful to add [skip actions] in the commit message so that the github action does not run when you commit the changes.

## Step 2: Modifying the GitHub Action File

The github action file is located in the .github/workflows folder. The file is called grader.yml. The file should be modified to change the docker secret of the docker container to match the assignment number. This can be created in the organization by going to:

1. Settings
2. Secrets and Variables
3. Actions
4. Organizational Secrets

The schema for the docker container is: <username(jagar2)>/engr_131_<ASSIGNMENT_NUMBER>:latest

The schema for the secret name is ENGR131_HWX_2024

## Step 3: Update the Readme.md File in the repository

Update the readme.md file in the repository to match the assignment number and assignment name.

## Step 4: Turn the assignment into a template

For the assignment to be used with github classroom it needs to be a template. To do this click settings, and the check the box that says "Template Repository".


## Step 5: Create the Assignment in GitHub Classroom

To create the assignment in github classroom go to the organization page and click "New Assignment". Follow the onscreen instructions to create the assignment, and copy the link. Leave autograde tests field blank.

You can leave it here for future reference.

<https://classroom.github.com/a/cxTEzdqI>

## Step 6: Copy Files to the Solution Folder

Leave the solution notebook with otter format in the folder for the assignment. 

Copy from a previous homework directory the `grader.sh` file, the `requirements.txt` file, and the `Dockerfile` in the folder for the assignment.

Edit the assignment number variable in the `grader.sh` file to match the assignment number.

## Step 7: Add the Student ID and Submit Assignment Instructions

Add the Student ID and submit assignment instructions to the to the assignment notebook by copying first and final Markdown cells from a previous assignment. Make sure to update the link to the github classroom assignment that was just created.

## Step 8: Set the Bash Variables

Navigate to the root directory of the assignment and run the following lines to set the bash variables. Make sure they are updated to reflect the assignment number and assignment name.

### Sets the Assignment Number

```bash
ASSIGNMENT_NUMBER="homework_9" &&
ASSIGNMENT_NAME="homework 9 - Classes"
```

## Step 9: Change the assignment number in the grader.sh file

Make sure you change the assignment number in the grader.sh file to match the assignment number you are grading.

## Step 10: Building the Container with a Local Docker Image

### Load the Docker Environment

```bash
docker run -it -v ./:/usr/src/app jagar2/engr_131_python_env:latest
```

### Building the Assignment

From the ./SOLUTIONS/week4/homework_4 folder:

```bash
pip install -U mistune &&
otter assign ./*.ipynb dist
chown -R $USER:$USER ./dist &&
mkdir ./dist/test_solution &&
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

## Step 11: Adding the Assignment to the Database

From the ./SOLUTIONS/week4/homework_4 folder:

This calls a script that creates a cookie for login to the SQL database as an admin. It then does a post request to the server to add the assignment to the database. Finally it removes the cookie.

```bash
curl -s -o /dev/null -c cookie.txt -X POST -d "username=admin&password=diffuser"  https://engr131-admin-grader.nrp-nautilus.io/login &&
curl -b cookie.txt -X POST -F "file=@./dist/test_solution/results.json" -F "password=diffuser" -F "assignment_id=$ASSIGNMENT_NUMBER" -F "assignment_name=$ASSIGNMENT_NAME" https://engr131-admin-grader.nrp-nautilus.io/upload_assignment &&
rm cookie.txt
```

The post request will return success if successful.

## Step 12: Building the Docker Image for Grading ???

Update the tag name to match the version of the assignment. This will build the docker image and push it to docker hub. It will also tag the image as latest and push it to docker hub.

First, copy the Dockerfile from a previous homework directory to this homework directory. 

```bash
tagname="0.0.2"
docker build -t jagar2/engr_131_$ASSIGNMENT_NUMBER:$tagname . &&
docker push jagar2/engr_131_$ASSIGNMENT_NUMBER:$tagname &&
docker tag jagar2/engr_131_$ASSIGNMENT_NUMBER:$tagname jagar2/engr_131_$ASSIGNMENT_NUMBER:latest &&
docker push jagar2/engr_131_$ASSIGNMENT_NUMBER:latest
```

This can take some time to complete as the docker container can be a few gigabytes in size.

## Step 13 (Optional): Testing the Docker Image Locally

It is useful to test the docker image locally. Since the original docker container that makes the grading image is not owned by the local user it is necessary to copy the ./dist/test_solution folder to the root directory of the assignment. This can be done with the following command:

```bash
cp -r ./dist/test_solution ./
```

The docker image can then be run with the following command:

```bash
docker run -v ./test_solution:/app/submission cappssl/engr_131_$ASSIGNMENT_NUMBER:latest
```

Again, you should check that you see the Drexel ID and the success message.

## Step 14: Check the Autograder on GitHub

Use the provided link and create your own repository to test the autograder.

1. Skip selecting your name if you are not in the classroom list.
2. Follow instructions to create your repository.
3. Hit refresh to see when your repository is ready.
4. Upload the solution file, commit changes, and wait for the grader to complete.

## Step 15: Tag the Student File for Inclusion in the Jupyter Book

This will change the ownership of the files and then make all of the MD files not editable and all of the otter grader commands skipped for the jupyter book

```bash
sudo chown $(whoami) ./dist/student/*.ipynb &&
sudo chmod u+w ./dist/student/*.ipynb &&
tag-files ./dist/student
```

## Step 16: Move the files to the Jupyter Book

Move the file to the location in the jupyter book. Then add the file to the TOC and a index file if necessary. Follow the notes to rebuild the jupyter book and push the changes to the website.
