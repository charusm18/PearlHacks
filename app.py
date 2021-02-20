from flask import Flask, render_template, request, redirect
app = Flask(__name__)
from perspective import perspectiveAPI, spacyFunctions, emotions

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/nlp', methods = ['POST'])
def nlp():
    text = request.form['text']
    print(spacyFunctions(text))
    print(emotions(text))
    print(perspectiveAPI(text))
    # hateSonar(text)
    return redirect('/')

if __name__ == '__main__':
   app.run()
   
