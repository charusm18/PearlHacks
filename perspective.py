from googleapiclient import discovery
import json
import spacy
from spacytextblob.spacytextblob import SpacyTextBlob
import text2emotion as te
from hatesonar import Sonar
import sklearn.linear_model._logistic

# for environmental variable
from dotenv import load_dotenv
load_dotenv()
import os
token = os.environ.get("api_key")

def perspectiveAPI(text):
    API_KEY = token
    service = discovery.build('commentanalyzer', 'v1alpha1', developerKey=API_KEY)
    analyze_request = {
    'comment': { 'text': text },
    'requestedAttributes': {'TOXICITY': {}, 'INSULT': {}, 'PROFANITY': {},'THREAT': {},'IDENTITY_ATTACK': {}}
    }

    response = service.comments().analyze(body=analyze_request).execute()
    return {
          "toxicity": response['attributeScores']['TOXICITY']['summaryScore']['value'],
          "insult": response['attributeScores']['INSULT']['summaryScore']['value'],
          "profanity": response['attributeScores']['PROFANITY']['summaryScore']['value'],
          "threat": response['attributeScores']['THREAT']['summaryScore']['value'],
          "identity_attack": response['attributeScores']['IDENTITY_ATTACK']['summaryScore']['value']
    }
  

def spacyFunctions(text):
    nlp = spacy.load('en_core_web_sm')
    spacy_text_blob = SpacyTextBlob()
    nlp.add_pipe(spacy_text_blob)
    doc = nlp(text)

    return { 
        'polarity': doc._.sentiment.polarity, 
        'subjectivity': doc._.sentiment.subjectivity,
        'assessments': doc._.sentiment.assessments
    }
 
def emotions(text):
    return te.get_emotion(text)

def hateSonar(text):
    sonar = Sonar()
    print(sonar.ping(text))