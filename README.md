# Resume Reader App

## Introduction

This project leverages the newly launched LlamaExtract Beta API to extract structured data from unstructured PDF CVs/resumes using Streamlit. The LlamaExtract API provides a powerful solution for extracting structured information from various documents with high accuracy and efficiency.

## About LlamaExtract

**Introducing LlamaExtract Beta: Structured Data Extraction in Just a Few Clicks**

LlamaExtract is a managed service by LlamaCloud that allows you to perform structured extraction from unstructured documents. Structured extraction from unstructured data is not only a core use case for large language models (LLMs) but also a crucial component in data processing for retrieval and RAG (Retrieval-Augmented Generation) use cases.
More info on this blog: [LlamaIndex](https://www.llamaindex.ai/blog/introducing-llamaextract-beta-structured-data-extraction-in-just-a-few-clicks)

### Key Features:
- **Schema Inference:** LlamaExtract can infer a schema from an existing candidate set of documents. Users have the option to edit this schema later.
- **Value Extraction:** Extracts values from documents according to a specified schema, whether inferred, specified by a human, or both.

LlamaExtract is available to LlamaCloud users through both a UI and API. Schema inference is currently limited to 5 files with a maximum of 10 pages per file. Schema extraction operates on a per-document level given an existing schema.

### Metadata Extraction in the LLM ETL Stack:
A new data ETL stack is needed for LLM applications. The data loading, transformation, and indexing layer is crucial for downstream RAG and agent use cases over unstructured data. We built LlamaParse and LlamaCloud to serve these ETL needs and power thousands of production pipelines over complex documents. Besides chunk-level embeddings, automated metadata extraction is vital for increasing transparency and control over unstructured data.

## Getting Started

### Prerequisites
- Python 3.x
- Streamlit
- LlamaCloud API Key

### Installation

1. **Create a Virtual Environment:**
    ```
    python -m venv venv
    ```
    Activate the Virtual Environment:

    On Windows:
    ```
    venv\Scripts\activate
    ```
    On macOS/Linux:
    ```
    source venv/bin/activate
    ```

2. **Install Required Packages:**
    ```
    pip install -r requirements.txt
    ```

3. **Set Up API Key:**

    Add your LLAMA_CLOUD_API_KEY in the resume_reader_app.py file.

4. **Run the Streamlit App:**
    ```
    streamlit run resume_reader_app.py
    ```

5. **Usage**

    Once the Streamlit server is running, you can upload PDF CVs/resumes through the app's interface. The app will use the LlamaExtract API to process the documents and display the extracted structured data.