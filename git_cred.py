import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access Git credentials
git_username = os.getenv("GIT_USERNAME")
git_email = os.getenv("GIT_EMAIL")

import subprocess

def set_git_user_email(username, email):
    subprocess.run(["git", "config", "--global", "user.name", username])
    subprocess.run(["git", "config", "--global", "user.email", email])
    print(username, email)


if __name__ == "__main__":
    set_git_user_email(username = git_username, email = git_email)