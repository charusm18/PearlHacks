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

"""
Purpose: Utilize python NLP packages to analyze text.
"""
def perspectiveAPI(text):
    API_KEY = token
    service = discovery.build('commentanalyzer', 'v1alpha1', developerKey=API_KEY)
    analyze_request = {
    'comment': { 'text': text },
    'requestedAttributes': {'TOXICITY': {}, 'INSULT': {}, 'PROFANITY': {},'THREAT': {},'IDENTITY_ATTACK': {}}
    }

    response = service.comments().analyze(body=analyze_request).execute()
    print(round(response['attributeScores']['THREAT']['summaryScore']['value'],4))
    return {
          "toxicity": round(response['attributeScores']['TOXICITY']['summaryScore']['value'],4),
          "insult": round(response['attributeScores']['INSULT']['summaryScore']['value'],4),
          "profanity": round(response['attributeScores']['PROFANITY']['summaryScore']['value'],4),
          "threat": round(response['attributeScores']['THREAT']['summaryScore']['value'],4),
          "identity_attack": round(response['attributeScores']['IDENTITY_ATTACK']['summaryScore']['value'], 4)
    }
  
def spacyFunctions(text):
    nlp = spacy.load('en_core_web_sm')
    spacy_text_blob = SpacyTextBlob()
    nlp.add_pipe(spacy_text_blob)
    doc = nlp(text)

    

    return { 
        'polarity': round(doc._.sentiment.polarity, 4), 
        'subjectivity': round(doc._.sentiment.subjectivity,4),
        'assessments': doc._.sentiment.assessments
    }
 
def emotions(text):
    return te.get_emotion(text)

def hateSonar(text):
    sonar = Sonar()
    print(sonar.ping(text))