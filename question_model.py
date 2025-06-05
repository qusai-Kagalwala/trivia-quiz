# Day 17 - Angela Yu 100 Days of Code
# Question Model Class - Data structure for quiz questions

class Question:
    """
    A simple class to represent a quiz question with its text and correct answer.
    This class serves as a data model for storing question information.
    """

    def __init__(self, q_text, q_answer):
        """
        Initialize a Question object with question text and correct answer.

        Args:
            q_text (str): The question text to be displayed to the user
            q_answer (str): The correct answer for this question
        """
        self.text = q_text  # Store the question text
        self.answer = q_answer  # Store the correct answer