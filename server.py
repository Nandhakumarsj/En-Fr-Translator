"""Flask Server"""
from flask import Flask, render_template, request
from machinetranslation import translator

# App Name
app = Flask("Translator")

# Routes
@app.route('/')
def index()->str:
    """renders index page
    """
    return render_template('index.html')

@app.route('/englishToFrench')
def english_french():
    "returns translation for english to french"
    _input = request.args['text']
    print(_input)
    _name = "Hello"
    _result = translator.english_to_french(_name)
    return render_template('index.html', original_text = _name, translated_text = _result)

@app.route('/frenchToEnglish')
def french_english():
    "returns translation for french to english"
    _name = "Bonjour"
    _result = translator.french_to_english(_name)
    return render_template('index.html', original_text = _name, translated_text = _result)

if __name__ == '__main__':
    app.run(debug=True)
    