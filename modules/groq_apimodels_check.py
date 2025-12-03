import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")
if not API_KEY:
    raise RuntimeError("Missing GROQ_API_KEY in .env")

client = Groq(api_key=API_KEY)

def list_models():
    print("Fetching available Groq models...\n")
    models = client.models.list()

    for model in models.data:
        print(model.id)

if __name__ == "__main__":
    list_models()