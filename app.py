import streamlit as st

from src.classifier import classify_persona
from src.rag_pipeline import search
from src.generator import generate_answer
from src.escalator import check_escalation


st.set_page_config(
    page_title="Persona Adaptive Support Agent",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Persona Adaptive Support Agent")

st.write(
    "Ask a support question and the AI will detect the customer persona, "
    "retrieve relevant knowledge base documents, generate an adaptive response, "
    "and escalate to a human agent when required."
)

query = st.text_input(
    "Ask your support question"
)


if query:

    # =========================
    # Persona Classification
    # =========================

    persona = classify_persona(query)

    st.subheader("👤 Detected Persona")
    st.json(persona)

    # =========================
    # Document Retrieval
    # =========================

    docs = search(query)

    st.subheader("📚 Retrieved Sources")

    try:

        sources = docs["metadatas"][0]

        for source in sources:
            st.write("📄", source["source"])

    except Exception:
        st.warning("No sources found.")

    # =========================
    # Build Context
    # =========================

    try:

        context = "\n\n".join(
            docs["documents"][0]
        )

    except Exception:

        context = ""

    # =========================
    # Retrieval Confidence
    # =========================

    try:

        distance = docs["distances"][0][0]

        score = round(
            max(0, 1 - distance),
            2
        )

    except Exception:

        score = 1.0

    st.subheader("📊 Retrieval Confidence")
    st.write(score)

    # =========================
    # Escalation Check
    # =========================

    escalation = check_escalation(
        query=query,
        persona=persona["persona"],
        score=score
    )

    # =========================
    # Human Escalation
    # =========================

    if escalation["escalate"]:

        st.error(
            "🚨 Escalated to Human Support"
        )

        st.subheader(
            "Human Handoff Summary"
        )

        st.json(
            escalation["handoff_summary"]
        )

    # =========================
    # AI Response
    # =========================

    else:

        answer = generate_answer(
            query=query,
            persona=persona["persona"],
            context=context
        )

        st.subheader("🤖 AI Response")

        st.write(answer)

        st.success(
            "Response generated successfully."
        )