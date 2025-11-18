# utils/validation.py
from datetime import datetime

# -------------------------------
# 基本型チェック
# -------------------------------
def check_type(value, expected_type, name="value"):
    if not isinstance(value, expected_type):
        raise TypeError(f"{name} must be {expected_type}, got {type(value)}")
    return True

# -------------------------------
# 必須項目チェック
# -------------------------------
def check_required_keys(data: dict, required_keys: list):
    for key in required_keys:
        if key not in data:
            raise ValueError(f"Missing required key: {key}")
    return True

# -------------------------------
# 範囲チェック
# -------------------------------
def check_range(value, min_value=None, max_value=None, name="value"):
    if min_value is not None and value < min_value:
        raise ValueError(f"{name} must be >= {min_value}, got {value}")
    if max_value is not None and value > max_value:
        raise ValueError(f"{name} must be <= {max_value}, got {value}")
    return True

# -------------------------------
# フォーマットチェック（例：日付や文字列形式）
# -------------------------------
def check_date_format(date_str, fmt="%Y-%m-%d", name="date"):
    try:
        datetime.strptime(date_str, fmt)
    except ValueError:
        raise ValueError(f"{name} must match format {fmt}, got {date_str}")
    return True

def check_string_format(value, allowed_values, name="value"):
    if value not in allowed_values:
        raise ValueError(f"{name} must be one of {allowed_values}, got {value}")
    return True

# -------------------------------
# 一意性チェック
# -------------------------------
def check_unique(items, name="items"):
    if len(items) != len(set(items)):
        raise ValueError(f"{name} contains duplicate values")
    return True

# -------------------------------
# 論理整合性チェック
# -------------------------------
def check_logical_relation(condition, error_message):
    if not condition:
        raise ValueError(error_message)
    return True

# -------------------------------
# Null / None チェック
# -------------------------------
def check_not_none(value, name="value"):
    if value is None:
        raise ValueError(f"{name} must not be None")
    return True

# -------------------------------
# デフォルト値確認
# -------------------------------
def set_default(value, default):
    return value if value is not None else default

# -------------------------------
# 外部制約チェック（例：許可値リスト）
# -------------------------------
def check_allowed_values(value, allowed_values, name="value"):
    if value not in allowed_values:
        raise ValueError(f"{name} must be in {allowed_values}, got {value}")
    return True
