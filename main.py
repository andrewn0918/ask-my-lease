from answer import answer_question
from store import search

question = "What happens if I pay rent late?"
hit_results = search(question)

print(answer_question(question, hit_results))