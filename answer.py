from dotenv import load_dotenv
import anthropic

# loads .env file and creates the client
load_dotenv()
client = anthropic.Client()

# takes a question and a list of hits (from search) and returns an answer
def answer_question(question, hits):
    # loops over hits and turns each into text
    context = "\n\n".join(
        f"[Page {h['page_number']}]\n{h['text']}" for h in hits
    )

    # instructions
    prompt = (
        "Answer the question using ONLY the lease excerpts below. "
        "Cite the page number(s) you used, like (page 7). "
        "If the excerpts do not contain the answer, reply exactly: "
        "'Not found in your lease.'\n\n"
        f"Excerpts:\n{context}\n\n"
        f"Question: {question}"
    )

    # calling claude to generate answer
    response = client.messages.create(
        model="claude-sonnet-5-5",
        max_tokens=2000,
        messages=[{"role": "user", "content": prompt}],
    )

    # loops through every block (skips thinking ones) and finds the block with text"
    texts = [block.text for block in response.content if block.type == "text"]
    #print([block.type for block in response.content])
    return "\n".join(texts)