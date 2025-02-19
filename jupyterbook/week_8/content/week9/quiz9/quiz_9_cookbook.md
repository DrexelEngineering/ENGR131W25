# Quiz 6 Cookbook

## Step 1: Creating the GitHub Repository

To create an assignment we need a github repository with a template that contains the github action file. The easiest way to do that is take the previous homework assignment as a template. This is an option when creating a new repository.

wronged-june-nephew

## Step 2: Creating a Secret to the Docker Container

It is a good idea to obfuscate the docker container name. To do this we need to create a secret in the github repository. The secret.

The schema for the secret name is ENGR131_HWX_2024  ENGR131_QUIZ9_2024

The schema for the docker container is: <username(jagar2)>/engr_131_<ASSIGNMENT_NUMBER>:latest

## Step 3: Modifying the GitHub Action File

Create a new repository modeled after the previous quiz.

The github action file is located in the .github/workflows folder. The file is called grader.yml. The file should be modified to change the docker secrete of the docker container to match the assignment number. This can be created in the organization by going to:

1. Settings
2. Secrets and Variables
3. Actions
4. Organizational Secrets

The schema for the docker container is: <username(jagar2)>/engr_131_<ASSIGNMENT_NUMBER>:latest

The schema for the secret name is ENGR131_HWX_2024

## Step 4: Update the Readme.md File in the repository

Update the readme.md file in the repository to match the assignment number and assignment name.

## Step 5: Turn the assignment into a template

For the assignment to be used with github classroom it needs to be a template. To do this click settings, and the check the box that says "Template Repository".

It is helpful to add [skip actions] in the commit message so that the github action does not run when you commit the changes.

## Step 6: Create the Assignment in GitHub Classroom

To create the assignment in github classroom go to the organization page and click "New Assignment". Follow the onscreen instructions to create the assignment, and copy the link.

You can leave it here for future reference.

<https://classroom.github.com/a/Ok5XgX3N>


## Step 15: Creating the Wise Assignment

1. Go to Wise
2. Login as a Professor jca318@lehigh.edu pass: PA5PwLjLq94HSR
3. Click start proctoring
4. Add the NBpuller link. 

Get the wise link and place it in the student file.

https://courses.coe.drexel.edu/ENGR/ENGR131W24_Quiz/index.html

https://online.wiseattend.com/student/testLink?c=ENGR131&k=6857

## Step 7: Copy Files to the Solution Folder

Place the solution notebook with otter format, the `grader.sh` file, and the `Dockerfile` in the folder for the assignment.

Edit the assignment number variable in the `grader.sh` file to match the assignment number.

## Step 8: Add the Submit Assignment Instructions

Add the submit assignment instructions to the to the assignment notebook. Make sure to update the link to the github classroom assignment that was just created.

## Step 9: Set the Bash Variables

Navigate to the root directory of the assignment and run the following lines to set the bash variables. Make sure they are updated to reflect the assignment number and assignment name.

### Sets the Assignment Number

```bash
ASSIGNMENT_NUMBER="quiz_9" &&
ASSIGNMENT_NAME="quiz_9 - classes"
```

## Step 10: Change the assignment number in the grader.sh file

Make sure you change the assignment number in the grader.sh file to match the assignment number you are grading.

## Step 11: Building the Docker Image for Grading

Update the tag name to match the version of the assignment. This will build the docker image and push it to docker hub. It will also tag the image as latest and push it to docker hub.

```bash
tagname="0.0.2"
docker build -t jagar2/engr_131_$ASSIGNMENT_NUMBER:$tagname . &&
docker push jagar2/engr_131_$ASSIGNMENT_NUMBER:$tagname &&
docker tag jagar2/engr_131_$ASSIGNMENT_NUMBER:$tagname jagar2/engr_131_$ASSIGNMENT_NUMBER:latest &&
docker push jagar2/engr_131_$ASSIGNMENT_NUMBER:latest
```

This can take some time to complete as the docker container can be a few gigabytes in size.

## Step 16: Building the Container with a Local Docker Image

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

## Step 17: Adding the Assignment to the Database

This calls a script that creates a cookie for login to the SQL database as an admin. It then does a post request to the server to add the assignment to the database. Finally it removes the cookie.

Option 1: local evaluation

Generate the output.log

sudo chown -R $(whoami) ./


```bash
python3 read_log_file.py output.log &&
curl -s -o /dev/null -c cookie.txt -X POST -d "username=admin&password=diffuser"  https://engr131-admin-grader.nrp-nautilus.io/login &&
curl -b cookie.txt -X POST -F "file=@./results.json" -F "password=diffuser" -F "assignment_id=$ASSIGNMENT_NUMBER" -F "assignment_name=$ASSIGNMENT_NAME" https://engr131-admin-grader.nrp-nautilus.io/upload_assignment &&
rm cookie.txt
```

The post request will return success if successful.

## Step 18: Upload the Assignment to the Github Repository

Download the file from the student folder in dist and upload it to the github repository. This is the file with the tests.

## Step 19: Copy the Student Assignment Locally for JupyterHub

Copy the student assignment locally for the jupyterhub. This makes it editable

```bash
folder_path="./dist/student" &&
prefix="jbook-" &&
destination_folder="./student" &&
mkdir -p "$destination_folder" &&
ipynb_file=$(find "$folder_path" -name '*.ipynb' -print -quit) &&
file_name=$(basename "$ipynb_file") &&    
cp "$ipynb_file" "$destination_folder/$prefix$file_name" &&
build-quiz-for-jupyterbook "$destination_folder"
```

## Step 12: Creating a Repository with the Quiz

We have to post the quiz online but it is preferred that the students do not know where to find the quiz. To do this, we will create a public repository with a random name. 

Once the repository is created, we will add the quiz to the repository.

Download the quiz from the student folder and upload it to the respository. 

## Step 14: Creating the GitPuller Link

We need to create a gitpuller link to the exam jupyterhub and connect it to the quiz repository. 

Navigate to this link <https://nbgitpuller.readthedocs.io/en/latest/link.html>

The jupyter hub is located at http://engrjhub.eastus.cloudapp.azure.com/

Copy the link to the repository and paste it into the gitpuller link generator.

<https://github.com/jagar2/humbling-likeness-cardigan>

Make sure to set the branch to main.

Copy the generated link. It can go here:

http://engrjhub.eastus.cloudapp.azure.com/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fjagar2%2Fwronged-june-nephew&urlpath=lab%2Ftree%2Fwronged-june-nephew%2Fquiz9-classes.ipynb&branch=main
