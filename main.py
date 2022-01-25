try:
    import pandas as pd
    from sklearn.tree import DecisionTreeClassifier
except ImportError:
    print("One or more requirements missing!")

    import os
    os.system("pip install -r requirements.txt")

try:
    music_data = pd.read_csv("music.csv")
except FileNotFoundError:
    print("File Not Found!")

    import sys
    sys.exit()

age_and_gender = music_data.drop(columns=["genre"])
genre = music_data.drop(columns=["age", "gender"])

model = DecisionTreeClassifier()
model.fit(age_and_gender.values, genre.values)

age = None
gender = None

try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Invalid age specified! Please only enter numbers!")
    
    import sys
    sys.exit()

gender = (input("Enter your sex (male (m) / female (f)): ")).lower()

if gender == "male" or gender == "m":
    gender = 1
elif gender == "female" or gender == "f":
    gender = 0
else:
    print("Invalid sex specified! Please only enter male or female.")

    import sys
    sys.exit()

predictions = model.predict([ [age, gender] ])
print(f"\n\nYou are likely to be interested in: {predictions[0]}")