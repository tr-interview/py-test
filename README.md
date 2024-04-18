# Technical test task

This test is designed to test your Python coding skills. The basic project should provide you all that you need to get up and running, all you need to do is to add your code and run. 

## The Rules
You have 30 minutes for this test. Feel free to use Google and the official docs. Please don't use any AI code generating tools.

## Pre-requisites
You will need to have a working installation of Python 3.9 or above. This will be supplied to you as a Cloud9 IDE instance

## Getting started
Create a fork of this repository into your personal Github organisation and then checkout this fork locally.

Create a python virtual environment 
```python3 -m venv .venv ```

Activate the environment
```source .venv/bin/activate```

Then install all the required dependancies of this project by running 
```pip install -r requirements.txt```

Then you should be able to build this project with 
```python3 github_api.py```


# The Test
We would like you to create a script using Python to help us manage our Github repositories. The Github organisation `tr-interview` contains a number of private repositories. 

Please write a script the will fetch the name of all of the private repositories in this organisation via the Github API and output them to the console. 

We have supplied a Github personal access token which will give you access to this organisation via the API. 

When you have completed the test locally, please commit your script back to your personal repository, you shoudl then provide us with a link to this repository so we can validate your script. 

Please make sure that you follow security best practices and DO NOT commit any secrets back to Github. 

## Bonus Points
If there is still time remaining please do the following:

* Create a Dockerfile that will run your script
* Build your Dockerfile into an image called pytest
* Run a Docker container using your new image which outputs the repo names to the console.
