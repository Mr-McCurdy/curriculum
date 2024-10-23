# curriculum/scripts/quiz_lib/config.py

import json
import os
from typing import Dict, Any

def load_secrets(secrets_file_path: str = None) -> Dict[str, Any]:
    """
    Loads secrets from a JSON file.

    Args:
        secrets_file_path (str): Path to the secrets JSON file. 
                                 If None, uses the default path.

    Returns:
        Dict[str, Any]: A dictionary containing secrets.

    Raises:
        FileNotFoundError: If the secrets file does not exist.
        json.JSONDecodeError: If the secrets file contains invalid JSON.
    """
    if not secrets_file_path:
        secrets_file_path = os.getenv('SECRETS_FILE', 'secrets.json')
    
    if not os.path.exists(secrets_file_path):
        raise FileNotFoundError(f"'{secrets_file_path}' not found. Please provide a valid path.")
    
    with open(secrets_file_path, 'r') as file:
        secrets = json.load(file)
    
    return secrets