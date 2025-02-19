#!/bin/bash

# Assigns the Assignment Number
# make sure this is lowercase
ASSIGNMENT_NUMBER="quiz_9"

# Sets the username and password for the student grader web account
# this is just there to prevent bombardment of the server
USERNAME="student"
PASSWORD="capture"

# Directory containing the .ipynb files
NOTEBOOK_DIR="./submission" # Set to your notebook directory

# Directory to store the results
RESULTS_DIR="./submission"

# Find all .ipynb files in the ./submission directory and store them in an array
NOTEBOOKS=($(find ./submission -name "*.log"))

# Login to the student grader
curl -s -o /dev/null -c student_cookie.txt \
    -X POST \
    -d "username=$USERNAME&password=$PASSWORD" \
    https://engr131-student-grader.nrp-nautilus.io/login

# Check if there are any .log files
if [ ${#NOTEBOOKS[@]} -eq 0 ]; then
    echo "No .log files found in $NOTEBOOK_DIR."
    exit 1
fi

for notebook in "${NOTEBOOKS[@]}"; do
    
    echo "Processing $notebook..."

    # Extract filename without extension
    base_name=$(basename "$notebook" .log)

    python3 read_log_file.py "$notebook"

    # Check if results.json was created
    if [ -f "results.json" ]; then
        # Copy and rename results.json to the submission folder
        cp results.json "${base_name}_results.json"

        # Assuming the Python script has already been run and info.json exists

        if [ -f info.json ]; then
            while IFS="=" read -r key value; do
                export "$key"="$value"
            done < <(jq -r "to_entries|map(\"\(.key)=\(.value|tostring)\")|.[]" info.json)
        else
            echo "info.json not found"
            exit 1
        fi

        echo "Uploading $base_name to the student grader... Your Drexel ID is $DREXEL_ID"

        grade-report "${base_name}_results.json" \
            "$DREXEL_ID" \
            "$FIRST_NAME" \
            "$LAST_NAME" \
            "$DREXEL_EMAIL" \
            "$ASSIGNMENT_NUMBER" \
            "$base_name"

        cp "${base_name}_Grade_Report.md" "$RESULTS_DIR/${base_name}_Grade_Report.md"

        curl -b student_cookie.txt \
            -X POST \
            -F "file=@${base_name}_results.json" \
            -F "password=$PASSWORD" \
            -F "assignment_id=$ASSIGNMENT_NUMBER" \
            -F "student_id=$DREXEL_ID" \
            -F "original_file_name=$base_name" \
            -F "start_time=$START_TIME" \
            -F "end_time=$END_TIME" \
            https://engr131-student-grader.nrp-nautilus.io/upload_score

        rm results.json
        
    else
        echo "No results.json generated for $notebook"
    fi
done