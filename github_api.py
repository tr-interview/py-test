import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get GitHub PAT from environment variables
access_token = os.getenv('GITHUB_PAT')
org_name=os.getenv('GITHUB_ORG')

if not access_token:
    print('GitHub Personal Access Token not found in .env file')
    exit(1)

# GitHub API base URL
api_url = 'https://api.github.com'

# Write your script here and output the results to the console.