# Flask Chatbot with MySQL Database

A chatbot built using Flask and MySQL, capable of answering user questions and learning new responses through a dedicated endpoint.

## Features

- Answering Questions
The chatbot compares user input with questions stored in the database and returns the best matching response.

- Learning New Responses
Users can teach the chatbot new question-response pairs through a dedicated /teach endpoint.

- MySQL Database Integration
Questions and answers are stored and retrieved from a MySQL database.

- Similarity Matching
The bot uses fuzzy matching to find the most similar question in the database if an exact match isn't found.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Future Improvements](#future-improvements)
- [Contributing](#contributing)

## Technologies Used
- Flask: Web framework for handling API routes.
- MySQL: Relational database for storing question-answer pairs.
- Python: Core language for development.
- Difflib: Library for finding the closest string matches.
- CORS: Enables Cross-Origin Resource Sharing for API usage.

## Installation
Follow these steps to set up the project locally:

1. Clone the repository:
   git clone https://github.com/crifree/chatbot-api-database.git
   cd chatbot-api-database

2. Create and activate a virtual environment:
   python -m venv venv
   source venv/bin/activate # For Windows: venv\Scripts\activate

3. Set Up the Database:
   Create a MySQL database using the provided chat.sql script

4. Install dependencies:
   pip install -r requirements.txt

5. Configure Database Connection
   Modify the DB_CONFIG in conn.py to match your MySQL credentials

6. Start the server:
   python main.py
   The API will be available at http://127.0.0.1:5000.

## Usage
API Endpoints:

1. POST /api/chatbot
Sends a question to the chatbot and receives a response.

Example request body:

{
  "question": "What is your name?"
}

Response (Example):

{
   "answer": "I do not have any!"
}

2. POST /api/teach
Teaches the chatbot a new question and answer pair.

Example request body:

{
  "question": "What is Flask?",
  "answer": "Flask is a micro web framework for Python."
}

## Project Structure

.
├── main.py                # Entry point for the Flask app
├── app
│   ├── chat.sql           # database
│   ├── __init__.py        # App initialization
│   ├── routes             # Contains API routes
│   │   ├── conn.py        # connection to database
│   │   └── chatbot.py     # Chatbot logic
│   ├── services           # Placeholder for service logic
│   ├── static             # Static files (CSS, JS, images)
│   └─── templates          # HTML templates
│   
│   README.md
└── requirements.txt       # Python dependencies


## Future Improvements
1. Implement advanced NLP for better question matching.
2. Add Docker support for easy deployment.
3. Enhance the frontend with more features and better UI.


## Contributing
Contributions are welcome! Feel free to fork the repository and submit a pull request.

How to contribute:
   Fork the repository
   Create a new branch for your feature/bugfix
   Commit your changes
   Push to your fork and create a pull request