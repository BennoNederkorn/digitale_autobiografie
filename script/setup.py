import logging
from pathlib import Path

def get_logger():
    # Configure the logger
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler("app.log"),  # Log to a file
            logging.StreamHandler()          # Log to console
        ]
    )
    return logging.getLogger("BasicLogger")

def collect_answers_into_single_string(answers_txt : list[Path]):
    """
    collects all the existing answers and strings them into a single string

    answers_txt: List of Paths to answer files.
    """
    answers_content = [answer.read_text(encoding="utf-8") for answer in answers_txt]
    all_answers = " ".join(answers_content)

    return all_answers
