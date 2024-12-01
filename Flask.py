from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load the trained model
model = joblib.load(r'C:\Users\Kshitish Pandit\Desktop\Chess\Random_Forest.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json  # Expecting JSON data
    input_features = pd.DataFrame(data, index=[0])  # Convert to DataFrame
    prediction = model.predict(input_features)
    probability = model.predict_proba(input_features)  # Get probabilities
    return jsonify({
        'winner': prediction[0],
        'probability': {
            'white': probability[0][1],  # Assuming index 1 is for white winning
            'black': probability[0][0]    # Assuming index 0 is for black winning
        }
    })

if __name__ == '__main__':
    app.run(debug=True)