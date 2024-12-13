import unittest
from difflib import get_close_matches


def load_knowledge(file_path: str) -> dict:
       with open(file_path, 'r') as file:
             data: dict = json.load(file)
       return data
     
     
def save_knowledge(file_path: str, data: dict):
      with open(file_path, 'w') as file:
            json.dump(data, file, indent=2)
      

def find_best_match(user_question: str, questions: list[str]) -> str | None:
      matches: list = get_close_matches(user_question, questions, n=1, cutoff=0.6)
      return matches[0] if matches else None
      

def get_answer_for_question(question: str, knowledge: dict) -> str | None:
      for q in knowledge['questions']:
            if q['question'] == question:
                  return q['answer']
      return None


class chatbot_test(Unittest.TestCase):

      def test_load_knowledge(self):