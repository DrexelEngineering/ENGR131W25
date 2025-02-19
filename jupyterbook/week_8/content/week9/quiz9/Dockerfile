# syntax=docker/dockerfile:1
# otter grade -n demo -a ./dist/demo-autograder_2023_12_15T16_56_04_536836.zip -v ./submission
FROM ubuntu:latest

WORKDIR /app

# Copy the source code into the /app directory in the container.
# COPY ./dist /app/dist
COPY ./requirements.txt /app/requirements.txt
COPY ./grader.sh /app/grader.sh
COPY ./read_log_file.py /app/read_log_file.py


# Install Docker and Python
RUN apt-get update && \
    apt-get install -y docker

# # Install Python 3.10
RUN apt-get install -y python3.10 python3.10-venv python3.10-dev python3-pip curl jq
RUN pip install -r ./requirements.txt
RUN pip install -U mistune
RUN pip install -U drexel_jupyter_logger

# Ensure the script is executable
RUN chmod +x ./grader.sh

# # Command to run the script
CMD ["./grader.sh"]
