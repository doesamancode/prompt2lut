import re

def normalize_text(text):
    return text.lower().strip()

def split_phrases(text):
    text = normalize_text(text)
    phrases = re.split(r",| and ", text)
    return [p.strip() for p in phrases if p.strip()]

print(split_phrases("warm shadows, slightly muted highlights"))