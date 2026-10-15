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


scored = [q for q in questions if q["pages"]]
hits_count = 0
for item in scored:
    returned = [h["page_number"] for h in search(item["question"], n_results=K)]
    if any(p in returned for p in item["pages"]):
        hits_count += 1

print(f"recall@{K}: {hits_count}/{len(scored)} = {hits_count / len(scored):.0%}")