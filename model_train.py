# Random Forest Classifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd 
import pickle

# Loading the data
df = load_iris()
X = df.data
y = df.target

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 87, test_size = 0.5)

# Build the model
rfc = RandomForestClassifier(n_estimators = 10)

# Train moddel
rfc.fit(X_train, y_train)

# Predict
pred = rfc.predict(X_test)

# Eval 
print(accuracy_score(pred, y_test))

# Export model
with open("./api/main/data/rcf_model.pkl", "wb") as f:
    pickle.dump(rfc, f)