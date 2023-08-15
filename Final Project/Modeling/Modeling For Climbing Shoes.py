import pandas as pd
from sklearn.linear_model import RidgeClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


# Model A: Predicting Shoe Brand From Pricing and Color
# Load data
climbingshoes_df = pd.read_csv('BackcountryClimbing-Shoes.csv')

# Split data into features and target
X = climbingshoes_df[['Shoe_Color', 'Shoe_Price']]
y = climbingshoes_df['Shoe_Brand']

# Convert categorical color data into numerical data
X = pd.get_dummies(X, columns=['Shoe_Color'])

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create Decision Tree Classifier model and fit data
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Make predictions and evaluate accuracy
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Model B : Predicting Shoe Price From Brand and Color
# Load data
climbingshoes_df = pd.read_csv('BackcountryClimbing-Shoes.csv')

# Split data into features and target
X = climbingshoes_df[['Shoe_Color', 'Shoe_Price']]
y = climbingshoes_df['Shoe_Brand']

# Convert categorical color data into numerical data
X = pd.get_dummies(X, columns=['Shoe_Color'])

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create Ridge Classifier model and fit data
model = RidgeClassifier(alpha=0.5)
model.fit(X_train, y_train)

# Make predictions and evaluate accuracy
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)