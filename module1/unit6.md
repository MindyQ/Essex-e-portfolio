# Unit 6 · Principles of Artificial Intelligence (AI) I

> A first machine-learning model — and an honest look at its limits.

## Task / Assignment
Build a binary classifier and report on its performance, limitations and ethics.

### The model
- **Library**: Python + scikit-learn.
- **Task**: predict whether a breast tumour is **benign or malignant** on the public
  **UCI Breast Cancer Wisconsin** dataset (numerical features from cell images).
- **Pipeline**: `StandardScaler` → `LogisticRegression`, trained/tested on an **80/20 split**.
- **Metrics**: accuracy, precision, recall — all high.
  - High **precision** → rarely mislabels benign as malignant (avoids needless anxiety).
  - High **recall** → catches most real malignant cases (dangerous tumours detected reliably).

### Limitations & ethics
- Learns only from **fixed historical data** — struggles with rare/new tumour types outside the distribution.
- No **interpretability**; cannot replace professional medical judgement.
- **Demographic bias** — dataset is region-specific; may underperform on other ages/ethnicities, risking
  diagnostic error.
- Conclusion: an **auxiliary reference only**, never an authoritative medical verdict.

## Code (`Unit6 AI model.py`)
```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score
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
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)

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

## Associated source files
| File | Type | Notes |
|------|------|-------|
| `Unit6 AI model Analysis.txt` | Text | Performance, limitations and ethical discussion |
| `Unit6 AI model.py` | Python | Reproducible training/evaluation script |
