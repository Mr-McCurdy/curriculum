!pip install openai
!pip install python-dotenv

import json
import os
import requests
from IPython.display import Markdown, display
import openai
from openai import OpenAI

# Define the path to your secrets file
SECRETS_FILE = '/Users/gmccurdy/repos/curriculum/scripts/utilities/secrets.json'

# Load OpenAI API
with open(SECRETS_FILE, 'r') as file:
    secrets = json.load(file)
OPENAI_API_KEY = secrets.get('OPENAI_API_KEY')

# Load secrets from the JSON file
with open(SECRETS_FILE, 'r') as file:
    secrets = json.load(file)

# Extract the GitHub token
GITHUB_TOKEN = secrets.get('GITHUB_TOKEN')

# Verify that the token was loaded successfully
if not GITHUB_TOKEN:
    raise ValueError("GitHub token not found in secrets.json")

# Define Repository and File Details
GITHUB_REPO = 'Mr-McCurdy/curriculum'          # Repository in 'owner/repo' format
GITHUB_FILE_PATH = 'subjects/mathematics/AP-statistics/content/confidence-intervals.md'  # Path to the file in the repo
GITHUB_BRANCH = 'main'  # Branch name (default is 'main')

def fetch_markdown_from_github(repo, file_path, branch='main', token=None):
    """
    Fetches the raw markdown content from a GitHub repository.

    :param repo: Repository in the format 'owner/repo' (e.g., 'octocat/Hello-World')
    :param file_path: Path to the markdown file within the repository (e.g., 'docs/article.md')
    :param branch: Branch name (default is 'main')
    :param token: GitHub Personal Access Token
    :return: Markdown content as a string
    """
    headers = {
        'Accept': 'application/vnd.github.v3.raw'  # Fetches raw content directly
    }
    
    if token:
        headers['Authorization'] = f'token {token}'
    
    # Construct the GitHub API URL
    url = f'https://api.github.com/repos/{repo}/contents/{file_path}?ref={branch}'
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.text
    elif response.status_code == 404:
        raise FileNotFoundError(f"The file '{file_path}' was not found in repository '{repo}'.")
    else:
        raise Exception(f"Failed to fetch file from GitHub: {response.status_code} {response.text}")

def extract_section(markdown_content, section_header):
    """
    Extracts a specific section from the markdown content based on the header.

    :param markdown_content: Full markdown content as a string
    :param section_header: Header of the section to extract (e.g., '# Exercises')
    :return: Content of the section as a string
    """
    lines = markdown_content.splitlines()
    section_lines = []
    capture = False

    for line in lines:
        if line.startswith(section_header):  # Start capturing lines after the specified header
            capture = True
            section_lines.append(line)
        elif capture and line.startswith('#'):  # Stop capturing when the next section starts
            break
        elif capture:
            section_lines.append(line)

    return '\n'.join(section_lines)

# Fetch the Markdown Content
try:
    print("Fetching Markdown content from GitHub...")
    markdown_content = fetch_markdown_from_github(
        repo=GITHUB_REPO,
        file_path=GITHUB_FILE_PATH,
        branch=GITHUB_BRANCH,
        token=GITHUB_TOKEN
    )
    print("Markdown content fetched successfully.")
    
    # Extract the specific section
    section_header = '## Exercises'
    section_content = extract_section(markdown_content, section_header)
    print(f"### Extracted Content from '{section_header}' Section:\n")
    display(Markdown(section_content))

except FileNotFoundError as fnf_error:
    print(fnf_error)
except Exception as e:
    print(f"An error occurred: {e}")

client = OpenAI(api_key=OPENAI_API_KEY)

prompt = "Create a multiple choice assessment based on these exercises" + section_content

completion = client.chat.completions.create(
    model="gpt-o1-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": prompt
        }
    ]
)

print(completion.choices[0].message.content)
print(completion.usage.total_tokens)




