# Chatbot API Project

A simple chatbot API that allows users to interact with a chatbot by sending questions and teaching it new responses.

## Features
- Responds to user questions based on a JSON knowledge base.
- Allows users to teach the chatbot new questions and answers.
- Built with Flask and supports RESTful API operations.
- The bot can dynamically learn new responses through user input.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Future Improvements](#future-improvements)
- [Contributing](#contributing)

## Technologies Used
- Python 3.11
- Flask (Micro Web Framework)
- JSON for storing knowledge base

## Installation
Follow these steps to set up the project locally:

1. Clone the repository:
   git clone https://github.com/crifree/chatbot-api.git
   cd chatbot-api

2. Create and activate a virtual environment:
   python -m venv venv
   source venv/bin/activate # For Windows: venv\Scripts\activate

3. Install dependencies:
   pip install -r requirements.txt

4. Start the server:
   python main.py
   The API will be available at http://127.0.0.1:5000.

## Usage
API Endpoints:

1. GET /api/chatbot
Sends a question to the chatbot and receives a response.
Example request body:

{
  "question": "What is your name?"
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
│   ├── __init__.py        # App initialization
│   ├── routes             # Contains API routes
│   │   ├── chatbot.py     # Chatbot logic
│   │   └── knowledge.json # JSON knowledge base
│   ├── services           # Placeholder for service logic
│   ├── static             # Static files (CSS, JS, images)
│   └─── templates          # HTML templates
│   
└── requirements.txt       # Python dependencies


## Future Improvements
1. Add support for a database (e.g., SQLite, PostgreSQL) to replace the JSON knowledge base.
2. Implement advanced NLP for better question matching.
3. Add Docker support for easy deployment.
4. Enhance the frontend with more features and better UI.


## Contributing
Contributions are welcome! Feel free to fork the repository and submit a pull request.

How to contribute:
   Fork the repository
   Create a new branch for your feature/bugfix
   Commit your changes
   Push to your fork and create a pull request