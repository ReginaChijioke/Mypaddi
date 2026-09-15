import string 
from intents import INTENT_MAP
def clean_input(raw_text):
    cleaned_text = None
    low = raw_text.lower()
    clean = low.strip()
    punctuation = clean.maketrans("", "", string.punctuation)
    cleaned_text = clean.translate(punctuation)
    return cleaned_text


def match_intent(cleaned_text, intent_map):
    for matched_intent, phrase_list in intent_map.items():
        for phrase in phrase_list:
            if phrase in cleaned_text:
                return matched_intent

    return None

def extract_name(cleaned_text):
    name_intro = ["my name is", "im ", "call me"]
    for phrase in name_intro:
        if phrase in cleaned_text:
            name = cleaned_text.split(phrase)
            cleaned_name = name[1]
            real_name = cleaned_name.strip()
            return real_name
    return None





