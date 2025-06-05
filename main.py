# Day 17 - Angela Yu 100 Days of Code
# Quiz Game Application - Main Module

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Create an empty list to store Question objects
question_bank = []

# Loop through the question data and create Question objects
for question in question_data:
   question_text = question["question"]
   question_answer = question["correct_answer"]
   new_question = Question(question_text, question_answer)
   question_bank.append(new_question)

# Create a QuizBrain object with the question bank
quiz = QuizBrain(question_bank)

# Main quiz loop - continues until no more questions remain
while quiz.still_has_questions():
   quiz.next_question()

# Display final results when quiz is complete
print("You've completed the quiz.")
print(f"Your final score was : {quiz.score} / {quiz.question_number}")