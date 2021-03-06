from flask import Flask, render_template, request, redirect, jsonify
app = Flask(__name__)
from perspective import perspectiveAPI, spacyFunctions, emotions # our nlp analyses

"""
purpose: Render our website pages.
"""
@app.route('/')
def home():
   return render_template('index.html', initScreen = True, sentimentValues={}, emotionsValues = {}, perspectiveValues={})

@app.route('/test')
def test():
   return render_template('test.html')

"""
purpose: Take input from the JavaScript form.
"""
@app.route('/analysis', methods = ['POST'])
def analysis():
    text = request.form['text']
    perspectiveValues = perspectiveAPI(text)
    emotionsValues = emotions(text)
    sentimentValues = spacyFunctions(text)

    # return redirect('/')
    return render_template('index.html', text = text,  
        initScreen = False, 
        sentimentValues = sentimentValues, 
        emotionsValues = emotionsValues, 
        perspectiveValues  = perspectiveValues
    )

"""
purpose: Run server.
"""
if __name__ == '__main__':
   app.run()
   
