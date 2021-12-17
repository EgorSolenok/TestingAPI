# Testing API Project https://jsonplaceholder.typicode.com
**PythonTestAutomationFramework**

**Description**

Test REST API Automation Framework of "https://jsonplaceholder.typicode.com" using Python.


* Framework realized with different multiple tests for CRUD requests methods. 
* Has positive and negative (marked as xfail) tests.
* Usage of pytest, cerberus
* Allure reporting.
* Logging to external file.
* Parallel running - pytest-xdist

# How to install it
Make sure you have python3.6 or later installed on your machine by typing in cmd ``python3 --version`` if not - go to https://realpython.com/installing-python/#step-1-download-the-python-3-installer.

1) Clone the repository to any local path.

``$ git clone https://github.com/EgorSolenok/TestingAPI.git``

2) Make sure you have  allure command line  by typing in cmd ``allure --version``. If not - you have to install allure command line and add the allure folder installation into system environment variable: https://docs.qameta.io/allure/#_installing_a_commandline

3) Make sure you have pipenv by typing in cmd ``pipenv --version``. If not - you have to install pipenv for creation virtual environment and installation packages: https://pipenv.pypa.io/en/latest/  

``$ pip install --user pipenv``

4) Install dependencies:

``pipenv install``

# How to run it

**For all tests running you should type commands in root directory.**

To run all existing tests in parallel (positive, negative) and create report:

`` pipenv run python -m pytest -n auto --tb=line --alluredir=report_data ``

To run all positive tests and create report:

`` pipenv run python -m pytest .\tests\positive_tests\  -n auto --tb=line --alluredir=report_data ``

To run all negative tests negative and create report:

`` pipenv run python -m pytest .\tests\positive_tests\ -n auto --tb=line --alluredir=report_data ``

To running tests not in parallel - you should remove ``  -n auto  `` from commands.

To create **Allure report** and open it - type in cmd being located in the folder path:

``allure serve report_data``

**Logging**

To read logs you should see file ``logging_data.log``