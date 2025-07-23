import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import pickle

df = pd.read_csv('Salary_Data.csv')

# Rename columns for easier access
df.rename(columns={
    'Education Level': 'Education',
    'Job Title': 'JobTitle',
    'Years of Experience': 'YearsExperience'
}, inplace=True)

# Drop rows with missing values in relevant columns
df.dropna(subset=['Salary', 'YearsExperience', 'Age', 'Gender', 'Education', 'JobTitle'], inplace=True)

# Prepare features and target
X = pd.get_dummies(df[['YearsExperience', 'Age', 'Gender', 'Education', 'JobTitle']], drop_first=True)
y = df['Salary']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save model
with open('salary_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model training complete and saved as salary_model.pkl")
