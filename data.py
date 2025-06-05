# Day 17 - Angela Yu 100 Days of Code
# Question Data Module - Contains quiz questions from Open Trivia Database with HTML entities decoded

import html

# Raw question data retrieved from Open Trivia Database API
# Category: Science: Computers (Easy difficulty, True/False questions)
raw_question_data = [
    {
        "type": "boolean",
        "difficulty": "easy",
        "category": "Science: Computers",
        "question": "RAM stands for Random Access Memory.",
        "correct_answer": "True",
        "incorrect_answers": [
            "False"
        ]
    },
    {
        "type": "boolean",
        "difficulty": "easy",
        "category": "Science: Computers",
        "question": "JavaScript derives from a later version of Java",
        "correct_answer": "False",
        "incorrect_answers": [
            "True"
        ]
    },
    {
        "type": "boolean",
        "difficulty": "easy",
        "category": "Science: Computers",
        "question": "A Mac is not a PC",
        "correct_answer": "False",
        "incorrect_answers": [
            "True"
        ]
    },
    {
        "type": "boolean",
        "difficulty": "easy",
        "category": "Science: Computers",
        "question": "The Windows ME operating system was released in the year 2000.",
        "correct_answer": "True",
        "incorrect_answers": [
            "False"
        ]
    },
    {
        "type": "boolean",
        "difficulty": "easy",
        "category": "Science: Computers",
        "question": "Pointers were not used in the original C programming language; they were added later on in C++.",
        "correct_answer": "False",
        "incorrect_answers": [
            "True"
        ]
    },
    {
        "type": "boolean",
        "difficulty": "easy",
        "category": "Science: Computers",
        "question": "The programming language &quot;Python&quot; is based off a modified version of &quot;JavaScript&quot;.",
        "correct_answer": "False",
        "incorrect_answers": [
            "True"
        ]
    },
    {
        "type": "boolean",
        "difficulty": "easy",
        "category": "Science: Computers",
        "question": "Ada Lovelace is often considered the first computer programmer.",
        "correct_answer": "True",
        "incorrect_answers": [
            "False"
        ]
    },
    {
        "type": "boolean",
        "difficulty": "easy",
        "category": "Science: Computers",
        "question": "The logo for Snapchat is a Bell.",
        "correct_answer": "False",
        "incorrect_answers": [
            "True"
        ]
    },
    {
        "type": "boolean",
        "difficulty": "easy",
        "category": "Science: Computers",
        "question": "&quot;HTML&quot; stands for Hypertext Markup Language.",
        "correct_answer": "True",
        "incorrect_answers": [
            "False"
        ]
    },
    {
        "type": "boolean",
        "difficulty": "easy",
        "category": "Science: Computers",
        "question": "The first IBM PC was released in 1981.",
        "correct_answer": "True",
        "incorrect_answers": [
            "False"
        ]
    }
]

# Process the raw data to decode HTML entities for proper terminal display
question_data = []
for question in raw_question_data:
    # Create a copy of the question dictionary
    decoded_question = question.copy()

    # Decode HTML entities in the question text (&quot; becomes ", &amp; becomes &, etc.)
    decoded_question["question"] = html.unescape(question["question"])

    # Add the processed question to the final list
    question_data.append(decoded_question)