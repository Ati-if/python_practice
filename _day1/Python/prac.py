import io
import warnings
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import requests
import seaborn as sns
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score, precision_score, recall_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.svm import SVC

warnings.filterwarnings("ignore", category=Warning)

PROJECT_ROOT = Path(__file__).resolve().parent
DATASET_URL = "https://lms.digiskills.pk/Courses/AIP301/Downloads/titanic.csv"


def load_dataset() -> pd.DataFrame:
    local_candidates = [
        PROJECT_ROOT / "titanic.csv",
        PROJECT_ROOT / "data" / "titanic.csv",
        PROJECT_ROOT.parent / "titanic.csv",
    ]

    for path in local_candidates:
        if path.exists():
            print(f"Loading Titanic dataset from local file: {path}")
            return pd.read_csv(path)

    try:
        print("Downloading Titanic dataset from remote URL...")
        response = requests.get(DATASET_URL, timeout=20, verify=False)
        response.raise_for_status()
        return pd.read_csv(io.StringIO(response.text))
    except Exception as exc:
        print(f"Remote dataset unavailable: {exc}")
        print("Creating a small Titanic-style sample dataset for demo purposes.")
        return pd.DataFrame(
            {
                "PassengerId": [1, 2, 3, 4, 5, 6, 7, 8],
                "Survived": [0, 1, 1, 0, 1, 0, 1, 0],
                "Pclass": [3, 1, 3, 1, 2, 3, 1, 2],
                "Name": [
                    "Braund, Mr. Owen Harris",
                    "Cumings, Mrs. John Bradley",
                    "Heikkinen, Miss. Laina",
                    "Futrelle, Mrs. Jacques Heath",
                    "Allen, Mr. William Henry",
                    "Moran, Mr. James",
                    "McCarthy, Mr. Timothy J",
                    "Palsson, Master. Gosta",
                ],
                "Sex": ["male", "female", "female", "female", "male", "male", "male", "male"],
                "Age": [22, 38, 26, 35, 35, 28, 54, 4],
                "SibSp": [1, 1, 0, 1, 0, 0, 0, 3],
                "Parch": [0, 0, 0, 0, 0, 0, 0, 1],
                "Fare": [7.25, 71.28, 7.92, 53.10, 8.05, 8.46, 51.86, 21.07],
                "Embarked": ["S", "C", "S", "S", "S", "Q", "S", "S"],
            }
        )


def clean_dataset(df: pd.DataFrame) -> pd.DataFrame:
    cleaned = df.copy()

    if "Age" in cleaned.columns:
        cleaned["Age"] = cleaned["Age"].fillna(cleaned["Age"].median())
    if "Fare" in cleaned.columns:
        cleaned["Fare"] = cleaned["Fare"].fillna(cleaned["Fare"].median())
    if "Embarked" in cleaned.columns:
        cleaned["Embarked"] = cleaned["Embarked"].fillna(cleaned["Embarked"].mode()[0])
    if "Cabin" in cleaned.columns:
        cleaned.drop(columns=["Cabin"], inplace=True)

    return cleaned


def explore_data(df: pd.DataFrame) -> None:
    print("Total Rows and Columns:", df.shape)
    print("\nFirst 7 Rows:")
    print(df.head(7))

    print("\n--- Descriptive Statistics ---")
    print(df.describe())

    num_cols = df.select_dtypes(include=["int64", "float64"]).columns.tolist()
    cat_cols = df.select_dtypes(include=["object", "category"]).columns.tolist()

    print("\nNumerical Variables:", num_cols)
    print("Categorical Variables:", cat_cols)

    print("\n--- Unique Values & Frequency Distributions ---")
    if "Sex" in df.columns:
        print("Unique Sex:", df["Sex"].unique())
        print(df["Sex"].value_counts())

    if "Pclass" in df.columns:
        print("\nUnique Passenger Class (Pclass):", df["Pclass"].unique())
        print(df["Pclass"].value_counts())

    print("\n--- Missing Values Before Handling ---")
    print(df.isnull().sum())


def train_model(df: pd.DataFrame):
    features = ["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare"]
    target = "Survived"

    X = df[features].copy()
    y = df[target].copy()

    label_encoder = LabelEncoder()
    X["Sex"] = label_encoder.fit_transform(X["Sex"])

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    model = SVC(kernel="rbf", random_state=42)
    model.fit(X_train_scaled, y_train)

    y_pred = model.predict(X_test_scaled)

    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    conf_matrix = confusion_matrix(y_test, y_pred)

    print("\n--- Model Evaluation Metrics ---")
    print(f"Accuracy:  {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall:    {recall:.4f}")
    print(f"F1-Score:  {f1:.4f}")
    print("\nConfusion Matrix:")
    print(conf_matrix)

    return model, X, y


def plot_results(df: pd.DataFrame) -> None:
    sns.set_theme(style="whitegrid")

    plt.figure(figsize=(8, 5))
    sns.barplot(data=df, x="Pclass", y="Survived", hue="Sex", ci=None)
    plt.title("Survival Rate by Passenger Class and Gender")
    plt.ylabel("Survival Rate")
    plt.xlabel("Passenger Class")
    plt.show()

    plt.figure(figsize=(8, 4))
    sns.boxplot(x=df["Fare"], color="skyblue")
    plt.title("Distribution of Passenger Fare")
    plt.xlabel("Fare")
    plt.show()

    plt.figure(figsize=(7, 5))
    sns.countplot(data=df, x="Sex", hue="Survived")
    plt.title("Survival vs Non-Survival Count by Gender")
    plt.xlabel("Gender")
    plt.ylabel("Count")
    plt.legend(title="Survived", labels=["No (0)", "Yes (1)"])
    plt.show()


def main() -> None:
    df = load_dataset()
    explore_data(df)

    df = clean_dataset(df)
    print("\n--- Missing Values After Handling ---")
    print(df.isnull().sum())

    train_model(df)
    plot_results(df)


if __name__ == "__main__":
    main()
