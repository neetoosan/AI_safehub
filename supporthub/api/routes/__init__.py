"""API Routes Package"""

from .reports import ReportRoutes
from .analytics import AnalyticsRoutes
from .admin import AdminRoutes

__all__ = ["ReportRoutes", "AnalyticsRoutes", "AdminRoutes"]
