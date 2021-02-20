from flask import Flask, render_template, request, redirect, jsonify
app = Flask(__name__)
from perspective import perspectiveAPI, spacyFunctions, emotions # our nlp analyses

"""
purpose: Render our website pages.
"""
@app.route('/')
def home():
   return render_template('index.html')

@app.route('/test')
def test():
   return render_template('test.html')

"""
purpose: Take input from the JavaScript form.
"""
@app.route('/nlp', methods = ['POST'])
def nlp():
    text = request.form['text']
    print("text:", request.form['text']) # debug: check our form input was received correctly
    print(spacyFunctions(text))
    print(emotions(text))
    print(perspectiveAPI(text))
    # hateSonar(text)
    # return redirect('/')
    return jsonify(perspectiveAPI(text))

"""
purpose: Run server.
"""
if __name__ == '__main__':
   app.run()
   
