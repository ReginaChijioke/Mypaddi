from nlp_utils import clean_input, match_intent, extract_name
from responses import get_response, RESPONSE_MAP
from intents import INTENT_MAP

exit_phrases = {"exit", "bye", "quit"}
exchange_count = 0
user_name = None 
while True:
    raw_input = input("You: ")
    cleaned = clean_input(raw_input)
    if cleaned in exit_phrases:
        print("see ya")
        break

    possible_name = extract_name(cleaned)
    if possible_name is not None:
        user_name = possible_name
        print(f"Nice to meet you, {user_name}")
        continue

    matched_intent = match_intent(cleaned, INTENT_MAP)
    bot_response = get_response(matched_intent, RESPONSE_MAP, user_name)
    print("Bot:", bot_response)
    exchange_count += 1
print(exchange_count)

