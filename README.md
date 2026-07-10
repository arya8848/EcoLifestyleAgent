# 🌱 Eco Lifestyle Agent

An AI-powered Eco Lifestyle Assistant built using **IBM Granite**, **Retrieval-Augmented Generation (RAG)**, **FAISS**, and **Streamlit**.

This application helps users adopt sustainable living by answering questions related to recycling, waste management, energy conservation, water conservation, renewable energy, and eco-friendly practices using trusted environmental documents.

---

## 📌 Problem Statement

**Problem Statement No. 6 – Eco Lifestyle Agent**

Developed as part of the **Edunet Foundation Internship Program** using **IBM Cloud Lite** and **IBM Granite**.

The application provides personalized eco-friendly suggestions by retrieving relevant information from environmental PDF documents and generating natural language responses using IBM Granite.

---

## 🚀 Features

- 🌱 AI-powered Eco Lifestyle Assistant
- 📄 Retrieval-Augmented Generation (RAG)
- 🤖 IBM Granite Foundation Model
- 🔍 FAISS Vector Database for semantic search
- 📚 Answers based on environmental PDF documents
- 💬 Natural language question answering
- 🖥️ Interactive Streamlit web interface

---

## 🛠️ Technologies Used

- Python
- IBM Cloud Lite
- IBM watsonx.ai
- IBM Granite
- Streamlit
- LangChain
- FAISS
- Hugging Face Embeddings
- PyPDF
- python-dotenv

---

## 📂 Project Structure

```text
EcoLifestyleAgent/
│
├── app.py
├── granite.py
├── rag.py
├── build_vector_db.py
├── config.py
├── test_granite.py
├── test_rag.py
├── test_rag_granite.py
├── requirements.txt
├── README.md
├── .env
│
├── data/
│   ├── Environmental PDF Files
│
├── vector_db/
│   ├── index.faiss
│   └── index.pkl
│
└── assets/
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/EcoLifestyleAgent.git
cd EcoLifestyleAgent
```

---

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

Windows

```bash
.\venv\Scripts\Activate.ps1
```

Linux/Mac

```bash
source venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Configure Environment Variables

Create a `.env` file.

```text
IBM_API_KEY=your_api_key
IBM_PROJECT_ID=your_project_id
IBM_URL=https://us-south.ml.cloud.ibm.com
```

---

### 5. Build the Vector Database

```bash
python build_vector_db.py
```

---

### 6. Run the Application

```bash
python -m streamlit run app.py
```

The application will open in your browser.

---

## 💡 Example Questions

- How should plastic waste be managed?
- How can I save electricity at home?
- What are eco-friendly ways to conserve water?
- What are the benefits of renewable energy?
- How should recyclable plastic waste be disposed of?

---

## 🧠 How It Works

1. User enters a question.
2. FAISS searches the vector database.
3. Relevant document chunks are retrieved.
4. Retrieved context is sent to IBM Granite.
5. Granite generates an accurate response.
6. The answer is displayed in the Streamlit application.

---

## 📊 Architecture

```text
User
   │
   ▼
Streamlit Interface
   │
   ▼
FAISS Vector Database
   │
   ▼
Relevant PDF Context
   │
   ▼
IBM Granite
   │
   ▼
Generated Answer
```

---

## 📈 Future Enhancements

- Carbon Footprint Calculator
- Eco Score Prediction
- Recycling Center Locator
- Voice-based Assistant
- Multi-language Support
- Mobile Application

---

## 👨‍💻 Developed By

**Arya**

B.Tech Computer Science Engineering

Edunet Foundation Internship Project

---

## 📜 License

This project is developed for educational and internship purposes.