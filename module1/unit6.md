# Unit 6 · Principles of Artificial Intelligence (AI) I

> A binary classification model for breast-cancer screening, built with Scikit-learn.

## What the model does
The AI model uses Python and the Scikit-learn library to perform **binary classification** on the public UCI Breast Cancer Wisconsin Dataset. Its core task is to predict automatically whether a tumour is **benign or malignant**, based on numerical medical features extracted from cell images.

This supports medical screening in three ways: fast, consistent classification; assistance with preliminary diagnosis; and a reduced manual workload for clinical staff.

## How performance is measured
The model is evaluated with three standard metrics on an 80-20 train/test split:
- **Accuracy** — most test samples get the correct prediction.
- **Precision** — the model rarely labels a benign tumour as malignant, avoiding needless anxiety.
- **Recall** — the model catches most real malignant cases, so dangerous tumours are detected reliably.

## Limitations & ethical concern
The model learns only from fixed historical data, so it cannot adapt to rare tumour types or new patient cases outside the dataset distribution. It also lacks the interpretability clinical diagnosis requires and must not replace professional medical judgement.

The key ethical risk is **demographic bias**: the dataset covers only specific regions, so the model may perform poorly for patients of different ages, ethnicities, or regions. Over-reliance could cause diagnostic errors and health risks. The model should serve only as an auxiliary reference, never as an authoritative conclusion.

## Code (`Unit6 AI model.py`)
```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, classification_report
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_breast_cancer

cancer_data = load_breast_cancer()
df = pd.DataFrame(cancer_data.data, columns=cancer_data.feature_names)
df["target"] = cancer_data.target
df.to_csv("breast_cancer.csv", index=False)

df = pd.read_csv("breast_cancer.csv")
X = df.drop("target", axis=1)
y = df["target"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

model = Pipeline([
    ("scaler", StandardScaler()),
    ("classifier", LogisticRegression())
])
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred))
print("Recall:", recall_score(y_test, y_pred))
```
