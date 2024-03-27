import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()

BACKEND_URL = os.getenv("fastapiurl")

def get_message():
   response = requests.get(f"{BACKEND_URL}/")
   return response.json()

if st.button("Click here"):
   st.write(get_message())
