import os
import re
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# ----------- Text Cleaner (removes emojis, markdown, bullets, symbols) -----------
def clean_text(text):
    if not text:
        return ""

    # Remove emojis and non-standard characters
    text = re.sub(r'[^\w\s,.!?\'"]+', '', text)

    # Remove markdown formatting
    text = text.replace("**", "").replace("*", "").replace("_", "").replace("`", "")

    # Remove bullet characters
    text = text.replace("•", "").replace("-", "")

    # Clean multiple spaces
    text = re.sub(r"\s+", " ", text).strip()

    return text

# ------------------------ GROQ Request ------------------------
def ask_groq(prompt: str) -> str:
    try:
        response = client.chat.completions.create(
            model="openai/gpt-oss-120b",   # Working model
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )

        raw_text = response.choices[0].message.content
        return clean_text(raw_text)

    except Exception as e:
        return f"Error: {str(e)}"