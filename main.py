import csv
import random

# Dummy MBTI types
mbti_types = ['ISTJ', 'ISFJ', 'INFJ', 'INTJ', 'ISTP', 'ISFP', 'INFP', 'INTP',
              'ESTP', 'ESFP', 'ENFP', 'ENTP', 'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ']

# Dummy hobbies
hobbies = ['Reading', 'Cooking', 'Running', 'Painting', 'Gardening', 'Photography',
           'Singing', 'Dancing', 'Writing', 'Coding', 'Playing an Instrument',
           'Hiking', 'Swimming', 'Traveling', 'Watching Movies', 'Playing Video Games', 'Playing Audio Games', 'Pottery']

# Function to generate dummy data
def generate_dummy_data(num_rows):
    data = []
    for _ in range(num_rows):
        mbti = random.choice(mbti_types)
        hobby = random.choice(hobbies)
        data.append([mbti, hobby])
    return data

# Function to write data to CSV
def write_to_csv(filename, data):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['MBTI Type', 'Hobby'])
        writer.writerows(data)

# Generating 50 rows of dummy data
dummy_data = generate_dummy_data(250)

# Writing data to CSV file
write_to_csv('dummy_data.csv', dummy_data)
