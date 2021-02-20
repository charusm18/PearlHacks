from flask import Flask, render_template
app = Flask(__name__)
import spacy
from spacytextblob.spacytextblob import SpacyTextBlob
import text2emotion as te
from hatesonar import Sonar
import sklearn.linear_model._logistic


# @app.route('/nlp')
def spacyFunctions(text):
    nlp = spacy.load('en_core_web_sm')
    spacy_text_blob = SpacyTextBlob()
    nlp.add_pipe(spacy_text_blob)
    doc = nlp(text)
    print('Polarity:', doc._.sentiment.polarity) #how positive or negative the words are
    print('Subjectivity:', doc._.sentiment.subjectivity) #how positive or negative the words are
    print('Assessments:', doc._.sentiment.assessments) #assessments groups todether the good/bad phrases

def emotions(text):
    print(te.get_emotion(text))

def hateSonar(text):
    sonar = Sonar()
    print(sonar.ping(text))
    

@app.route('/')
def home():
   return render_template('index.html')

if __name__ == '__main__':
   #app.run()
   text = "I am having a very very bad day that sucks. "
   spacyFunctions(text)
   emotions(text)
   hateSonar(text)