from dotenv import load_dotenv
load_dotenv()
import os
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate


from langchain_google_genai import GoogleGenerativeAI


llm = GoogleGenerativeAI(model="gemini-1.5-pro", google_api_key=os.environ["GOOGLE_API_KEY"], temperature=0.5)


from langchain_community.document_loaders import CSVLoader


from langchain_community.embeddings import HuggingFaceInstructEmbeddings
from langchain_community.vectorstores import FAISS

instructor_embeddings = HuggingFaceInstructEmbeddings()
vector_db_path = "faiss_index"

def create_vectordb():
    loader = CSVLoader("faqs.csv", source_column="prompt", encoding="ISO-8859-1")
    data = loader.load()
    vectordb = FAISS.from_documents(data, instructor_embeddings)
    vectordb.save_local(vector_db_path)

def get_qa_chain():
    vector_db = FAISS.load_local(vector_db_path, instructor_embeddings, allow_dangerous_deserialization=True)
    retriever = vector_db.as_retriever(score_threshold=0.7)

    system_prompt = (
        "Use the given context only to answer the question."
        "If context does not help you answer it, please say 'I don't know'." 
        "Dont make up things on your own."
        "Use upto three sentence and keep the answer concise."
        "Do not give reasoning behind your answer."
        "Context: {context}"
    )

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            ("human", "{input}"),
        ]
    )
    qna_chain = create_stuff_documents_chain(llm, prompt)
    chain = create_retrieval_chain(retriever, qna_chain)
    return chain


if __name__ == "__main__":
    chain = get_qa_chain()
    print(chain.invoke({"input": "Do you offer internships?"}))