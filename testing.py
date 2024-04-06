import requests

# Define the API endpoint URL
api_url = "http://localhost:8000/predict_mbti/"

# Define the hobby input
hobby_input = {"hobby": "Reading"}

# Make a POST request to the API endpoint
response = requests.post(api_url, json=hobby_input)

# Check the response status code
if response.status_code == 200:
    # Print the predicted MBTI type
    print("Predicted MBTI type:", response.json()["predicted_mbti"])
else:
    print("Failed to get a response from the API")
