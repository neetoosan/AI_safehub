"""UI Pages Package"""

from .login_page import create_login_page
from .dashboard_page import create_dashboard_page
from .reporter_track_or_report_page import create_reporter_track_or_report_page

__all__ = [
    "create_login_page",
    "create_dashboard_page",
    "create_reporter_track_or_report_page",
]
