from answer import answer_question
from store import search

question = "What happens if I pay rent late?"
hit_results = search(question)

'''
for hit in hit_results:
    print(f"--- Page {hit['page_number']} ---")
    print(hit["text"][:300])
    print()
'''

print(answer_question(question, hit_results))