from flask import Flask, render_template
app = Flask(__name__)
import spacy
from textblob import TextBlob, Word, Blobber

# @app.route('/nlp')
def nlp():
    nlp = spacy.load('en_core_web_sm')
    spacy_text_blob = TextBlob()
    nlp.add_pipe(spacy_text_blob)
    text = "I had a really horrible day. It was the worst day ever!"
    doc = nlp(text) 
    print('Polarity:', doc._.sentiment.polarity) 
    print('Sujectivity:', doc._.sentiment.subjectivity)
    print('Assessments:', doc._.sentiment.assessments) 
    #return render_template('index.html')

@app.route('/')
def home():
   return render_template('index.html')

if __name__ == '__main__':
   app.run()
   #nlp()