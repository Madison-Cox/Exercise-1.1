# Exercise-1.1

# Install Python
Install Python 3.8.7
You can check version by doing python --version in terminal.

# Set up Virtual Environment
Create virtual environment by using mkvirtualenv <name> in terminal.

# Write a script
create a Python script named “add.py”. This script will add two numbers and print the total.

# Set up ipython
Set up an IPython shell in the virtual environment "cf-python-base". An IPython shell is similar to the regular Python REPL with additional features like syntax highlighting, auto-indentation, and robust auto-complete features. Install using _pip install ipython_.

# Create requirements.txt
1. Generate a “requirements.txt” file from your source environment. To do this, you use the pip freeze command and all packages (including version numbers) installed in the currently activated environment will be compiled: > pip freeze > requirements.txt.
2. Next, create a new environment called “cf-python-copy”. In this new environment, install packages from the “requirements.txt” file that you generated earlier. To install the packages from this file in any other environment, you run the pip install command with the extra -r argument, followed by the name of your requirements file: > pip install -r requirements.txt.
3. 
