import time
import json

questions_file = open('questions.json', encoding='utf-8')
questions = json.load(questions_file)
questions_file.close()

def countdown(t): 
  while t:
    mins, secs = divmod(t, 60)
    timer = '{:02d}:{:02d}'.format(mins, secs)
    print(timer, end="\r")
    time.sleep(1)
    t -= 1

def print_answers(question) :
  for index, answer in enumerate(question["answers"]) :
    print(f'{index+1}: {answer}', end=" ", sep="|")
  print("")

def check_answer(question, answer):
  if(question["correct_answer"] == answer):
    print('Réponse correct ✅')
    return True
  else:
    print('Mauvaise réponse ❌')
    return False


def game():
  choix = ""
  score = 0
  for question in questions:
    # countdown(question["timer"])
    print(f'Question {question["number"]}: {question["text"]}')
    print_answers(question)
    choix = input(f'Donner votre réponse: ')
    choix = int(choix)
    print(f'Réponse N°{choix}')
    result = check_answer(question, choix)
    if(result):
      score += 1

  print(f'Score final {score}/{len(questions)}')


# start the game
game()