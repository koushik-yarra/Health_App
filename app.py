from dotenv import load_dotenv # type: ignore
load_dotenv()

import streamlit as st # type: ignore
import os
from PyPDF2 import PdfReader # type: ignore
import google.generativeai as genai # type: ignore

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input):
    model = genai.GenerativeModel('gemini-2.0-flash')
    response = model.generate_content(input)
    return response.text

def input_pdf_text(uploaded_file):
    if uploaded_file is not None:
        pdf_reader = PdfReader(uploaded_file)
        text = ''
        for page in pdf_reader.pages:
            extracted_text = page.extract_text()
            if extracted_text:  # Check if text is extracted
                text += extracted_text + "\n"
        return text.strip()
    else:
        return None

# Streamlit app
st.set_page_config(page_title='ATS Tracker')
st.title("SIMPLE ATS TRACKER")
st.text("Improve Your Resume ATS")

jd = st.text_area("Paste the Job Description")
uploaded_file = st.file_uploader("Upload Your Resume", type="pdf", help="Please upload a PDF resume")

submit = st.button("Submit")

if submit:
    if uploaded_file is not None and jd.strip():
        resume_text = input_pdf_text(uploaded_file)

        if resume_text:
            # Format the prompt correctly
            formatted_prompt = f"""
            Hey, act like a skilled and highly experienced ATS (Application Tracking System) 
            with expertise in software engineering, data science, data analytics, and big data engineering. 
            Your task is to evaluate the resume based on the given job description. 
            The job market is highly competitive, so provide the best assistance to improve the resume. 
            
            Assign a percentage match based on the JD and highlight the missing keywords accurately.
            
            Resume: {resume_text}
            Job Description: {jd}

            Return the response as a single structured JSON string in the format:
            {{"JD Match": "%", "MissingKeywords": [], "Profile Summary": ""}}
            """

            # Get response
            response = get_gemini_response(formatted_prompt)
            st.subheader("ATS Analysis Result")
            st.text_area("Output", response, height=300)
        else:
            st.error("Failed to extract text from the uploaded PDF. Try another file.")
    else:
        st.error("Please upload a resume and provide a job description.")
