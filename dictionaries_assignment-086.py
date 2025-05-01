

# Creating a dictionary with 10 students and their scores
student_scores = {
    "Ali": 85,
    "Zainab": 78,
    "Hamza": 92,
    "Ayesha": 88,
    "Usman": 76,
    "Fatima": 90,
    "Bilal": 95,
    "Sana": 80,
    "Tahir": 87,
    "Nida": 82
}

# 1. get()  Retrieve the score of a specific student
print("1. Zainab's score is:", student_scores.get("Zainab"))

# 2. keys()  List all student names
print("2. List of students:", list(student_scores.keys()))

# 3. values()  List all scores
print("3. Their scores:", list(student_scores.values()))

# 4. items()  Display all key-value pairs
print("4. Student and score pairs:")
for name, score in student_scores.items():
    print(f"   {name}: {score}")

# 5. update() Update a student's score
student_scores.update({"Ali": 89})
print("5. Ali's updated score:", student_scores["Ali"])

# 6. pop() Remove a student and return their score
removed_score = student_scores.pop("Usman")
print("6. Usman was removed. His score was:", removed_score)

# 7. popitem() Remove the last inserted item
last_entry = student_scores.popitem()
print("7. Last entry removed (likely Nida):", last_entry)

# 8. copy() Create a backup copy of the dictionary
scores_backup = student_scores.copy()
print("8. Backup of current student scores:", scores_backup)

# 9. setdefault() Add a new student only if they don't exist
student_scores.setdefault("Hira", 81)
print("9. Hira was added with default score. Current list:")
print(student_scores)

# 10. fromkeys() Create a new dictionary with default scores
new_students = ["Jawad", "Mina", "Qasim"]
default_scores = dict.fromkeys(new_students, 70)
print("10. New students with default scores:", default_scores)


# clear() Would remove all items from the dictionary
student_scores.clear()
print("All student data cleared:", student_scores)


#mehtab_haider-086
#Dictionaries assignment-01