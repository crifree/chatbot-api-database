from flask import Blueprint, jsonify, request
from flask_cors import CORS  # Importa CORS
from difflib import get_close_matches
import os
import json


# Blueprint per il chatbot
chatbot = Blueprint('chatbot', __name__)
CORS(chatbot)  # Abilita CORS

def load_knowledge(file_path: str) -> dict:
      full_path = os.path.join(os.path.dirname(__file__), file_path)
      with open(full_path, 'r') as file:
            data: dict = json.load(file)
      return data
     

def save_knowledge(file_path: str, data: dict):
      full_path = os.path.join(os.path.dirname(__file__), file_path)
      with open(full_path, 'w') as file:
            json.dump(data, file, indent=2)
      

def find_best_match(user_question: str, questions: list[str]) -> str | None:
      matches: list = get_close_matches(user_question, questions, n=1, cutoff=0.6)
      return matches[0] if matches else None
      

def get_answer_for_question(question: str, knowledge: dict) -> str | None:
      for q in knowledge['questions']:
            if q['question'] == question:
                  return q['answer']
      return None


@chatbot.route('/chatbot', methods=['POST'])
def chat_bot():
      try:
            knowledge: dict = load_knowledge('knowledge.json')
      except FileNotFoundError:
            return jsonify({"error": "knowledge file not found"}), 404
      except json.JSONDecodeError as e:
            return jsonify({"error": f"Knowledge file is invalid JSON. Details: {e}"}), 400
      except Exception as e:
                  return jsonify({"error": f"unexpected error: {e}"}), 500


      user_input: str = request.json.get('message', '')
      if not user_input:
            return jsonify({'error': 'No message provided'}), 400


      try:
            questions = [q['question'] for q in knowledge['questions']]
            best_match: str | None = find_best_match(user_input, questions)

            if best_match:
                  answer: str = get_answer_for_question(best_match, knowledge)
                  return jsonify({'response': answer})
            else:
                  return jsonify({'response': "I don't know the answer. Can you teach me? Or you can say skip to skip learning!", 'learn': True})
      except Exception as e:
            return jsonify({'response': f"An unexpected error occurred: {e}"}), 500


@chatbot.route('/teach', methods=['POST'])
def teach():
      try:
            knowledge = load_knowledge('knowledge.json')
            question = request.json.get('question', '')
            answer = request.json.get('answer', '')

            if not question or not answer:
                  return jsonify({'error': 'Both question and answer must be provided'}), 400

            if any(q['question'] == question for q in knowledge['questions']):
                  return jsonify({'error': 'This question already exists in the knowledge base'}), 409

            knowledge['questions'].append({'question': question, 'answer': answer})
            save_knowledge('knowledge.json', knowledge)

            
            return jsonify({'response': 'Thank you! I learned something new!'}), 201
      except Exception as e:
            return jsonify({'response': f"An unexpected error occurred: {e}"}), 500
