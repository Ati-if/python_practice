# ==========================================
# IMPORT REQUIRED LIBRARIES
# ==========================================
import importlib
import re
import string
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def display(obj):
    ipython_display = importlib.import_module('IPython.display') if importlib.util.find_spec('IPython') is not None else None
    if ipython_display is not None:
        ipython_display.display(obj)
    else:
        print(obj)


def optional_import(module_name):
    try:
        return importlib.import_module(module_name)
    except ImportError:
        return None


sns = optional_import('seaborn')

sklearn = optional_import('sklearn')
if sklearn is not None:
    train_test_split = sklearn.model_selection.train_test_split
    LabelEncoder = sklearn.preprocessing.LabelEncoder
    classification_report = sklearn.metrics.classification_report
    confusion_matrix = sklearn.metrics.confusion_matrix
else:
    train_test_split = None
    LabelEncoder = None
    classification_report = None
    confusion_matrix = None

tf = optional_import('tensorflow')
if tf is not None:
    keras_text = optional_import('tensorflow.keras.preprocessing.text')
    keras_sequence = optional_import('tensorflow.keras.preprocessing.sequence')
    keras_models = optional_import('tensorflow.keras.models')
    keras_layers = optional_import('tensorflow.keras.layers')

    Tokenizer = keras_text.Tokenizer if keras_text is not None else None
    pad_sequences = keras_sequence.pad_sequences if keras_sequence is not None else None
    Sequential = keras_models.Sequential if keras_models is not None else None
    Embedding = keras_layers.Embedding if keras_layers is not None else None
    LSTM = keras_layers.LSTM if keras_layers is not None else None
    Dense = keras_layers.Dense if keras_layers is not None else None
    Dropout = keras_layers.Dropout if keras_layers is not None else None
else:
    Tokenizer = None
    pad_sequences = None
    Sequential = None
    Embedding = None
    LSTM = None
    Dense = None
    Dropout = None

# ==========================================
# TASK 1: Dataset Loading and Initial Exploration
# ==========================================
print("--- TASK 1 ---")
# 1. Load dataset
script_dir = Path(__file__).resolve().parent
candidate_paths = [
    script_dir / 'toxic_comments_dataset.csv',
    script_dir.parent / 'toxic_comments_dataset.csv',
    Path.cwd() / 'toxic_comments_dataset.csv',
]

dataset_path = next((path for path in candidate_paths if path.exists()), None)

if dataset_path is None:
    print("Dataset file not found. Creating a sample dataset so the script can run.")
    df = pd.DataFrame({
        'comment_text': [
            'you are so stupid and ugly',
            'i love this product it is great',
            'you idiot stop bothering me',
            'this is a wonderful day',
            'i hate this nonsense and trash',
            'thanks for helping me today',
            'you are useless and annoying',
            'excellent work and good effort'
        ],
        'label': ['toxic', 'non_toxic', 'toxic', 'non_toxic', 'toxic', 'non_toxic', 'toxic', 'non_toxic']
    })
else:
    df = pd.read_csv(dataset_path)

# Display first 10 and last 8 records
print("\nFirst 10 records:")
display(df.head(10))

print("\nLast 8 records:")
display(df.tail(8))

# Dataset Shape
print("\nDataset Shape (Rows, Columns):", df.shape)

# 2. Column names and Data types
print("\nColumn Names and Data Types:")
print(df.dtypes)

# 3. Statistical summary of numerical columns
print("\nStatistical Summary of Numerical Columns:")
display(df.describe())


# ==========================================
# TASK 2: Text Cleaning, Preprocessing and Data Quality
# ==========================================
print("\n--- TASK 2 ---")

# Identify comment and target columns dynamically
comment_col = [col for col in df.columns if 'comment' in col.lower()][0]
target_col = [col for col in df.columns if col != comment_col][0]

# 2. Check duplicates and missing values prior to cleaning
print(f"Number of duplicate records before cleaning: {df.duplicated().sum()}")
print("Missing values in each column before cleaning:")
print(df.isnull().sum())

# 1 & 3. Text cleaning function
def clean_text(text):
    if not isinstance(text, str):
        return ""
    text = text.lower() # Lowercase
    text = re.sub(r'<.*?>', '', text) # Remove HTML tags
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE) # Remove URLs
    text = re.sub(r'\d+', '', text) # Remove numbers
    text = text.translate(str.maketrans('', '', string.punctuation)) # Remove punctuation
    text = re.sub(r'[^\w\s]', '', text) # Remove special characters / emojis
    text = re.sub(r'\s+', ' ', text).strip() # Remove extra spaces
    return text

# Apply cleaning
df[comment_col] = df[comment_col].apply(clean_text)

# Handle missing/empty comments after cleaning
df = df[df[comment_col].str.strip() != ""]
df.dropna(subset=[comment_col, target_col], inplace=True)

# Remove duplicates
df.drop_duplicates(subset=[comment_col], inplace=True)
print(f"\nDataset shape after handling duplicates and missing values: {df.shape}")

# Encode Target Variable if it is categorical/text
if LabelEncoder is None:
    raise ImportError("Scikit-learn is required to run this project. Please install it with: pip install scikit-learn")

le = LabelEncoder()
df['encoded_target'] = le.fit_transform(df[target_col])
num_classes = len(np.unique(df['encoded_target']))

# Train-Test Split
if train_test_split is None:
    raise ImportError("Scikit-learn is required to run this project. Please install it with: pip install scikit-learn")

X = df[comment_col].values
y = df['encoded_target'].values

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)


# ==========================================
# TASK 3: NLP Tokenization and Sequence Padding
# ==========================================
print("\n--- TASK 3 ---")

# Hyperparameters
MAX_WORDS = 10000
MAX_LEN = 100

if Tokenizer is None or pad_sequences is None or Sequential is None:
    raise ImportError("TensorFlow is required to run the NLP model. Please install it with: pip install tensorflow")

# 1. Tokenizer on training text only
tokenizer = Tokenizer(num_words=MAX_WORDS, oov_token="<OOV>")
tokenizer.fit_on_texts(X_train)

# 2. Convert to numerical sequences
train_sequences = tokenizer.texts_to_sequences(X_train)
test_sequences = tokenizer.texts_to_sequences(X_test)

# 3. Apply padding/truncation
X_train_padded = pad_sequences(train_sequences, maxlen=MAX_LEN, padding='post', truncating='post')
X_test_padded = pad_sequences(test_sequences, maxlen=MAX_LEN, padding='post', truncating='post')

print("X_train_padded shape:", X_train_padded.shape)
print("X_test_padded shape:", X_test_padded.shape)


# ==========================================
# TASK 4: Train and Validate the Deep Learning Model
# ==========================================
print("\n--- TASK 4 ---")

# Build Model (Embedding, LSTM/Model, Dropout, Dense, Softmax)
model = Sequential([
    Embedding(input_dim=MAX_WORDS, output_dim=128, input_length=MAX_LEN),
    LSTM(64, return_sequences=False),
    Dropout(0.5),
    Dense(64, activation='relu'),
    Dropout(0.3),
    Dense(num_classes, activation='softmax' if num_classes > 2 else 'sigmoid')
])

loss_fn = 'sparse_categorical_crossentropy' if num_classes > 2 else 'binary_crossentropy'

model.compile(
    optimizer='adam',
    loss=loss_fn,
    metrics=['accuracy']
)

model.summary()

# Train Model
history = model.fit(
    X_train_padded, y_train,
    validation_split=0.2,
    epochs=10,
    batch_size=32,
    verbose=1
)


# ==========================================
# TASK 5: Evaluate, Plotting and Visualize Model Performance
# ==========================================
print("\n--- TASK 5 ---")

# 2. Evaluate on Test Dataset
test_loss, test_acc = model.evaluate(X_test_padded, y_test, verbose=0)
print(f"Test Loss: {test_loss:.4f}")
print(f"Test Accuracy: {test_acc:.4f}")

# Get Predictions
y_pred_probs = model.predict(X_test_padded)
y_pred = np.argmax(y_pred_probs, axis=1) if num_classes > 2 else (y_pred_probs > 0.5).astype(int).reshape(-1)

# 3. Classification Report
print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=[str(c) for c in le.classes_]))

# 1. Confusion Matrix
plt.figure(figsize=(8, 6))
cm = confusion_matrix(y_test, y_pred)
if sns is not None:
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
                xticklabels=le.classes_, yticklabels=le.classes_)
else:
    print("Confusion Matrix:\n", cm)
plt.title('Confusion Matrix')
plt.xlabel('Predicted Label')
plt.ylabel('True Label')
plt.tight_layout()
plt.show()

# Training Performance Curves (Accuracy & Loss)
plt.figure(figsize=(12, 4))

plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'], label='Train Accuracy')
plt.plot(history.history['val_accuracy'], label='Val Accuracy')
plt.title('Model Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(history.history['loss'], label='Train Loss')
plt.plot(history.history['val_loss'], label='Val Loss')
plt.title('Model Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()

plt.tight_layout()
plt.show()