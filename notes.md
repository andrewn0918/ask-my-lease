# Notes

# retrieval
- "Can I have a pet?" returned pages 17, 18, 18 --> valid
- "Does the building have a pool?" returned not found --> valid (refusal case)
- "How much is the security deposit?"  returned not found --> valid (refusal case)
- "When do I get my deposit back?" returned page 12 --> valid
- "What happens if I pay rent late?" returned page 10 --> valid


## Baseline (400-word chunks, no overlap, k=3)
recall@3 (for the 10 questions): 3/3 = 100% on 3 answerable questions (too few to trust)
recall@3: 8/10 = 80%