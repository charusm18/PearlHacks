# PearlHacks  
Installation Guide:  
## **Flask Installation:**  
##### 1. Start Virtual Environment:  
- For Mac:   
  - $ python3 -m venv venv  
  - $ . venv/bin/activate  
- For Windows: 
  - use cmd terminal
  - $ py -3 -m venv venv
  - $ venv\Scripts\activate.bat
##### 2. Install Flask (should be in venv)  
- $ pip install Flask
- $ pip install -e .
- For Mac:
  - $ export FLASK_APP=flaskr  
  - $ export FLASK_ENV=development
- For Windows:  
  - $ set FLASK_APP=flaskr  
  - $ set FLASK_ENV=development  
##### 3. To Run:  
- $ py app.py
- open up http://127.0.0.1:5000

## **NLP package Installation: (should all be in venv)**    

##### SPACY textblob Installation **should all be inthe virtual environment**
- $ pip install spacytextblob 
- $ python -m textblob.download_corpora
- $ python -m spacy download en_core_web_sm

##### Text to Emotion Installation **should all be inthe virtual environment**
- $ pip install text2emotion

##### Hate Sonar Intallation
- $ pip install hatesonar

##### Perspective:
- Change the client key
- For Mac:
  - $ venv/bin/pip install google-api-python-client 
- For Windows:
  - $venv\Scripts\pip.exe install google-api-python-client

## **.env file Installation: (should be in venv)**
- $ pip install -U python-dotenv
