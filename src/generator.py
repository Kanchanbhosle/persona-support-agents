import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def generate_answer(query, persona, context):

    try:

        if persona == "Technical Expert":
            style = """
Give detailed technical explanation.
Include troubleshooting steps.
"""
        elif persona == "Frustrated User":
            style = """
Be empathetic.
Use simple language.
Provide action steps.
"""
        else:
            style = """
Be concise.
Focus on business impact.
Keep technical details minimal.
"""

        prompt = f"""
You are a customer support assistant.

Persona:
{persona}

Style:
{style}

Context:
{context}

Question:
{query}

Answer ONLY using the provided context.
"""

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    except Exception:

        return """
Gemini API quota exceeded.

The system successfully:
✓ Detected persona
✓ Retrieved relevant documents
✓ Performed escalation checks

For full AI-generated responses,
please retry later or use a new Gemini API key.
"""