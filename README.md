MyPaddi Chatbot

WHAT IT DOES

MyPaddi is a conversational chatbot that started as a simple rule-based Python project and has evolved into an LLM-powered chatbot with a Streamlit chat interface.

The current version uses the **Groq API** to generate natural-language responses and maintains conversation history during a user's Streamlit session. This allows MyPaddi to respond to follow-up questions while using information from earlier messages in the conversation.

MyPaddi is designed to feel like a warm, patient conversational companion. Its behavior is guided by a system prompt that defines its personality, conversational style, and how it should respond to certain situations.

The original rule-based version was developed separately and now lives in a different repository.

---

WHY I BUILT THIS

I built MyPaddi as a way to practice Python and understand how different concepts can work together in a real project.

The project started as a rule-based chatbot where I practiced:

* Functions
* Loops
* Conditionals
* Strings
* Lists and dictionaries
* Input processing
* Intent matching
* Conversation state

As I learned more, I expanded MyPaddi into an LLM-powered application to explore:

* APIs
* HTTP requests and responses
* JSON-based API communication
* API authentication
* Environment variables
* Conversation history
* LLM-powered applications
* Streamlit
* Session state
* Prompt design

MyPaddi is becoming a practical learning project for understanding how conversational applications are built rather than simply being a chatbot project.

---

CURRENT VERSION

The current version of MyPaddi uses:

* **Python** — Core programming language
* **Groq API** — Provides the large language model
* **Streamlit** — Provides the web-based chat interface
* **python-dotenv** — Loads the API key from a `.env` file
* **Streamlit Session State** — Stores conversation history during a session

The current application sends the conversation history to the Groq API whenever the user sends a new message.

The model receives messages using the standard conversation roles:

```text
system
user
assistant
```

The system message contains MyPaddi's personality and behavioral instructions, while user and assistant messages are added to the conversation history as the conversation continues.

---

HOW THE CURRENT CHATBOT WORKS

The basic flow is:

```text
User enters a message
        ↓
Streamlit receives the message
        ↓
Message is added to conversation history
        ↓
Conversation history is sent to Groq
        ↓
Groq generates a response
        ↓
Assistant response is added to conversation history
        ↓
Response is displayed in the chat
```

Because the conversation history is stored in `st.session_state`, MyPaddi can use information from previous messages during the current session.

For example:

```text
User: My name is Reggie

MyPaddi: Nice to meet you, Reggie!

User: What is my name?

MyPaddi: Your name is Reggie.
```

The model can answer the second question because the previous conversation is included in the history sent to the API.

---

CONVERSATION HISTORY

The chatbot stores the conversation as a list of message dictionaries.

Conceptually, the history looks like:

```text
[
    {"role": "system", "content": "..."},
    {"role": "user", "content": "My name is Reggie"},
    {"role": "assistant", "content": "Nice to meet you, Reggie!"},
    {"role": "user", "content": "What is my name?"}
]
```

The entire conversation history is sent to the model when generating a new response.

This is important because the API does not automatically remember previous messages between requests. MyPaddi provides the previous conversation as part of each new request.

---

SYSTEM PROMPT

MyPaddi's behavior is controlled by a system prompt.

The current prompt instructs MyPaddi to:

* Be warm, patient, and conversational.
* Make users feel heard and not judged.
* Identify itself as MyPaddi when asked its name.
* Distinguish between MyPaddi's name and the user's name.
* Use a user's previously provided name when asked about their name.
* Avoid claiming to be a licensed or certified therapist.
* Encourage qualified professional help when a conversation suggests serious distress or a situation beyond everyday support.
* Keep everyday conversations natural and supportive.

The system prompt allows the chatbot's behavior to be changed without having to hard-code every possible response.

---

STREAMLIT INTERFACE

The current version uses Streamlit to provide a web-based chat interface.

Important Streamlit features used include:

* `st.chat_input()` — receives messages from the user.
* `st.chat_message()` — displays user and assistant messages as chat bubbles.
* `st.session_state` — preserves conversation history while the session is active.
* `st.write()` — displays text inside the application.

The application is no longer limited to a terminal interface.

---

SECURE API KEY HANDLING

The Groq API key is not stored directly in the Python source code.

MyPaddi uses a `.env` file to store the API key and `python-dotenv` to load it into the environment.

The project also uses `.gitignore` to prevent the `.env` file from being committed to Git.

The API key should never be placed directly in the source code or shared publicly.

---

THE ORIGINAL RULE-BASED VERSION

MyPaddi originally began as a rule-based terminal chatbot.

That version used predefined intents and responses and included features such as:

* Greeting detection
* Name-related questions
* Time-related questions
* Jokes
* Goodbye detection
* Input cleaning
* Word-based sliding-window intent matching
* Basic name extraction
* Session-based name personalization

The rule-based version also solved a substring-matching problem where phrases such as `"see you"` could incorrectly match text such as `"youtube"`.

That version is now maintained in a **separate repository** and represents the foundation of the current project.

The current repository focuses on the next stage of MyPaddi: using an LLM and a web interface to create a more flexible conversational experience.

---

PROJECT STRUCTURE

The current repository contains the LLM-powered version of MyPaddi.

The main components are:

* **Streamlit application** — Provides the web-based chat interface.
* **Groq integration** — Sends conversation history to the Groq API and receives generated responses.
* **System prompt** — Defines MyPaddi's personality and behavioral instructions.
* **Conversation history** — Stores the current conversation using Streamlit session state.
* **`.env`** — Stores the Groq API key locally and is excluded from Git.
* **`.gitignore`** — Prevents sensitive and unnecessary files from being tracked.

The original rule-based chatbot is maintained separately in another repository.

---

CURRENT PROGRESS

The current version has successfully implemented:

* [x] LLM-powered responses
* [x] Groq API connection
* [x] Secure API key loading with environment variables
* [x] `.env` and `.gitignore` setup
* [x] Conversation history
* [x] System prompt
* [x] Streamlit chat interface
* [x] Streamlit session state
* [x] User and assistant chat bubbles
* [x] Context-aware follow-up conversations
* [x] Basic distinction between the user's name and MyPaddi's name
* [x] System-prompt-based supportive and safety-oriented behavior

The original rule-based chatbot was completed separately before this version.

---

KNOWN LIMITATIONS

The current version is still a learning project and has several limitations.

Session-only memory

Conversation history currently exists only during the active Streamlit session.

If the session ends, MyPaddi does not have permanent memory of the previous conversation.

No database

The chatbot does not currently use a database to permanently store users or conversations.

API dependency

The current chatbot depends on the Groq API to generate responses. If the API is unavailable or the application cannot access it, the LLM-powered functionality will not work.

Safety fallback

MyPaddi's safety behavior is currently guided by the system prompt. It has been tested with serious support-seeking scenarios, but there is currently no hardcoded keyword-based safety layer acting as a backup.

This means that if the LLM fails to follow the system prompt's safety instructions, there is no separate application-level fallback mechanism to catch the situation.

LLM limitations

Because responses are generated by an LLM, MyPaddi can sometimes misunderstand a question, produce an unexpected response, or fail to follow an instruction perfectly.

The system prompt can guide the model's behavior, but it does not guarantee perfect behavior.

No permanent user profiles

MyPaddi can use information provided earlier in the current conversation, such as a user's name, but it does not currently maintain a permanent profile for returning users.

---

PROJECT DIRECTION

MyPaddi is evolving from a small rule-based Python exercise into a practical conversational application.

The project is being developed incrementally so that each new feature builds on concepts I understand rather than hiding the complexity behind a framework.

The development path so far has been:

```text
Python fundamentals
        ↓
Rule-based chatbot
        ↓
Input processing and intent matching
        ↓
APIs and environment variables
        ↓
LLM integration
        ↓
Conversation history
        ↓
Streamlit interface
```

The next stages will focus on improving reliability, safety, user experience, and eventually deploying MyPaddi so it can be accessed through a public URL.

The long-term goal is not to recreate ChatGPT. Instead, MyPaddi is a project for learning how real conversational applications are designed, connected to APIs, given memory, presented through an interface, and gradually improved through testing.

---

WHAT I AM LEARNING THROUGH THIS PROJECT

MyPaddi is helping me move from writing isolated Python exercises to thinking about how different parts of a real application work together.

Through the project I am learning about:

* Python application structure
* State and data flow
* APIs
* HTTP and request/response concepts
* Authentication and API keys
* Environment variables
* JSON and structured data
* LLMs and prompts
* Conversation history
* Web application interfaces
* Streamlit session state
* Debugging
* Git and GitHub
* Building software incrementally

MyPaddi is still a work in progress, and the project will continue evolving as my programming skills improve.
