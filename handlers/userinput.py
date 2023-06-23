import streamlit as st

from .audio import handle_text_2_speech
from public import tpl_user, tpl_bot


def handle_userinput(user_question):
    response = st.session_state.conversation({'question': user_question})
    st.session_state.chat_history = response['chat_history']

    chat_history = st.session_state.chat_history

    for i, message in enumerate(chat_history):
        if i % 2 == 0:
            st.write(tpl_user.replace("{{MSG}}", message.content), unsafe_allow_html=True)
        else:
            st.write(tpl_bot.replace("{{MSG}}", message.content), unsafe_allow_html=True)

    if len(chat_history) > 0:
        handle_text_2_speech(chat_history[-1].content)
