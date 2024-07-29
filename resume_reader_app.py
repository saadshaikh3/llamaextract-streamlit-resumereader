import streamlit as st
import os
import asyncio
from pydantic import BaseModel, Field
from llama_extract import LlamaExtract
import tempfile

# Set your LlamaExtract API key
os.environ["LLAMA_CLOUD_API_KEY"] = "llx-..."

# Define the Pydantic models
class Education(BaseModel):
    institution: str
    degree: str

class Resume(BaseModel):
    name: str
    summary: str
    work_experience: str
    education: Education

# Streamlit app
st.title("CV/Resume Reader")

# File uploader
uploaded_files = st.file_uploader("Upload CV/Resume PDFs", accept_multiple_files=True, type="pdf")

if uploaded_files:
    # Create a temporary directory to store uploaded files
    with tempfile.TemporaryDirectory() as temp_dir:
        # Save uploaded files to the temporary directory
        fpaths = []
        for uploaded_file in uploaded_files:
            file_path = os.path.join(temp_dir, uploaded_file.name)
            with open(file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            fpaths.append(file_path)

        # Extract information from resumes
        @st.cache_data
        def extract_resume_info(file_paths):
            async def run_extraction():
                extractor = LlamaExtract(verbose=True)
                schema_response = await extractor.acreate_schema("Resume Schema", data_schema=Resume)
                responses, models = await extractor.aextract(schema_response.id, file_paths, response_model=Resume)
                return models

            return asyncio.run(run_extraction())

        with st.spinner("Extracting information from the resumes..."):
            extracted_models = extract_resume_info(fpaths)

        # Display extracted information in a table
        if extracted_models:
            st.subheader("Extracted Resume Information")
            
            # Prepare data for the table
            table_data = []
            for model in extracted_models:
                table_data.append({
                    "Candidate Name": model.name,
                    "Summary": model.summary,
                    "Work Experience": model.work_experience,
                    "Education": f"{model.education.degree} - {model.education.institution}"
                })

            # Display the table
            st.table(table_data)
        else:
            st.warning("No information could be extracted from the uploaded resumes.")

else:
    st.info("Please upload one or more resume PDFs to get started.")

# Add some styling
st.markdown("""
<style>
    .stTable {
        font-size: 14px;
    }
    .stTable thead th {
        background-color: #f0f2f6;
        font-weight: bold;
    }
    .stTable tbody tr:nth-of-type(even) {
        background-color: #f8f9fa;
    }
</style>
""", unsafe_allow_html=True)