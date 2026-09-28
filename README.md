# MyPaddi Chatbot

## WHAT IT DOES

MyPaddi is a simple rule-based chatbot that allows users to have a basic conversation through the terminal. It recognizes different types of messages, such as greetings, questions about its name, time-related questions, jokes, and goodbyes, and responds with a randomly selected response.

For time-related questions, MyPaddi gets the current time and inserts it into a randomly selected response template.

MyPaddi processes user input by cleaning and normalizing the text before matching it against its supported intents.

## WHY I BUILT THIS

I built MyPaddi as a way to practice Python and learn how the different concepts I have learned can work together in a real project.

This project is my starting point for building more capable conversational applications.

## SUPPORTED INTENTS

* `greetings` — Example: `"hi"`
* `ask_name` — Example: `"what is your name"`
* `ask_time` — Example: `"what is the time"`
* `joke` — Example: `"tell me a joke"`
* `goodbye` — Example: `"bye"`

## HOW IT PROCESSES USER INPUT

Before matching an intent, MyPaddi cleans the user's input by:

* Converting the text to lowercase.
* Removing leading and trailing whitespace.
* Removing punctuation.

The cleaned input is then split into individual words.

### Sliding-Window Intent Matching

MyPaddi uses a sliding-window approach to match phrases.

Instead of checking whether a phrase simply exists somewhere inside the user's text as a sequence of characters, the chatbot compares complete words in the correct order.

For example, the phrase:

```text
see you
```

is treated as:

```text
["see", "you"]
```

If the user enters:

```text
ok see you later
```

MyPaddi checks consecutive groups of words:

```text
["ok", "see"]
["see", "you"]
["you", "later"]
```

When the window matches the phrase exactly, the corresponding intent is returned.

This prevents incorrect matches such as:

```text
i see youtube videos
```

being interpreted as the `goodbye` intent because `"see you"` happens to appear across the characters in `"youtube"`.

## HOW TO RUN IT

Make sure Python is installed, then run:

```bash
python main.py
```

The project uses only Python's standard library. It uses modules such as `string`, `random`, and `datetime`, which are included with Python, so no external packages need to be installed with `pip`.

## HOW TO EXIT

The conversation ends when the user enters:

* `exit`
* `bye`
* `quit`

## PROJECT STRUCTURE

* `main.py` — Runs the chatbot conversation loop, handles user input, checks exit phrases, and counts exchanges.
* `nlp_utils.py` — Cleans user input, performs word-based sliding-window intent matching, and extracts the user's name.
* `intents.py` — Contains `INTENT_MAP`, which defines the phrases that trigger each intent.
* `responses.py` — Contains `RESPONSE_MAP` and `get_response()`, which selects a random response for the matched intent, generates the current time for `ask_time`, personalizes greetings, and provides a fallback when no intent is matched.

## CURRENT INTENT-MATCHING LOGIC

The `match_intent()` function currently works by:

1. Splitting the cleaned user input into words.
2. Splitting each supported phrase into words.
3. Determining the number of words in the phrase.
4. Moving a window across the user's words.
5. Comparing each window with the phrase.
6. Returning the corresponding intent when an exact word sequence is found.
7. Returning `None` if no phrase matches.

This gives MyPaddi more reliable phrase matching than the previous substring-based approach.

## KNOWN LIMITATIONS

* **First-match-wins intent matching:** `match_intent()` returns the first matching intent it finds. If a message could match multiple intents, the chatbot does not compare the matches to determine which one is most appropriate.
* **Limited understanding:** The chatbot only recognizes phrases that are included in `INTENT_MAP`.
* **Session-only memory:** The chatbot can remember the user's name during the current session, but this information is not saved after the program closes.
* **Basic name extraction:** The chatbot uses a simple rule to identify when a user provides their name.
* **Basic fallback:** When the chatbot cannot identify an intent, it uses a generic fallback response rather than understanding the user's message in context.
* **Exact phrase matching:** The sliding-window system requires the words in a supported phrase to appear consecutively and in the same order.

## PROJECT DIRECTION

MyPaddi currently represents my first milestone in building a conversational application. I am using this project to understand how a chatbot works from the ground up, starting with Python fundamentals, rule-based logic, input processing, phrase matching, and simple conversation state.

As I continue learning, the project will evolve alongside my skills.
