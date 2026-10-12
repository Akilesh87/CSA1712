from sklearn.tree import DecisionTreeClassifier

# Study hours and attendance
X = [
    [1, 40],
    [2, 50],
    [3, 60],
    [4, 70],
    [5, 80],
    [6, 90]
]

# 0 = Fail, 1 = Pass
y = [0, 0, 0, 1, 1, 1]

model = DecisionTreeClassifier(random_state=0)
model.fit(X, y)

hours = 5
attendance = 80

prediction = model.predict([[hours, attendance]])

if prediction[0] == 1:
    print("Student will Pass")
else:
    print("Student will Fail")