from flask import Flask, render_template
app = Flask(__name__)
import spacy
from spacytextblob.spacytextblob import SpacyTextBlob

# @app.route('/nlp')
def spacyFunctions():
    nlp = spacy.load('en_core_web_sm')
    spacy_text_blob = SpacyTextBlob()
    nlp.add_pipe(spacy_text_blob)
    text = "I had a really horrible day. It was the worst day ever! But every now and then I have a really good day that makes me happy."
    doc = nlp(text)
    print('Polarity:', doc._.sentiment.polarity) #how positive or negative the words are
    print('Subjectivity:', doc._.sentiment.subjectivity) #how positive or negative the words are
    print('Assessments:', doc._.sentiment.assessments) #assessments groups todether the good/bad phrases

@app.route('/')
def home():
   return render_template('index.html')

if __name__ == '__main__':
   #app.run()
   spacyFunctions()