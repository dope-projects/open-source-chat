import streamlit as st
from public import tpl_bot, tpl_user

from .audio import handle_text_2_speech


def handle_userinput(user_question):
    response = st.session_state.conversation({'question': user_question})
    st.session_state.chat_history = response['chat_history']

    chat_history = st.session_state.chat_history

    for i, message in enumerate(chat_history):
        if i % 2 == 0:  # User's message #FIXME
            st.write(
                tpl_user.replace(
                    '{{MSG}}', message.content,
                ), unsafe_allow_html=True,
            )
        else:  # AI message
            st.write(
                tpl_bot.replace(
                    '{{MSG}}', message.content,
                ), unsafe_allow_html=True,
            )

    if len(chat_history) > 0:
        handle_text_2_speech(chat_history[-1].content)
