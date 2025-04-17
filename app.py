from flask import Flask, request, render_template, jsonify
import pickle
from utils import enhanced_features  # Make sure this function is defined and working

app = Flask(__name__)

# Load the model and vectorizer
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')  # Renders the form

@app.route('/predict', methods=['POST'])
def predict():
    phone_number = request.form['phone_number']
    
    # Extract features and make prediction
    features = enhanced_features(phone_number)
    X_new = vectorizer.transform([features])
    prediction = model.predict(X_new)

    result = "SPAM" if prediction[0] == 1 else "NOT SPAM"
    result_class = "spam" if prediction[0] == 1 else "not-spam"

    # Return the result to the HTML template
    return render_template('index.html', result=result, result_class=result_class)


if __name__ == '__main__':
    app.run(debug=True)


