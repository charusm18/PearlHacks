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
  - $ flask init-db    
- For Windows:  
  - $ set FLASK_APP=flaskr  
  - $ set FLASK_ENV=development  
  - $ flask init-db  
##### 3. To Run:  
- $ py app.py
- open up http://127.0.0.1:5000

## **spaCy textblob Installation: (should all be in venv)**    

SPACY textblob Installation **should all be inthe virtual environment**
    $ pip install spacytextblob 
    $ python -m textblob.download_corpora
    $ python -m spacy download en_core_web_sm

Text to Emotion Installation **should all be inthe virtual environment**
    $ pip install text2emotion

Hate Sonar Intallation
    $ pip install hatesonar
