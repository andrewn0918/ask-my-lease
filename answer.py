from dotenv import load_dotenv
import anthropic

# loads .env file and creates the client
load_dotenv()
client = anthropic.Client()