"""Application constants"""

# Report Status
REPORT_STATUS_PENDING = "pending"
REPORT_STATUS_UNDER_REVIEW = "under_review"
REPORT_STATUS_RESOLVED = "resolved"
REPORT_STATUSES = [REPORT_STATUS_PENDING, REPORT_STATUS_UNDER_REVIEW, REPORT_STATUS_RESOLVED]

# Severity Levels
SEVERITY_LOW = "Low"
SEVERITY_MEDIUM = "Medium"
SEVERITY_HIGH = "High"
SEVERITY_CRITICAL = "Critical"
SEVERITY_LEVELS = [SEVERITY_LOW, SEVERITY_MEDIUM, SEVERITY_HIGH, SEVERITY_CRITICAL]

# Abuse Types
ABUSE_TYPES = [
    "Harassment",
    "Discrimination",
    "Bullying",
    "Threat",
    "Assault",
    "Other",
]

# User Roles
ROLE_ADMIN = "admin"
ROLE_MODERATOR = "moderator"
ROLE_ANALYST = "analyst"
ROLES = [ROLE_ADMIN, ROLE_MODERATOR, ROLE_ANALYST]

# File Types
ALLOWED_FILE_TYPES = ["image/jpeg", "image/png", "audio/mpeg", "video/mp4", "application/pdf"]
MAX_FILE_SIZE = 52428800  # 50MB

# Pagination
DEFAULT_PAGE_SIZE = 20
MAX_PAGE_SIZE = 100
