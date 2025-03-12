# CV Analyzer Application

This is an app to analyze cv with rag.

## Summary of the Application:
This application will enable you to upload a CV and APP will extract the following information:
- Personal Information
- Education History
- Work Experience
- Skills
- Projects
- Certifications

After extracting the information, the application will store retrieve clips of the dataset and will save in Vector database.
Also this will enable the User to interact to the extracted information via a chat interface.

## Technologies Used:
- Python [Version: 3.10.x]
- Django [Version: 4.x.x]
- S3 Storage (AWS/Minio/Digital Ocean)
- Django Rest Framework
- NEXT.js ( Chat UI ) Based on the SSR (Server Side Rendering) with React
- Tailwind CSS (For Styling)
- POSTGRESQL (Database)
- Celery
- Redis
- OCR (Tesseract)
- LLM API (Language Model API for NLP)
  - OpenAI GPT
- Pytest

### Key Technologies:
  - REST API (Django Rest Framework)
  - OCR (Tesseract)
  - NLP (OpenAI GPT for embeddings)
  - Microservices ( Django[Umbrella/Hexagonal Project] + Frontend)
  - RAG (Retrieval Augmented Generation)
  - Chroma DB (SQLite) as a Vector Database Referece: https://www.trychroma.com/
  - Token Based RATE LIMITING for the Chat API WIKI: https://en.wikipedia.org/wiki/Token_bucket



## How to run the application:
1. Clone the repository
2. Go to the root directory of the project
3. Run the following command to start the backend server:
```
  # Create a virtual environment and activate it
  # python3 -m venv .venv
  # source .venv/bin/activate

  pip install -r requirements.txt
  python manage.py migrate
  python manage.py runserver

  # To run the celery worker
  celery -A cv_analysis worker --loglevel=info
  # to monitor the tasks
  celery -A cv_analysis flower

  # Important: we are using the pdf2image library to convert the pdf to images
  # so we need to install the poppler-utils
  # Linux: sudo apt-get install poppler-utils
  # Mac: brew install poppler

  # to run the frontend server for chat window
  cd frontend && npm install && npm run dev
```

### More:

1. User can upload the CV in the frontend
2. The CV will be sent to the backend and the OCR will extract the text from the CV
3. The extracted text will be sent to the NLP model to vector database to save embeddings
4. User can later interact with the extracted information via the chat interface


## Hints for error on system:
1. Needs SQLite Version 3.35.0 or higher for chroma db to work
2. Needs to install poppler-utils for pdf2image to work


### OpenAI API KEY:
- Added the testable OpenAi API Key in the `.env.example` file


