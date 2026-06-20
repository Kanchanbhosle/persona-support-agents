# src/escalator.py

CONFIDENCE_THRESHOLD = 0.20


def check_escalation(query, persona, score):

    query_lower = query.lower()

    sensitive_keywords = [
        "refund",
        "duplicate charge",
        "duplicate charges",
        "unauthorized charge",
        "unauthorized charges",
        "legal action",
        "lawsuit",
        "close account",
        "delete account",
        "cancel account"
    ]

    sensitive_issue = any(
        keyword in query_lower
        for keyword in sensitive_keywords
    )

    # Escalate if retrieval confidence is low
    if score < CONFIDENCE_THRESHOLD:

        return {
            "escalate": True,
            "handoff_summary": {
                "persona": persona,
                "issue_summary": query,
                "reason": "Low retrieval confidence",
                "retrieved_documents": [],
                "attempted_actions": [
                    "Knowledge base search performed"
                ],
                "recommended_next_step":
                "Human review required"
            }
        }

    # Escalate if sensitive issue detected
    if sensitive_issue:

        return {
            "escalate": True,
            "handoff_summary": {
                "persona": persona,
                "issue_summary": query,
                "reason": "Sensitive customer request",
                "retrieved_documents": [],
                "attempted_actions": [
                    "Knowledge base search performed"
                ],
                "recommended_next_step":
                "Assign to human support specialist"
            }
        }

    # No escalation
    return {
        "escalate": False,
        "handoff_summary": None
    }