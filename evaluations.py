from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    fbeta_score
)


def evaluate(y_true, y_pred):
    accuracy = accuracy_score(y_true, y_pred)
    precision = precision_score(y_true, y_pred)
    recall = recall_score(y_true, y_pred)
    fbeta = fbeta_score(y_true, y_pred, beta=2)
    return {
        "accuracy": accuracy,
        "precision": precision,
        "recall": recall,
        "fbeta": fbeta
    }
