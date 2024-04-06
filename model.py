import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
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

# Check if the data contains all categories for MBTI Type and Hobby
missing_hobbies = set(hobby_categories) - set(data['Hobby'].unique())
if missing_hobbies:
    print("Warning: Missing hobby categories in the dataset:", missing_hobbies)

# Split the data into input features (X) and target labels (y)
X = data['Hobby']
y = data['MBTI Type']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Reshape the input features for Logistic Regression
X_train = X_train.values.reshape(-1, 1)
X_test = X_test.values.reshape(-1, 1)

# Train the Logistic Regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Evaluate the model on the testing set
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")

# Since there are only two classes, we don't need to specify target_names in classification_report
print(classification_report(y_test, y_pred))

# Function to predict MBTI type for a given hobby
# Function to predict MBTI type for a given hobby
def predict_mbti(hobby):
    if hobby not in hobby_categories:
        print(f"Warning: Hobby '{hobby}' is not present in the dataset.")
        return "ENFP"  # Return "ENFP" when hobby is not present
    hobby_encoded = le_hobby.transform([hobby])
    mbti_predicted = model.predict([hobby_encoded])[0]
    return le_mbti.inverse_transform([mbti_predicted])[0]

# Example usage
hobby = "Reading"  # Ensure the case matches the categories in the dataset
predicted_mbti = predict_mbti(hobby)
print(f"The most suitable MBTI type for hobby '{hobby}' is: {predicted_mbti}")
