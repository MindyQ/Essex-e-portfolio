# Unit 6 · Principles of Artificial Intelligence (AI) I

The artificial intelligence model uses Python and the Scikit-learn library.It performs binary classification on the publicly available UCI Breast Cancer Wisconsin Dataset. The core task is to predict automatically whether a breast tumour is benign or malignant. These predictions rely on numerical medical features extracted from cell images.

This machine learning solution supports medical screening in three ways. It gives fast and consistent classification results. Moreover, it helps doctors with preliminary tumour diagnosis. Besides, it reduces the manual analysis workload for clinical staff.

The model performance is measured with three standard metrics: accuracy, precision, and recall. After training and testing on an 80-20 data split, it reaches high overall performance. The high accuracy shows that most test samples receive correct predictions. The high precision means the model rarely labels a benign tumour as malignant, which avoids needless medical anxiety. Meanwhile, the high recall shows that the model catches most real malignant cases, so dangerous tumours are detected reliably.

However, there are still clear limitations. The model learns only from fixed historical medical data. It cannot adapt to rare tumour types or new patient cases that fall outside the dataset distribution. In addition, it cannot replace professional medical judgement. It also lacks the interpretability that clinical diagnosis requires.

The ethical concern is demographic bias. The dataset contains patient samples from specific regions only. The model may perform poorly on patients of different ages, ethnicities, or regions. Over-reliance on this tool could cause diagnostic errors and create health risks.

Therefore, the model should serve only as an auxiliary reference. It must not be treated as an authoritative medical conclusion.

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,precision_score, recall_score, classification_report
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_breast_cancer

cancer_data = load_breast_cancer()
df = pd.DataFrame(cancer_data.data, columns=cancer_data.feature_names)
df["target"] = cancer_data.target
df.to_csv("breast_cancer.csv", index=False)

df = pd.read_csv("breast_cancer.csv")
X = df.drop("target",axis=1)
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
