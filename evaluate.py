import json
from store import search

K = 3

with open("questions.json") as f:
    questions = json.load(f)

for item in questions:
    hits = search(item["question"], n_results = K)
    returned_pages = [hit["page_number"] for hit in hits]
    print(item["question"])
    print("expected: ", item["pages"])
    print("returned: ", returned_pages)
    print()