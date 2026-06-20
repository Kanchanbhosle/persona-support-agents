# 🤖 Persona Adaptive Support Agent

An AI-powered customer support assistant that understands user personas, retrieves relevant information from a knowledge base, generates adaptive responses using Generative AI, and escalates complex queries to human support when required.

This project combines **Generative AI, Retrieval-Augmented Generation (RAG), Vector Search, and Persona Detection** to create an intelligent customer support experience.

---

# 🌟 Project Overview

Traditional support systems provide the same response to every customer. This project creates a smarter support agent that:

- Understands who the user is
- Identifies the user's intent
- Retrieves relevant knowledge from documents
- Generates personalized AI responses
- Decides when human intervention is needed

The system adapts its communication style based on customer persona.

---

# 🚀 Features

## 🧠 Persona Detection

Automatically detects the type of customer asking the question.

Example personas:

- 👨‍💻 Developer
- 👩‍💼 Business User
- 🆕 Beginner User
- 🛠️ Technical Support User

Responses are customized according to the detected persona.

---

## 📚 Retrieval-Augmented Generation (RAG)

The system uses RAG architecture to provide accurate answers.

Workflow:

1. User asks a question
2. Relevant documents are searched from the knowledge base
3. Retrieved information is passed to Gemini AI
4. AI generates a context-aware response

---

## 🔎 Knowledge Base Search

- Document ingestion
- Text chunking
- Embedding generation
- Semantic similarity search
- Context retrieval

Vector database used:

- ChromaDB

---

## 🤖 Generative AI Response

Powered by:

- Google Gemini API

Capabilities:

- Natural language understanding
- Context-aware answers
- Personalized responses
- Technical explanations

---

## 🚨 Human Escalation

The system identifies queries that require human assistance.

Examples:

- Complex technical issues
- Unresolved customer problems
- Sensitive support requests

---

## 🌐 Interactive Web Application

Built using Streamlit.

Users can:

- Enter support questions
- View detected persona
- See retrieved information
- Get AI-generated responses

---

# 🏗️ System Architecture


```
                 User Query
                     |
                     ↓
          Persona Detection Module
                     |
                     ↓
        Knowledge Base Retrieval (RAG)
                     |
                     ↓
          Vector Database Search
                     |
                     ↓
             Gemini AI Model
                     |
                     ↓
        Adaptive Support Response
                     |
                     ↓
          Human Escalation Decision
```

---

# 🛠️ Tech Stack

## Programming Language

- Python

## Frontend

- Streamlit

## Artificial Intelligence

- Google Gemini API
- Generative AI
- Retrieval-Augmented Generation (RAG)
- Natural Language Processing

## Database

- ChromaDB Vector Database

## Development Tools

- Git
- GitHub
- Virtual Environment

---

# 📂 Project Structure


```
persona-support-agents/

│
├── app.py
│   └── Streamlit application interface
│
├── ingest.py
│   └── Document processing and embedding generation
│
├── test_gemini.py
│   └── Gemini API testing
│
├── requirements.txt
│   └── Required Python packages
│
├── README.md
│   └── Project documentation
│
├── data/
│   └── Knowledge base documents
│
├── src/
│   ├── persona.py
│   │   └── Persona detection logic
│   │
│   ├── retrieval.py
│   │   └── Document retrieval logic
│   │
│   └── response.py
│       └── AI response generation
│
└── chroma_db/
    └── Vector database storage
```

---

# ⚙️ Installation and Setup

## 1. Clone Repository


```bash
git clone https://github.com/Kanchanbhosle/persona-support-agents.git
```

---

## 2. Navigate to Project


```bash
cd persona-support-agents
```

---

## 3. Create Virtual Environment


```bash
python -m venv venv
```

Activate environment:

### Windows

```bash
venv\Scripts\activate
```

---

## 4. Install Dependencies


```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Configuration

Create a `.env` file:


```
GEMINI_API_KEY=your_gemini_api_key
```

Replace:

```
your_gemini_api_key
```

with your actual Gemini API key.

---

# 📖 Prepare Knowledge Base

Run the ingestion script:


```bash
python ingest.py
```

This process:

- Reads documents
- Creates embeddings
- Stores vectors in ChromaDB

---

# ▶️ Run Application


Start Streamlit:


```bash
streamlit run app.py
```

Application will run at:


```
http://localhost:8501
```

---

# 💡 Example Usage


### User Input:

```
Explain API authentication header requirements
```


### System Output:


```
Detected Persona:
Developer


Retrieved Knowledge:
API authentication documentation


AI Response:
Detailed explanation of authentication headers,
security practices, and implementation guidance.
```

---

# 🔄 How the Application Works


### Step 1:
User enters a support question.


### Step 2:
AI analyzes the query and identifies user persona.


### Step 3:
Relevant documents are retrieved from ChromaDB.


### Step 4:
Gemini AI generates a personalized response.


### Step 5:
System checks whether escalation is required.

---

# 🌍 Deployment

The application can be deployed using:

- Streamlit Community Cloud
- Cloud platforms supporting Python applications

For Streamlit deployment:

1. Push code to GitHub
2. Connect repository with Streamlit Cloud
3. Add Gemini API key in Secrets
4. Deploy application

---

# 🔐 Security

Implemented security practices:

- API keys stored using environment variables
- `.env` excluded from GitHub
- Sensitive files ignored using `.gitignore`

---

# 🚀 Future Enhancements

Future improvements:

- Add user authentication
- Add conversation memory
- Add multilingual support
- Improve persona classification model
- Add analytics dashboard
- Add voice-based support
- Integrate more LLM providers

---

# 👩‍💻 Author

## Kanchan Bhosle

B.Tech Computer Science Engineering  
Specialization: Cyber Security


### Skills

- Python
- JavaScript
- React JS
- MERN Stack
- SQL
- Generative AI
- RAG Applications
- AI Agent Development

---

# 🙏 Acknowledgement

This project was developed to explore practical applications of:

- Generative AI
- AI Agents
- Retrieval-Augmented Generation
- Intelligent Customer Support Automation

---

# ⭐ If you like this project

Give this repository a star ⭐ and feel free to explore the implementation.



git add README.md
git commit -m "Added project documentation"
git push
