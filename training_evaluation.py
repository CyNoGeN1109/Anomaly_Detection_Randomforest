import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
)

from preproccessing import (
    multi_train_X,
    multi_train_y,
    multi_val_X,
    multi_val_y,
    test_X,
    test_y,
)

CLASS_LABELS = {
    0: "Normal",
    1: "DoS",
    2: "Probe",
    3: "Privilege",
    4: "Access",
}


def train_model() -> RandomForestClassifier:
    """Train RandomForest model for multi-class anomaly detection."""
    model = RandomForestClassifier(random_state=1337)
    model.fit(multi_train_X, multi_train_y)
    return model


def evaluate_split(model, features, target, split_name):
    """Print split metrics and classification report."""
    predictions = model.predict(features)
    labels = list(CLASS_LABELS.keys())
    target_names = list(CLASS_LABELS.values())

    accuracy = accuracy_score(target, predictions)
    precision = precision_score(target, predictions, average="weighted", zero_division=0)
    recall = recall_score(target, predictions, average="weighted", zero_division=0)
    f1 = f1_score(target, predictions, average="weighted", zero_division=0)

    print(f"\n{split_name} Evaluation:")
    print(f"Accuracy: {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall: {recall:.4f}")
    print(f"F1-Score: {f1:.4f}")

    print(f"\nClassification Report for {split_name}:")
    print(
        classification_report(
            target,
            predictions,
            labels=labels,
            target_names=target_names,
            zero_division=0,
        )
    )

    return predictions


def plot_confusion_matrix(y_true, y_pred, title, output_file, enable_plots=False):
    """Save confusion matrix CSV and optionally a heatmap image."""
    labels = list(CLASS_LABELS.keys())
    class_names = list(CLASS_LABELS.values())

    conf_matrix = confusion_matrix(y_true, y_pred, labels=labels)
    conf_df = pd.DataFrame(conf_matrix, index=class_names, columns=class_names)
    csv_file = output_file.replace(".png", ".csv")
    conf_df.to_csv(csv_file)
    print(f"Saved confusion matrix table: {csv_file}")

    if not enable_plots:
        print("Heatmap plotting disabled (set enable_plots=True to generate .png).")
        return

    try:
        import os
        from pathlib import Path

        mpl_cache_dir = Path(".mplconfig")
        mpl_cache_dir.mkdir(exist_ok=True)
        os.environ["MPLCONFIGDIR"] = str(mpl_cache_dir.resolve())

        import matplotlib.pyplot as plt
        import seaborn as sns

        plt.figure(figsize=(8, 6))
        sns.heatmap(
            conf_matrix,
            annot=True,
            fmt="d",
            cmap="Blues",
            xticklabels=class_names,
            yticklabels=class_names,
        )
        plt.title(title)
        plt.xlabel("Predicted")
        plt.ylabel("Actual")
        plt.tight_layout()
        plt.savefig(output_file, dpi=150)
        plt.close()
        print(f"Saved confusion matrix heatmap: {output_file}")
    except Exception as exc:
        print(f"Skipping heatmap plotting due to environment issue: {exc}")


def save_model(model, output_file="network_anomaly_detection_model.joblib"):
    """Persist trained model to disk."""
    joblib.dump(model, output_file)
    print(f"Model saved to {output_file}")


def main():
    rf_model_multi = train_model()
    enable_plots = False

    # Validation set evaluation
    val_predictions = evaluate_split(
        model=rf_model_multi,
        features=multi_val_X,
        target=multi_val_y,
        split_name="Validation Set",
    )
    plot_confusion_matrix(
        y_true=multi_val_y,
        y_pred=val_predictions,
        title="Network Anomaly Detection - Validation Set",
        output_file="confusion_matrix_validation.png",
        enable_plots=enable_plots,
    )

    # Test set evaluation
    test_predictions = evaluate_split(
        model=rf_model_multi,
        features=test_X,
        target=test_y,
        split_name="Test Set",
    )
    plot_confusion_matrix(
        y_true=test_y,
        y_pred=test_predictions,
        title="Network Anomaly Detection - Test Set",
        output_file="confusion_matrix_test.png",
        enable_plots=enable_plots,
    )

    # Save model
    save_model(rf_model_multi)


if __name__ == "__main__":
    main()