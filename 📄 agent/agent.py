import json

def interpret_request(text):

    text = text.lower()

    if "book" in text:
        intent = "book"
    elif "cancel" in text:
        intent = "cancel"
    elif "reschedule" in text:
        intent = "reschedule"
    else:
        intent = "unknown"

    return {
        "intent": intent,
        "doctor": "general",
        "date": "tomorrow"
    }
