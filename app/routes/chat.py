import json
from difflib import get_close_matches
from flask import jsonify

def load_knowledge(file_path: str) -> dict:
      try:
            with open(file_path, 'r') as file:
                  data: dict = json.load(file)
            return data
      except FileNotFoundError:
            print(f'Error: the file "{file_path}" was not found')
            return {'questions':[]}
      except json.JSONDecodeError:
            print(f'Error: the file "{file_path}" is not a valid json file')
            return {'questions':[]}


def save_knowledge(file_path: str, data: dict):
      try:
            with open(file_path, 'w') as file:
                  json.dump(data, file, indent=2)
      except Exception as e:
            print(f'Error: unable to save knowledge to "{file_path}". {e}')
     

def find_best_match(user_question: str, questions: list[str]) -> str | None:
      try:
            matches: list = get_close_matches(user_question, questions, n=1, cutoff=0.6)
            return matches[0] if matches else None
      except Exception as e:
            print(f'An issue occurred while finding the best match. {e}')
            return None

def get_answer_for_question(question: str, knowledge: dict) -> str | None:
      try:
            for q in knowledge['questions']:
                  if q['question'] == question:
                        return q['answer']
      except KeyError as e:
            print(f"Error: Missing key in knowledge data: {e}. Expected a key 'questions'.")
      return None

def chatbot():
      knowledge: dict = load_knowledge('knowledge.json')

      try:
            while True:
                  user_input: str = input('You: ')

                  if user_input.lower() == 'quit':
                        break

                  best_match: str | None = find_best_match(user_input, [q['question'] for q in knowledge['questions']])

                  if best_match:
                        answer: str = get_answer_for_question(best_match, knowledge)
                        return jsonify({'response': answer})
                  else:
                        return jsonify({'response': 'bot: i don\'t know the answer. Can you teach me?'})
                        new_answer: str = input('type the answer or "skip" to skip: ')

                        if new_answer.lower() != 'skip':
                              knowledge['questions'].append({'question': user_input, 'answer': new_answer})
                              save_knowledge('knowledge.json', knowledge)
                              return jsonify({'response': 'bot: Thank you! I learned something new!'})
      except KeyboardInterrupt:
            print("\nBot: Chat session ended by user.")
      except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == '__main__':
      chatbot()