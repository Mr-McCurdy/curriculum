# curriculum/scripts/quiz_lib/utils.py

def get_user_input(prompt: str) -> str:
    """
    Retrieves input from the user.
    
    Args:
        prompt (str): The prompt message to display.
    
    Returns:
        str: The user's input.
    """
    return input(prompt)