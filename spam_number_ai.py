import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score
import pickle
from utils import enhanced_features


def predict_with_check(number, model, vectorizer, le, df):
    """
    This function checks if the number is registered in the dataset,
    and asks the user to label it if it is not registered.
    """
    # Check if the number exists in the training data
    if number not in df['number'].values:
        print(f"The number '{number}' is not registered.")
        
        # Ask the user to classify the number as spam or not spam
        label = input("Is this number spam or not spam? (Enter 'spam' or 'not spam'): ").strip().lower()
        while label not in ['spam', 'not spam']:
            print("Invalid input. Please enter 'spam' or 'not spam'.")
            label = input("Is this number spam or not spam? (Enter 'spam' or 'not spam'): ").strip().lower()
        
        # Encode the label using the label encoder
        label_encoded = le.transform([label])[0]
        
        # Optionally, you can add the new number to the dataset and retrain the model
        new_row = {
            'number': number,
            'prefix': number[1:4],
            'length': len(number),
            'contains_999': '999' in number,
            'label': label_encoded,
            'features': enhanced_features(number)
        }
        
        # Add the new row to the dataframe (this can be saved later if needed)
        df = df.append(new_row, ignore_index=True)
        
        # Re-encode features and labels
        X = vectorizer.transform(df['features'])
        y = df['label']
        
        # Retrain the model with the updated data (optional step)
        model.fit(X, y)
        
        print(f"Model updated with the new number: {number}.")
        
        # Return the classification of the new number
        features = vectorizer.transform([enhanced_features(number)])
        prediction = model.predict(features)[0]
        return le.inverse_transform([prediction])[0]
    
    else:
        # If the number is registered, predict using the model
        features = vectorizer.transform([enhanced_features(number)])
        prediction = model.predict(features)[0]
        return le.inverse_transform([prediction])[0]


# Loading the dataset
df = pd.read_csv('synthetic_number_data.csv')

df['number'] = df['number'].astype(str)
df['prefix'] = df['number'].str[1:4]
df['length'] = df['number'].str.len()
df['contains_999'] = df['number'].apply(lambda x: '999' in x)

le = LabelEncoder()
df['label'] = le.fit_transform(df['label'])

df['features'] = df['number'].apply(enhanced_features)

# Vectorizer and model training
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['features'])
y = df['label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

# Save the model and vectorizer
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

# Example usage
new_number = input("Enter a number for classification: ").strip()
prediction = predict_with_check(new_number, model, vectorizer, le, df)
print(f"The number '{new_number}' is classified as: {prediction}")

