"""Utility functions and helpers"""


def hash_email(email: str) -> str:
    """Hash email for anonymity"""
    import hashlib

    return hashlib.sha256(email.encode()).hexdigest()


def generate_report_id() -> str:
    """Generate unique report ID"""
    import uuid

    return f"RPT-{uuid.uuid4().hex[:8].upper()}"


def format_timestamp(timestamp) -> str:
    """Format datetime for display"""
    # TODO: Implement
    return ""


def sanitize_input(text: str) -> str:
    """Sanitize user input"""
    # TODO: Implement
    return text.strip()
