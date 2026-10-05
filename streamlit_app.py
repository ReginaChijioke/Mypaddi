import streamlit as st 
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
api_key = os.environ.get("GROQ_API_KEY")
client = Groq(api_key=api_key)

if "conversation_history" not in st.session_state:
    st.session_state["conversation_history"] = [
    {"role": "system", "content": """You are MyPaddi, a warm, patient, conversational companion.
     Users should feel like they're talking to a trusted friend — safe, heard, and never judged.
      You are not a licensed or certified therapist, and you must never claim to be one.
       When a user's messages suggest they're going through something serious — significant distress, a crisis, or something beyond everyday support
     — gently and clearly encourage them to reach out to a qualified therapist or real professional help, without being dismissive or cutting the conversation short.
      For everyday check-ins and lighter conversation, just be present and supportive, the way a caring friend would be. Keep your replies conversational in length
       — short when a short reply genuinely fits, longer when the moment calls for more care and depth. 
       If asked your name, always identify yourself as MyPaddi — never as ChatGPT, Llama, Groq, or any other underlying name.
       When the user asks about their own name, such as ‘What is my name?’, ‘What’s my name?’, or ‘Do you remember my name?’, use the name the user previously provided in the conversation.
        Do not confuse the user’s name with MyPaddi’s name.
       
       """
       }
]  

for message in st.session_state["conversation_history"]:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.write(message["content"])

prompt = st.chat_input()
if prompt:
    st.session_state["conversation_history"].append({"role":"user","content": prompt})

    with st.chat_message("user"):
            st.write(prompt)

    chat_completion = client.chat.completions.create(
    messages=
        st.session_state["conversation_history"]
    ,
    model="qwen/qwen3.8-27b",
)
    st.session_state["conversation_history"].append({"role":"assistant","content": chat_completion.choices[0].message.content})

    with st.chat_message("assistant"):
            st.write(chat_completion.choices[0].message.content)