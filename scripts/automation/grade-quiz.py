python -m pip install openai

#Import libraries
import json
import os
import openai
from openai import OpenAI


#Load API Keys
canvas_api_key = os.getenv('CANVAS_API_KEY')
github_api_key = os.getenv('GITHUB_API_KEY')
openai_api_key = os.getenv('OPENAI_API_KEY')


# Load secrets
SECRETS_FILE = '/Users/gmccurdy/repos/curriculum/scripts/utilities/secrets.json'

with open(SECRETS_FILE, 'r') as file:
    secrets = json.load(file)

canvas_url = secrets.get('CANVAS_URL')
course_id_apstatistics = secrets.get('COURSE_ID_APSTATISTICS')
course_id_statistics = secrets.get('COURSE_ID_STATISTICS')
course_id_hprecalculus = secrets.get('COURSE_ID_HPRECALCULUS')
course_id_precalculus = secrets.get('COURSE_ID_PRECALCULUS')


