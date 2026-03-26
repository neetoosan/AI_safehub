"""Validators for input validation"""


def validate_email(email: str) -> bool:
    """Validate email format"""
    import re

    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email) is not None


def validate_report_text(text: str, min_length: int = 10, max_length: int = 10000) -> bool:
    """Validate report description"""
    if not text:
        return False
    return min_length <= len(text) <= max_length


def validate_severity_score(score: float) -> bool:
    """Validate severity score"""
    return 0.0 <= score <= 10.0


def validate_file_size(file_size: int, max_size: int = 52428800) -> bool:
    """Validate file size (default 50MB)"""
    return 0 < file_size <= max_size
