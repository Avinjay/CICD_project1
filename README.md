# Git Commit Deployer

## Description
This Python script monitors a Git repository for new commits and automatically deploys the changes to a production environment.

## Dependencies
* `requests`
* `os`
* `subprocess`
* `logging`
* `datetime`
* `dotenv`

## Configuration
The script uses environment variables to store sensitive information such as the GitHub PAT and the GITHOME directory. You can customize the following options:

* `GITHUB_PAT`: The GitHub Personal Access Token
* `GITHOME`: The directory where the script will store the cloned repository. Make the changes as per your system folder structure and place python & Shell script one folder behind of GITHOME. the env file is not placed here for security reason because it will expose PAT.

## Usage

1. Install the required dependencies using `pip install requests os subprocess logging datetime dotenv`
2. Set the `GITHUB_PAT` and `GITHOME` environment variables
3. Run the script using `python deploy.py`

## Shell Script
The script calls a shell script (`scrip.sh`) to perform the deployment. The shell script is located in the `GITHOME` directory and is executed using the `subprocess` module.

### Shell Script Details
* The shell script takes a single argument, the Git repository URL.
* It extracts the repository name from the URL using `cut` and `awk`.
* It checks if the local repository exists, and if so, pulls the latest changes from the remote repository using `git pull`.
* If the local repository does not exist, it clones the repository using `git clone`.
* It copies the `index.html` file to the production directory using `cp`.
* It restarts the Nginx service using `systemctl restart nginx`.
* It logs the output of the shell script to a file using `tee`.

## Troubleshooting
* Check the script's output for errors
* Verify that the `requests`, `os`, `subprocess`, and `logging` commands are installed and available on your system
* Ensure that the environment variables are correctly set
* Check the shell script (`scrip.sh`) for any errors or issues

## LOGGING
The code uses the logging module to log important events and errors. The logging module provides a flexible and customizable way to log messages, including the ability to specify the log level, log format, and log destination.

In this code, the logging module is used to log the following events:

* INFO: The script logs an INFO message when it starts and when it completes successfully.
* ERROR: The script logs an ERROR message if an error occurs during the execution of the script.
* DEBUG: The script logs a DEBUG message if the DEBUG log level is set to True.
The log messages are written to a file named filelogg.log in the GITHOME directory. The log file is created in the GITHOME directory and is updated each time the script is run.

The logging feature is useful for debugging and troubleshooting the script. It allows you to track the script's execution and identify any errors or issues that may occur.

<img width="941" alt="image" src="https://github.com/user-attachments/assets/31e7a2e7-fede-4e47-94bc-7f201b2e5bf5" />

<img width="938" alt="image" src="https://github.com/user-attachments/assets/6dd5f320-d9a8-48b2-954b-513903e5ad1c" />

<img width="844" alt="image" src="https://github.com/user-attachments/assets/c566b244-8bc6-442c-b908-27b883bb1028" />

## OUTPUT
<img width="715" alt="image" src="https://github.com/user-attachments/assets/5ad5dfa8-3da3-4e6d-bfa1-fd9035a81eaa" />

<img width="352" alt="image" src="https://github.com/user-attachments/assets/9805992b-5c68-4802-ad45-abbb5d9aa097" />

<img width="354" alt="image" src="https://github.com/user-attachments/assets/c77a3912-3f96-46e1-b343-9740868fa219" />








