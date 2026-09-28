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
    input_words = cleaned_text.split()
    for matched_intent, phrase_list in intent_map.items():
        for phrase in phrase_list:
            phrase_split = phrase.split()
            phrase_word_count = len(phrase_split)
            for start in range(len(input_words) - phrase_word_count + 1):
                window = input_words[start:start + phrase_word_count]
                if window == phrase_split:
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

