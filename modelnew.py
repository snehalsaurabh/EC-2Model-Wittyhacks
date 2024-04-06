import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder

# Load the dataset
data = pd.read_csv("dummy_data.csv")

# Define the categories for MBTI Type and Hobby
mbti_categories = ['ISTJ', 'ISFJ', 'INFJ', 'INTJ', 'ISTP', 'ISFP', 'INFP', 'INTP',
                  'ESTP', 'ESFP', 'ENFP', 'ENTP', 'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ']
hobby_categories = ['Reading', 'Cooking', 'Running', 'Painting', 'Gardening', 'Photography',
                    'Singing', 'Dancing', 'Writing', 'Coding', 'Playing an Instrument',
                    'Hiking', 'Swimming', 'Traveling', 'Watching Movies', 'Playing Video Games']

# Encode the input features and target labels
le_hobby = LabelEncoder()
le_mbti = LabelEncoder()

data['Hobby'] = le_hobby.fit_transform(data['Hobby'])
data['MBTI Type'] = le_mbti.fit_transform(data['MBTI Type'])

# Train the Logistic Regression model
X = data['Hobby'].values.reshape(-1, 1)
y = data['MBTI Type']
model = LogisticRegression()
model.fit(X, y)

# FastAPI app
app = FastAPI()

# Define request and response models
class HobbyInput(BaseModel):
    hobby: str

class MBTIOutput(BaseModel):
    predicted_mbti: str

# Route for predicting MBTI type for a given hobby
@app.post("/predict_mbti/")
def predict_mbti_for_hobby(hobby_input: HobbyInput):
    hobby = hobby_input.hobby
    if hobby not in hobby_categories:
        return {"predicted_mbti": "ENFP"}  # Return "ENFP" when hobby is not present
    hobby_encoded = le_hobby.transform([hobby])
    mbti_predicted = model.predict([hobby_encoded])[0]
    predicted_mbti = le_mbti.inverse_transform([mbti_predicted])[0]
    return {"predicted_mbti": predicted_mbti}
