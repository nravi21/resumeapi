
from flask import Flask, request, jsonify
import spacy
from spacy.tokens import Doc
from spacy.training.example import Example

# Load the fine-tuned spaCy model
nlp = spacy.load('fine_tuned_nlp_model')

app = Flask(__name__)

@app.route('/parse_resume', methods=['POST'])
def parse_resume():
    text = request.json['text']
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return jsonify(entities)

if __name__ == '__main__':
    app.run()
