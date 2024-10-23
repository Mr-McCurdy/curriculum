# curriculum/scripts/quiz_lib/questions.py

from typing import Dict, Any
import requests
import logging

def add_question(api_url: str, course_id: str, quiz_id: int, headers: Dict[str, str], question: Dict[str, Any]) -> None:
    """
    Adds a question to a specified quiz.
    
    Args:
        api_url (str): Base URL of the Canvas API.
        course_id (str): ID of the course.
        quiz_id (int): ID of the quiz.
        headers (Dict[str, str]): HTTP headers including authorization.
        question (Dict[str, Any]): Question data.
    
    Raises:
        requests.HTTPError: If the API request fails.
    """
    create_question_url = f'{api_url}/api/v1/courses/{course_id}/quizzes/{quiz_id}/questions'
    
    # Base question data
    question_data = {
        'question': {
            'question_name': question['question_name'],
            'question_type': question['question_type'],
            'question_text': question['question_text'],
            'points_possible': question.get('points_possible', 1)
        }
    }
    
    # Include 'answers' only if they exist and the question is not an essay question
    if 'answers' in question and question['question_type'] != 'essay_question':
        question_data['question']['answers'] = question['answers']
    
    # Include 'general_feedback' if it exists (for essay questions)
    if 'general_feedback' in question:
        question_data['question']['general_feedback'] = question['general_feedback']
    
    response = requests.post(create_question_url, headers=headers, json=question_data)
    
    if response.status_code in [200, 201]:
        print(f"Added question '{question['question_name']}' successfully.")
    else:
        print(f"Failed to add question '{question['question_name']}'")
        print(f"Status Code: {response.status_code}")
        print(response.text)
        response.raise_for_status()