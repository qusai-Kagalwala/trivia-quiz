# Day 17 - Angela Yu 100 Days of Code
# Quiz Brain Class - Manages quiz game logic and flow

class QuizBrain:
    """
    A class to manage the quiz game logic, including question navigation,
    user input handling, answer checking, and score tracking.
    """

    def __init__(self, q_list):
        """
        Initialize the QuizBrain with a list of questions.

        Args:
            q_list: List of Question objects containing quiz questions
        """
        self.question_number = 0  # Track current question position (starts at 0)
        self.score = 0  # Track user's correct answers
        self.question_list = q_list  # Store the list of questions

    def still_has_questions(self):
        """
        Check if there are more questions remaining in the quiz.

        Returns:
            bool: True if more questions exist, False if quiz is complete
        """
        return self.question_number < len(self.question_list)

    def next_question(self):
        """
        Display the next question and get user input.
        Increments question number and processes the user's answer.
        """
        # Get the current question object from the list
        current_question = self.question_list[self.question_number]

        # Increment question number for display (human-readable numbering)
        self.question_number += 1

        # Prompt user for answer and get their input
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True / False): ")

        # Check if the user's answer is correct
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        """
        Compare user's answer with the correct answer and update score.
        Provides feedback and displays current progress.

        Args:
            user_answer (str): The user's input answer
            correct_answer (str): The correct answer for the question
        """
        # Case-insensitive comparison of answers
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")

        # Display the correct answer for learning
        print(f"The correct answer was: {correct_answer}.")

        # Show current progress to the user
        print(f"Your current score is: {self.score} / {self.question_number}")
        print("\n")  # Add blank line for better readability