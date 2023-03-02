import openai
import streamlit as st

openai.api_key = st.secrets["KEY"]
import streamlit as st

st.set_page_config(
    page_title="Chat",
    page_icon="🧊",
    layout="wide",)
if 'messages' not in st.session_state:
    st.session_state['messages'] = [{"role": "system", "content": "You are a kind helpful assistant."}, ]

#b st.write(st.session_state['messages'])
for index, key in enumerate(st.session_state['messages']):
    col1, col2 = st.columns([3, 1])
    if index % 2 == 0:
        with col1:
            st.success(key["content"])
    else:
        with col2:
            st.info(key["content"])

form = st.form(key='my_form')
search = form.text_input(label='User : ')
submit_button = form.form_submit_button(label='Enter')
if submit_button:
    st.session_state['messages'].append(
        {"role": "user", "content": search},
    )
    chat = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=st.session_state['messages']
    )

    reply = chat.choices[0].message.content
    st.info(f"ChatGPT: {reply}")
    st.session_state['messages'].append({"role": "assistant", "content": reply})
