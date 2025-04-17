import pickle
from utils import enhanced_features
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load the model and vectorizer
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

# Load the existing dataset to check if the number is registered
df = pd.read_csv('synthetic_number_data.csv')

# LabelEncoder for converting 'spam' and 'not spam' labels
le = LabelEncoder()
le.fit(df['label'].unique())  # Fit the label encoder with the existing labels

def predict_with_check(number):
    """
    This function checks if the number is registered in the dataset,
    and initially classifies unregistered numbers as 'not spam'. It then asks the user
    if they think the number is spam and records their feedback.
    """
    # Check if the number exists in the training data
    if number not in df['number'].values:
        print(f"The number '{number}' is not registered.")
        
        # Initially mark it as 'not spam'
        print("Classifying this number as NOT SPAM by default.")
        
        # Ask the user if they think the number is spam and acknowledge feedback
        user_input = input("Do you think this number is spam? (Yes/No): ").strip().lower()
        
        while user_input not in ['yes', 'no']:
            print("Invalid input. Please enter 'Yes' or 'No'.")
            user_input = input("Do you think this number is spam? (Yes/No): ").strip().lower()
        
        if user_input == 'yes':
            print("Feedback taken.")
            label_encoded = le.transform(['spam'])[0]
        else:
            label_encoded = le.transform(['not spam'])[0]
        
        # Add the new number to the dataframe with the reported label
        new_row = {
            'number': number,
            'prefix': number[1:4],
            'length': len(number),
            'contains_999': '999' in number,
            'label': label_encoded,
            'features': enhanced_features(number)
        }
        
        df.loc[len(df)] = new_row  # Append new row to dataframe
        print(f"Model updated with the new number: {number}.")
        
        # Predict for the new number
        features = enhanced_features(number)
        X_new = vectorizer.transform([features])
        prediction = model.predict(X_new)
        
        return "SPAM" if prediction[0] == 1 else "NOT SPAM"
    else:
        # If the number is registered, predict using the model
        features = enhanced_features(number)
        X_new = vectorizer.transform([features])
        prediction = model.predict(X_new)
        return "SPAM" if prediction[0] == 1 else "NOT SPAM"


# Example usage
new_number = input("Enter phone number to check: ").strip()
prediction = predict_with_check(new_number)
print(f"The number '{new_number}' is classified as: {prediction}")


