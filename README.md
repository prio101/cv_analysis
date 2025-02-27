# CV Analyzer Application

This is a task given by ASTUDIO.

## Summary of the Application:
This application will enable you to upload a CV and it will extract the following information:
- Personal Information
- Education History
- Work Experience
- Skills
- Projects
- Certifications

After extracting the information, the application will store and display the information in a structured format.
Also this will enable the User to interact to the extracted information via a chat interface.

## Technologies Used:
- Python
- Django
- S3 Storage (AWS/Minio/Digital Ocean)
- Django Rest Framework
- NEXT.js
- React.js
- Tailwind CSS
- POSTGRESQL
- Celery
- Redis
- OCR (Tesseract)
- LLM API (Language Model API for NLP)
  - OpenAI GPT-3
  - Ollama API ( Locally installed LLM )
- Pytest
- Docker (Optional)

### Key Technologies:
  - REST API
  - OCR
  - NLP
  - Microservices



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

```

### More:

1. User can upload the CV in the frontend
2. The CV will be sent to the backend and the OCR will extract the text from the CV
3. If the CV is not uploaded, the app will always process the sample CVs available in the local storage: `sample_cvs/`
4. The extracted text will be sent to the NLP model to extract the information
5. The extracted information will be stored in the database
