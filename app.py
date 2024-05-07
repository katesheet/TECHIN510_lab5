import os

import google.generativeai as genai
from dotenv import load_dotenv
import streamlit as st
import time 

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-pro')

prompt_template = """
You are an expert at filling up job application answering job application questions.

Please use the information mentioned in resume and job description to answer a job application question.

Please include the following details:
- Bullet points
- put a key word for each point on the beginning
- Make the wording professional and passionate

my resume is: {resume}
the job description: {jd}
the question: {question}
"""

def generate_content(resume, jd, question):
    prompt = prompt_template.format(resume = resume, jd = jd, question = question)
    response = model.generate_content(prompt)
    return response.text

def stream_output():
    for word in reply.split(" "):
        yield word + " "
        time.sleep(0.02)

st.title("AI Job Application Questions Bot")

c1, c2 = st.columns(2)

with c1:
    resume = st.text_area("Enter your CV:", height = 300)
with c2:
    jd = st.text_area("Enter the job description:", height = 300)

question = st.text_input("Enter the application question: ")
reply = None
if st.button("Give me an answer!", use_container_width=True):
    reply = generate_content(resume, jd, question)
    st.write_stream(stream_output)