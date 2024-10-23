# curriculum/scripts/quiz_lib/canvas_api.py

import requests
from typing import Dict, Any
from .config import load_secrets
import logging

class CanvasAPI:
    """
    A class to interact with the Canvas API for managing quizzes and questions.
    
    Attributes:
        api_url (str): Base URL of the Canvas API.
        api_key (str): Authorization token for the API.
        course_id (str): ID of the course where quizzes are managed.
        headers (Dict[str, str]): HTTP headers for API requests.
        logger (logging.Logger): Logger for logging information and errors.
    """
    
    def __init__(self, secrets_file_path: str = None):
        secrets = load_secrets(secrets_file_path)
        self.api_url = secrets.get('API_URL')
        self.api_key = secrets.get('API_KEY')
        self.course_id = secrets.get('COURSE_ID_STATISTICS')
        
        if not all([self.api_url, self.api_key, self.course_id]):
            missing = [key for key in ['API_URL', 'API_KEY', 'COURSE_ID_STATISTICS'] if not secrets.get(key)]
            raise ValueError(f"Missing keys in secrets: {', '.join(missing)}")
        
        self.headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
        
        # Setup logging
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
    
    def create_quiz(self, title: str, description: str, quiz_type: str = 'assignment', published: bool = False) -> Dict[str, Any]:
        """
        Creates a quiz in the specified Canvas course.
        
        Args:
            title (str): Title of the quiz.
            description (str): Description of the quiz.
            quiz_type (str): Type of the quiz (default is 'assignment').
            published (bool): Whether the quiz is published (default is False).
        
        Returns:
            Dict[str, Any]: JSON response from the API containing quiz details.
        
        Raises:
            requests.HTTPError: If the API request fails.
        """
        quiz_data = {
            'quiz': {
                'title': title,
                'description': f'<p>{description}</p>',
                'quiz_type': quiz_type,
                'published': published
            }
        }
        
        create_quiz_url = f'{self.api_url}/api/v1/courses/{self.course_id}/quizzes'
        self.logger.info(f"Creating quiz '{title}'")
        response = requests.post(create_quiz_url, headers=self.headers, json=quiz_data)
        
        if response.status_code in [200, 201]:
            quiz = response.json()
            quiz_id = quiz.get('id')
            self.logger.info(f"Quiz created successfully with ID: {quiz_id}")
            return quiz
        else:
            self.logger.error(f"Failed to create quiz. Status Code: {response.status_code}")
            self.logger.error(f"Response: {response.text}")
            response.raise_for_status()
    
    def get_quiz(self, quiz_id: int) -> Dict[str, Any]:
        """
        Retrieves details of a specific quiz.
        
        Args:
            quiz_id (int): ID of the quiz.
        
        Returns:
            Dict[str, Any]: JSON response containing quiz details.
        
        Raises:
            requests.HTTPError: If the API request fails.
        """
        get_quiz_url = f'{self.api_url}/api/v1/courses/{self.course_id}/quizzes/{quiz_id}'
        self.logger.info(f"Retrieving quiz with ID: {quiz_id}")
        response = requests.get(get_quiz_url, headers=self.headers)
        
        if response.status_code == 200:
            return response.json()
        else:
            self.logger.error(f"Failed to retrieve quiz. Status Code: {response.status_code}")
            self.logger.error(f"Response: {response.text}")
            response.raise_for_status()