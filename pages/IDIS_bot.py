import streamlit as st
import yfinance as yf
import pandas as pd
import datetime as dt
import plotly.graph_objects as go
import openai
from openai import OpenAI

if "isverif" not in st.session_state or st.session_state.isverif == False:
    st.header("ANDA TIDAK MEMPUNYAI AKSES")
    st.subheader("Harap buat akun terlebih dahulu 😊")
else:

    st.title("IDIS BOT")

    def chat_with_ai():
            st.header("IDIS BOT!")
            st.markdown("Here to answer your Invesment Problem !")

            client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

            if "openai_model" not in st.session_state:
                st.session_state["openai_model"] = "gpt-3.5-turbo"

            if "messages" not in st.session_state:
                st.session_state.messages = []

            with st.chat_message("assistant"):
                st.markdown("Halo nama saya IDIS bot, Asisten Investsai kamu Kamu, Tolong Tanyakan apapun tetang investasi kepada saya!🤑")

            for message in st.session_state.messages:
                with st.chat_message(message["role"]):
                    st.markdown(message["content"])

            if prompt := st.chat_input("Apa pertanyaan kamu hari ini?"):
                # Ensure the user input is focused on emotions and mental well-being
                st.session_state.messages.append({"role": "user", "content": prompt})
                with st.chat_message("user"):
                    st.markdown(prompt)

                with st.chat_message("assistant"):
                    message_placeholder = st.empty()
                    full_response = ""
                    for response in client.chat.completions.create(
                        model=st.session_state["openai_model"],
                        messages=[
                            {"role": m["role"], "content": m["content"]}
                            for m in st.session_state.messages
                        ],
                        stream=True,
                    ):
                        full_response += (response.choices[0].delta.content or "")
                        message_placeholder.markdown(full_response + "▌")
                    message_placeholder.markdown(full_response)

                st.session_state.messages.append({"role": "assistant", "content": full_response})

    chat_with_ai()
