# Import necessary libraries
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib
import json

if __name__ == '__main__':
    # Load the Iris dataset
    iris = load_iris()
    X, y = iris.data, iris.target

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # Train a Random Forest classifier (small change: n_estimators + max_depth)
    model = RandomForestClassifier(n_estimators=150, max_depth=4, random_state=42)
    model.fit(X_train, y_train)

    # Evaluate
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)

    # Save the model
    joblib.dump(model, 'iris_model.pkl')

    # Save metrics (makes your submission clearly different)
    metrics = {
        "accuracy": acc,
        "n_estimators": 150,
        "max_depth": 4,
        "test_size": 0.2,
        "random_state": 42
    }
    with open("metrics.json", "w") as f:
        json.dump(metrics, f, indent=2)

    print("Model training was successful! ")
    print(f"Accuracy: {acc:.4f}")
    print("Classification Report:")
    print(classification_report(y_test, y_pred, target_names=iris.target_names))