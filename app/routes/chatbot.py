from flask import Blueprint, jsonify, request
from flask_cors import CORS  # Importa CORS
from difflib import get_close_matches
import os
import json
from .conn import connection
import logging

logging.basicConfig(level=logging.DEBUG)  # Log di livello DEBUG e superiore
logger = logging.getLogger(__name__)

# Blueprint per il chatbot
chatbot = Blueprint('chatbot', __name__)
CORS(chatbot)  # Abilita CORS


def find_best_match(user_question: str, questions: list[str]) -> str | None:
      matches: list = get_close_matches(user_question, questions, n=1, cutoff=0.6)
      return matches[0] if matches else None


@chatbot.route('/chatbot', methods=['post'])
def chat_bot():

      user_input: str = request.json.get('message', '')

      if not user_input:
            return jsonify({'error': 'No message provided'}), 400

      try:
            db = connection()
            db.openConn()

            query = 'SELECT question, answer FROM qa WHERE question LIKE %s LIMIT 10'
            params = (f'%{user_input}%',)
            results = db.sqlQuery(query, params)

            if not results:
                  db.closeConn()
                  logger.debug('suca')
                  return jsonify({
                  'response': "I don't know the answer. Can you teach me? Or you can say skip to skip learning!",
                  'learn': True
                  })

            questions = [q[0] for q in results]
            qa_dict = {row[0]: row[1] for row in results}

            best_match = find_best_match(user_input, questions)

            if best_match:
                  answer = qa_dict.get(best_match)
                  db.closeConn()
                  return jsonify({'response': answer})
            else:
                  db.closeConn()
                  return jsonify({
                  'response': "I don't know the answer. Can you teach me? Or you can say skip to skip learning!",
                  'learn': True
                  })

      except Exception as e:
            print(f'errore durante la connessione {e}')           


@chatbot.route('/teach', methods=['POST'])
def teach():
      db = None
      try:
            db = connection()
            db.openConn()

            answer = request.json.get('answer', '') 
            question = request.json.get('question', '')

            if not question or not answer:
                  return jsonify({'error': 'Both question and answer must be provided'}), 400

            get_questions = 'SELECT question FROM qa WHERE question LIKE %s LIMIT 10'
            param = (f'%{question}%',)
            results = db.sqlQuery(get_questions, param)

            if any(q[0] == question for q in results):
                  return jsonify({'error': 'This question already exists in the knowledge base'}), 409

            insert_data = 'INSERT INTO qa (question, answer) VALUES (%s, %s)'
            params = (question, answer)
            db.sqlQuery(insert_data, params)

            return jsonify({'response': 'Thank you! I learned something new!'}), 201

      except Exception as e:
            return jsonify({'response': f'An unexpected error occurred: {e}'}), 500

      finally:
            if db is not None:
                  db.closeConn()

