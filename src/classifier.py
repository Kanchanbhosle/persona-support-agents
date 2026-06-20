import json
import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def classify_persona(message):

    try:

        prompt = f"""
Classify this support message into ONE persona.

Personas:
1. Technical Expert
2. Frustrated User
3. Business Executive

Return ONLY valid JSON:

{{
  "persona":"",
  "confidence":0.0,
  "reason":""
}}

Message:
{message}
"""

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return json.loads(response.text)

    except Exception:

        # fallback classification
        msg = message.lower()

        if any(word in msg for word in [
            "api",
            "token",
            "header",
            "database",
            "authentication",
            "endpoint",
            "code"
        ]):
            return {
                "persona": "Technical Expert",
                "confidence": 0.80,
                "reason": "Fallback keyword classification"
            }

        if any(word in msg for word in [
            "angry",
            "frustrated",
            "not working",
            "tried everything",
            "refund",
            "help"
        ]):
            return {
                "persona": "Frustrated User",
                "confidence": 0.80,
                "reason": "Fallback keyword classification"
            }

        return {
            "persona": "Business Executive",
            "confidence": 0.80,
            "reason": "Fallback keyword classification"
        }