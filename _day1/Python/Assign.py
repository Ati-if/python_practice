# ==========================================
# Task 1: Dataset Loading and Initial View
# ==========================================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, f1_score

# Load the Titanic dataset
url = "https://lms.digiskills.pk/Courses/AIP301/Downloads/titanic.csv"
df = pd.read_csv(url)

# Display total number of rows and columns
print("Total Rows and Columns:", df.shape)

# Display the first 7 rows
df.head(7)


# ==========================================
# Task 2: Data Exploration
# ==========================================
# 1. Calculate and display descriptive statistics for numerical variables
print("--- Descriptive Statistics ---")
display(df.describe())

# 2. Identify numerical and categorical variables
num_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
cat_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()

print("\nNumerical Variables:", num_cols)
print("Categorical Variables:", cat_cols)

# 3. Analyze categorical variables (Sex, Pclass/Passenger class)
print("\n--- Unique Values & Frequency Distributions ---")
print("Unique Sex:", df['Sex'].unique())
print(df['Sex'].value_counts())

print("\nUnique Passenger Class (Pclass):", df['Pclass'].unique())
print(df['Pclass'].value_counts())


# ==========================================
# Task 3: Data Cleaning
# ==========================================
# 1. Count missing values in each column
print("--- Missing Values Before Handling ---")
print(df.isnull().sum())

# 2. Fill missing values using mean or median
# Fill 'Age' missing values with median
if 'Age' in df.columns:
    df['Age'].fillna(df['Age'].median(), inplace=True)

# Fill 'Fare' missing values with median (if any)
if 'Fare' in df.columns:
    df['Fare'].fillna(df['Fare'].median(), inplace=True)

# Fill 'Embarked' missing values with mode
if 'Embarked' in df.columns:
    df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

# Drop 'Cabin' if it exists and has excessive missing values
if 'Cabin' in df.columns:
    df.drop(columns=['Cabin'], inplace=True)

# 3. Verify missing values are handled
print("\n--- Missing Values After Handling ---")
print(df.isnull().sum())


# ==========================================
# Task 4: Feature Selection, Model Training & Evaluation
# ==========================================
# Select relevant features and target
features = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare']
target = 'Survived'

X = df[features].copy()
y = df[target].copy()

# Encode categorical variable 'Sex' (Male: 1, Female: 0)
le = LabelEncoder()
X['Sex'] = le.fit_transform(X['Sex'])

# Divide dataset into training and testing sets (80/20 split)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Feature Scaling for SVC
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Build and train Support Vector Classifier (SVC)
model = SVC(kernel='rbf', random_state=42)
model.fit(X_train_scaled, y_train)

# Make predictions on test data
y_pred = model.predict(X_test_scaled)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print("--- Model Evaluation Metrics ---")
print(f"Accuracy:  {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall:    {recall:.4f}")
print(f"F1-Score:  {f1:.4f}")
print("\nConfusion Matrix:")
print(conf_matrix)


# ==========================================
# Task 5: Data Visualization
# ==========================================
sns.set_theme(style="whitegrid")

# 1. Combined relationship between Gender, Passenger Class, and Survival
plt.figure(figsize=(8, 5))
sns.barplot(data=df, x='Pclass', y='Survived', hue='Sex', ci=None)
plt.title('Survival Rate by Passenger Class and Gender')
plt.ylabel('Survival Rate')
plt.xlabel('Passenger Class (Pclass)')
plt.show()

# 2. Distribution of passenger Fare using a Box Plot (to show skewness/outliers)
plt.figure(figsize=(8, 4))
sns.boxplot(x=df['Fare'], color='skyblue')
plt.title('Distribution of Passenger Fare (Box Plot)')
plt.xlabel('Fare')
plt.show()

# 3. Compare survival and non-survival count between Male and Female passengers
plt.figure(figsize=(7, 5))
sns.countplot(data=df, x='Sex', hue='Survived')
plt.title('Survival vs Non-Survival Count by Gender')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.legend(title='Survived', labels=['No (0)', 'Yes (1)'])
plt.show()