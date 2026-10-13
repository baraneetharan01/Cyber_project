import argparse
import os
from typing import Any, Dict
import yaml
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split

from src.data_loading.loader import load_csv
from src.features.transformers import infer_feature_types
from src.models.rf import train_random_forest
from src.evaluation.metrics import compute_metrics, save_metrics


def load_config(path: str) -> Dict[str, Any]:
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def ensure_dir(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def main(config_path: str) -> None:
    cfg = load_config(config_path)

    raw_csv_path = cfg["data"]["raw_csv_path"]
    target_column = cfg["data"]["target_column"]
    test_size = float(cfg["data"]["test_size"])  # type: ignore
    random_state = int(cfg["data"]["random_state"])  # type: ignore

    model_type = cfg["model"]["type"]
    rf_params = cfg["model"].get("params", {})

    model_dir = cfg["output"]["model_dir"]
    metrics_path = cfg["output"]["metrics_path"]

    ensure_dir(os.path.dirname(metrics_path) or ".")
    ensure_dir(model_dir)

    df = load_csv(raw_csv_path)
    if target_column not in df.columns:
        raise ValueError(f"Target column '{target_column}' not found in data. Columns: {list(df.columns)}")

    X = df.drop(columns=[target_column])
    y = df[target_column]

    categorical_cols, numerical_cols = infer_feature_types(df, target_column)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=y if y.nunique() > 1 else None
    )

    if model_type != "random_forest":
        raise NotImplementedError(f"Model type '{model_type}' is not implemented in this scaffold.")

    pipeline = train_random_forest(X_train, y_train, categorical_cols, numerical_cols, rf_params)

    y_pred = pipeline.predict(X_test)
    metrics = compute_metrics(y_test, y_pred)
    save_metrics(metrics, metrics_path)

    model_path = os.path.join(model_dir, "model.pkl")
    joblib.dump(pipeline, model_path)
    print(f"Saved model to: {model_path}")
    print(f"Saved metrics to: {metrics_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train threat detection model")
    parser.add_argument("--config", required=True, help="Path to YAML config file")
    args = parser.parse_args()
    main(args.config)


