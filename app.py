from flask import Flask, render_template, request, jsonify
from chat_bot2 import tree_to_code  # Import the tree_to_code function

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    symptom = request.form['msg']  # Get the symptom from the form
    response = tree_to_code(symptom)  # Call tree_to_code with the symptom
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
