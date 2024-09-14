# QnA Bot for website offering tech-courses

This project provides a Question-and-Answer (QnA) bot designed to assist prospective students with queries related to the courses or content offered on tech courses website. The bot utilizes a FAQs document containing frequently asked questions (FAQs) and their answers. It finds the most relevant QnA pairs from the document and passes them to a large language model (LLM) for answer generation. If no similar question-answer pair is found, the bot replies with "I don't know."

## Features
- Retrieves relevant question-answer pairs from a provided FAQs document using similarity scoring.
- Uses Google Gemini 1.5 Pro LLM to generate answers based on the context of the retrieved FAQs.
- Provides concise, context-based answers.
- Handles cases where there is no relevant context by responding with "I don't know."

## Screenshot
![Demo Screenshot](https://drive.google.com/uc?export=view&id=1E97WmDR6nAFYgpf3AkrhzX_1_686-LTS)

## Architecture
1. **Frontend:** Built using Streamlit for an interactive user interface where users can input questions.
    - Main.py: Displays the interface with options to create a knowledge base from the FAQs and input questions.

2. **Backend:**

    - Langchain Helper (langchain_helper.py):
        - FAQ Retrieval: Uses HuggingFace embeddings to convert FAQs into vector embeddings and stores them in a FAISS vector database.
        - Question Answering Chain: Retrieves similar FAQs from the vector database and feeds them to the LLM.
        - LLM Integration: Integrates with Google Gemini 1.5 Pro to generate responses based on the context provided by the retrieved FAQs.
3. **Data Handling:**
    - CSV FAQ Loader: Loads a CSV file (faqs.csv) containing FAQs and stores the vector representations in FAISS.

## Installation

### Prerequisites
- Python 3.8+
- Google Cloud account and access to the Google Generative AI (Gemini 1.5 Pro) API.
- A valid GOOGLE_API_KEY for the Google Gemini 1.5 Pro model.

### Setup
1. Clone the repository
2. Install dependencies: Ensure you have pip installed, then run:
```
pip install -r requirements.txt
```
3. Set up environment variables: Create a .env file in the root directory and add your Google API key:
```
GOOGLE_API_KEY=your_google_api_key_here
```
4. Prepare the FAQs:

- Ensure you have a CSV file named faqs.csv in the root directory, containing frequently asked questions and their answers.
- The CSV should have at least a prompt column that stores the questions.


## Running the Application

1. Start the Streamlit app:
```
streamlit run main.py
```
2. Create the Knowledge Base:

    - Click the "Create Knowledgebase" button on the app interface to load the FAQs and create the vector database.
    - After the knowledge base is created, you can input any question related to the demo courses, and the bot will respond based on the FAQs or by invoking the LLM.

## How it works

1. Input Question: Users ask a question using the provided input field.
2. Retrieve FAQs: The bot searches for similar QnA pairs from the FAQs based on vector similarity using FAISS.
3. Answer Generation: If a relevant QnA pair is found, it is passed along with the question to the Google Gemini LLM, which generates an answer based on the context.
4. Response: If no relevant FAQ is found, the LLM responds with "I don't know."

## Tech Stack
- Streamlit: For the user interface.
- Langchain: To handle question-answer retrieval and answer generation with LLMs.
- Google Gemini 1.5 Pro: For generating natural language responses.
- FAISS: For fast vector search and similarity matching.
- HuggingFace Embeddings: For converting FAQs into vector representations.
- CSVLoader: For loading FAQs from a CSV file.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

