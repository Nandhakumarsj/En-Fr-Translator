"""Flask Server"""
from flask import Flask, render_template, request, url_for, redirect
from machinetranslation import translator

# App Name
app = Flask("Translator")

# Routes
@app.route('/', methods=['POST', 'GET'])
def index()->str:
    """renders index page
    """
    if request.method == "POST":
        input_text = request.form.get('text_input')
        print('Text is ',input_text)
        if request.form.get('en_fr') == 'true':
            # return english_french(input_text) --> same endpoint
            return redirect(url_for('english_french', _name = input_text))
        if request.form.get('fr_en') == 'true':
            # return french_english(input_text) --> same endpoint
            return redirect(url_for('french_english', _name = input_text))
        
    return render_template('index.html')

@app.route('/englishToFrench')
def english_french():
    "returns translation for english to french"
    _name = request.args.get('_name')
    _result = translator.english_to_french(_name)
    return render_template('translate.html', original_text = _name, translated_text = _result)

@app.route('/frenchToEnglish')
def french_english():
    "returns translation for french to english"
    _name = request.args.get('_name')
    _result = translator.french_to_english(_name)
    return render_template('translate.html', original_text = _name, translated_text = _result)

if __name__ == '__main__':
    app.run(debug=True)
    